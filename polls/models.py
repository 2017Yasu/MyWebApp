from django.db import models

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
