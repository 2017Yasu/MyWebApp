from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path

# Create your views here.
def index(request):
    my_dict = {
        'insert_something' : "views.pyのinsert_something部分",
        'name' : "Nakayama",
        'test_items' : ["item1", "item2", "item3"],
    }
    return render(request, 'ledger/index.html', my_dict)

def page1(request):
    return render(request, 'ledger/page1.html')

def page2(request):
    return render(request, 'ledger/page2.html')
