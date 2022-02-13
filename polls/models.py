import datetime
from xmlrpc.client import boolean

from django.db import models
from django.utils import timezone

from django.contrib import admin

# Create your models here.

class Question(models.Model):
    """
    Question.

    Attributes
    ----------
    question_text : CharField
        Text of this question.
    pub_date : DateTimeField
        Date of publication.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @admin.display(boolean=True, ordering='pub_date', description='Published recently?')
    def was_published_recently(self) -> bool:
        """
        Whether this question was published recently.

        Returns
        -------
        bool
            true if this question was published within 1 day.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self) -> str:
        """
        Generate question text

        Returns
        -------
        str
            Question text string
        """
        return self.question_text

class Choice(models.Model):
    """
    Choice of a question.

    Attributes
    ----------
    question : ForeignKey
        Key to the corresponding question.
    choice_text : CharField
        Text of this choice.
    votes : IntegerField
        Number of votes for this choice.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        """
        Generate choice text

        Returns
        -------
        str
            Choice text string
        """
        return self.choice_text
