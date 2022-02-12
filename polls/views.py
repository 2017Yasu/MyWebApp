from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from .models import *

# Create your views here.
def index(request):
    """
    Index page.

    Parameters
    ----------
    request : HttpRequest
        Http request.

    Returns
    -------
    HttpResponse
        Http response
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """
    View for displaying question text and vote form.

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
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    View for displaying the result of a specified question.

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
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)

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
    return HttpResponse("You are voting on question %s." % question_id)
