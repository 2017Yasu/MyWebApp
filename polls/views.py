from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You are at the polls index")

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
    return HttpResponse("You are looking at question %s." % question_id)

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
