import django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import *

class IndexView(generic.ListView):
    """
    Index view class.

    Attributes
    ----------
    template_name : str
        Template name.
    context_object_name : str
        Context object name
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self) -> django.db.models.query.QuerySet[Question]:
        """
        Return the last five published questions.

        Returns
        -------
        django.db.models.query.QuerySet[Question]
            The lastest five published questions.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """
    Detail view class.

    Attributes
    ----------
    template_name : str
        Template name.
    model: : class
        Class of the model
    """
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self) -> models.query.QuerySet[Question]:
        """
        Excludes any questions that are not published yet.

        Returns
        -------
        models.query.QuerySet[Question]
            Filtered question set.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    """
    Result view class.

    Attributes
    ----------
    template_name : str
        Template name.
    model: : class
        Class of the model
    """
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    """
    View for voting on a specified question.

    Parameters
    ----------
    request : HttpRequest
        Http request.
    question_id : int
        Question ID.

    Returns
    -------
    HttpResponse
        Http response
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You do not select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
