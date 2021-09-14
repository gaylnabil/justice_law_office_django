from django.db import models
from accounts.models import Attorney
from clients.models import Client
from django.utils.translation import gettext as _
# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=255, blank=False,
                            null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'categories'


class Question(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='questions')

    tags = models.CharField(_("Tags"), null=True, blank=True, max_length=255)

    attorney = models.ForeignKey(
        Attorney, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='questions_attorney')

    client = models.ForeignKey(
        Client, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='questions_client')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'question'
        managed = True
        verbose_name = 'Question'
        verbose_name_plural = 'questions'


class Comment(models.Model):
    text = models.TextField(null=False, blank=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='comments')  # related_name='comments' means : Question.objects.get(id=id).comments.all()

    attorney = models.ForeignKey(
        Attorney, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='comments_attorney')

    client = models.ForeignKey(
        Client, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='comments_client')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'comment'
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class SubComment(models.Model):
    text = models.TextField(null=False, blank=False)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='subcomments')

    attorney = models.ForeignKey(
        Attorney, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='subcomments_attorney')

    client = models.ForeignKey(
        Client, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='subcomments_client')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'subcomment'
        managed = True
        verbose_name = 'SubComment'
        verbose_name_plural = 'SubComments'
