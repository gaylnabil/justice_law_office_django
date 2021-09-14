
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from justice.forms import CommentForm, QuestionForm, SubCommentForm
from justice.models import Question, Comment, SubComment
from accounts.utils import CITIES
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Count
from accounts.models import Attorney, Types
from justice.models import Category
from django.urls import reverse
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.db.models import Q, Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.postgres.search import SearchVector, SearchQuery, TrigramSimilarity
from django.apps import apps
from django.template import loader

# Create your views here.

ATTORNEYS_PER_PAGE = 2
QUESTIONS_PER_PAGE = 3


def similarity_filter(qs, char_field=None, search_string=None, threshold=0.5):
    return qs.annotate(similarity=TrigramSimilarity(char_field, search_string)).filter(similarity__gt=threshold)


def index(request):
    context = {
        'title': _('page d\'acceuil'),
        'active_page': 'home',
    }
    return render(request, 'index.html', context)


def attorneys_list(request):
    query = request.GET.get('query', '')
    city = request.GET.get('city', '')
    page = request.GET.get('page', 1)

    attorneys = Attorney.objects.annotate(search=SearchVector('first_name', 'last_name', 'city', 'is_active')).filter(
        Q(search__icontains=query) & Q(search__icontains=city) & Q(is_active=True))
    # attorneys = Attorney.objects.filter(Q(first_name__trigram_similar=query) | Q(last_name__trigram_similar=query))
    # attorneys = Attorney.objects.filter(first_name__search=query)
    print(attorneys)
    # attorneys = Attorney.objects.filter(Q(first_name__trigram_similar=query) | Q(last_name__trigram_similar=query))
    paginator = Paginator(attorneys, ATTORNEYS_PER_PAGE)

    try:
        attorneys = paginator.page(page)
    except PageNotAnInteger:
        page = ATTORNEYS_PER_PAGE
        attorneys = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        attorneys = paginator.page(page)

    title = _(f'List des avocats')

    context = {
        'title': title + f' ({page})',
        'inner_title': title,
        'breadcrumb': _('Consultation'),
        'attorneys': attorneys,
        'query': query,
        'cities': CITIES,
        'current_city': city,
        'page': page,
        'active_page': 'attorneys',
    }
    return render(request, 'justice/attorneys_list.html', context)


def attorney_details(request, id):
    attorney = Attorney.objects.filter(pk=id).first()

    # if attorney is not None:
    #     ...

    context = {
        'title': _('Information d\'avocat'),
        'inner_title': _('Details d\'avocat'),
        'breadcrumb': _('Details'),
        'attorney': attorney,
        'active_page': 'attorneys',
    }
    return render(request, 'justice/attorney_details.html', context)


def contact(request):
    template_name = 'justice/contact.html'
    value = _('Contacts')
    context = {
        'title': value,
        'inner_title': _('Details Contacts'),
        'breadcrumb': value,
        'active_page': 'contact',
    }
    return render(request, template_name, context)


def faq(request):
    template_name = 'justice/faq.html'
    value = _('FAQ')
    context = {
        'title': value,
        'inner_title': value,
        'breadcrumb': _('Details FAQ'),
        'active_page': 'faq',
    }
    return render(request, template_name, context)


def justice_question(request):

    user = request.user
    if user is None or not user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    template_name = 'justice/questions.html'

    #questions = Question.objects.order_by('-created_at')

    # query = request.GET.get('query', '')
    # city = request.GET.get('city', '')
    page = request.GET.get('page', 1)

    questions = Question.objects.annotate(comments__count=Count('comments', distinct=True)).annotate(
        subcomments__count=Count('comments__subcomments', distinct=True)).order_by('-created_at')

    paginator = Paginator(questions, QUESTIONS_PER_PAGE)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        page = QUESTIONS_PER_PAGE
        questions = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        questions = paginator.page(page)

    categories = Category.objects.all()
    form = QuestionForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            question = form.save(commit=False)

            if user.type == Types.CLIENT:
                # client = Client.objects.get(pk=user)
                question.client = user.client  # inherited
            else:
                question.attorney = user

            question.save()
            return redirect('justice_question')

    value = _('Questions')
    context = {
        'title': value,
        'inner_title': value,
        'breadcrumb': _('Details Questions'),
        'active_page': 'questions',
        'form': form,
        'questions': questions,
        'categories': categories,
    }

    return render(request, template_name, context)


