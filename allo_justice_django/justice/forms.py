
from django import forms
from accounts.models import Schedule
from django.utils.translation import gettext as _
from justice.models import Comment, Question, SubComment


class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        defaultValue = _('Choisissez le catégorie')
        self.fields['category'].empty_label = f'---{defaultValue}---'
        # variants = Category.objects.order_by('name')
        # categories = [(cat.id, cat.name) for cat in variants]
        # self.fields['category'] = forms.ChoiceField(choices=variants)

    # Metadata
    class Meta:
        model = Question
        fields = ('title', 'text', 'category', 'attorney', 'client')

        labels = {
            'title': _('Titre'),
            'text': _('Posez une Question'),
            'category': _('Catégorie'),
        }


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = False
        self.fields['text'].widget.attrs['rows'] = 2

    # Metadata
    class Meta:
        model = Comment
        fields = ('text', 'attorney', 'client')


class SubCommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SubCommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = False
        self.fields['text'].widget.attrs['rows'] = 2

    # Metadata
    class Meta:
        model = SubComment
        fields = ('text', 'attorney', 'client')


class ScheduleAttorneyForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = '__all__'
        # exclude = ['attorney']
        labels = {
            'day_name': _('Jour'),
            'time_from': _('De'),
            'time_to': _('à'),
        }

    def __init__(self, *args, **kwargs):
        super(ScheduleAttorneyForm, self).__init__(*args, **kwargs)

        self.fields['day_name'].widget.attrs['readonly'] = 'readonly'
        self.fields['day_name'].widget.attrs['class'] = 'day_name'
        self.fields['day_name'].widget.attrs['style'] = 'border-color: transparent;'
        self.fields['day_name'].widget.attrs['style'] = 'background-color: transparent;'
        # Textarea(attrs={'style': 'border-color: orange;'}),