def justice_comments(request, id=1):

    user = request.user
    if user is None or not user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    # question = Question.objects.filter(pk=id).first()

    question = Question.objects.annotate(Count('comments', distinct=True)).annotate(
        subcomments__count=Count('comments__subcomments', distinct=True)).filter(pk=id).first()

    # print('Children : ', children)
    # print('count : ', vars(question))

    template_name = 'justice/comments.html'

    categories = Category.objects.all()

    context = {}

    if question is None:
        return render(request, template_name, context)

    value = question.title
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            cmt = form.save(commit=False)

            cmt.question = question
            type = 0
            if user.type == Types.CLIENT:
                # client = Client.objects.get(pk=user)
                cmt.client = user.client  # inherited
            else:
                type = 1
                cmt.attorney = user

            cmt.save()
            comment = {
                'text':  cmt.text,
                'type': type,
                'fullName': user.__str__(),
                'created_at': cmt.created_at,
                'updated_at': cmt.updated_at,
                'id': cmt.pk,
            }

            # comment = {
            #     'text':  cmt.text,
            #     'type': type,
            #     'fullName': user.__str__(),
            #     'created_at': '10/10/2020 18:08:49',
            #     'updated_at': '20/11/2020 22:23:55',
            #     'id': 1588,
            # }
            # obj = serializers.serialize('json', [sub, ])
            return JsonResponse({'comment': comment})

            # comment.save()
            # return redirect('justice_comments', id=question.pk)

    subForm = SubCommentForm()

    # obj = serializers.serialize('json', [question])
    # print("Nabil :", type(obj))
    context = {
        'title': value,
        'inner_title': value,
        'breadcrumb': _('Details Question'),
        'active_page': 'questions',
        'qst': question,
        'categories': categories,
        'form': form,
        'subForm': subForm
    }
    return render(request, template_name, context)


def justice_subcomments(request, id=1):

    user = request.user
    if user is None or not user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    comment = Comment.objects.filter(pk=id).first()

    # template_name = 'justice/comments.html'

    form = SubCommentForm(request.POST or None)
    sub = None
    if request.method == 'POST':
        if form.is_valid():

            sub = form.save(commit=False)

            sub.comment = comment
            type = 0  # client
            if user.type == Types.CLIENT:
                # client = Client.objects.get(pk=user)
                sub.client = user.client  # inherited
            else:
                sub.attorney = user
                type = 1  # attorney

            sub.save()

            print(user.__str__())

            subComment = {
                'text':  sub.text,
                'type': type,
                'fullName': user.__str__(),
                'created_at': sub.created_at,
                'updated_at': sub.updated_at,
                'cmt_id': comment.pk,
            }
            # obj = serializers.serialize('json', [sub, ])
            return JsonResponse({'subComment': subComment})

    # context = {
    #     'form': form,
    #     'sub': sub
    # }

    return False


def justice_delete(request, id=0, name=None):

    user = request.user
    if user is None or not user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    name = name.capitalize() if not name is None else None

    if not name is None:

        # apps.get_model("app_name", "model_name")
        model = apps.get_model("justice", name)
        print('model : ', model)
        model = model.objects.filter(pk=id).first()

        print("model_name : ", name)

        print('model Data : ', model)

        redirect_to = redirect('home')
        msg = None

        if name.lower() == 'question':
            msg = "Votre Question a été supprimer avec succés"
            redirect_to = redirect('justice_question')

        elif name.lower() == 'comment':

            msg = "Votre Commentaire a été supprimer avec succés"
            question = model.question
            redirect_to = redirect('justice_comments', id=question.id)

        else:

            msg = "Votre Sous Commentaire a été supprimer avec succés"
            question = model.comment.question
            # sub = SubComment.objects.filter().first()
            # print('justice_question : comment ', sub.comment)
            # print('justice_question : sub comment ', sub.comment.question)

            redirect_to = redirect('justice_comments', id=question.id)
        model.delete()

        if not msg is None:
            messages.Info(request, msg)

        return redirect_to


def content_subcomment(request, id=0):

    template_name = 'justice/subcomment.html'
    subForm = SubCommentForm()
    sub_html = loader.render_to_string(
        template_name,
        {
            'id': id,
            'leaveAnswer': _('Laissez une réponse'),
            'answer': _('Réponse'),
            'subForm': subForm
        },
        request=request
    )

    output_data = {
        'sub_html': sub_html,
    }
    print(output_data)

    return JsonResponse(output_data)
