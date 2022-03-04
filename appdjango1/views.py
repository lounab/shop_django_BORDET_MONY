from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Question
from .forms import Appform
from .forms import Achatform
from django.utils import timezone

from django.shortcuts import render


def index(request):

    return render(request,'appdjango1/index.html')


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Question.objects.all()
    form = Appform(request.POST or None)
    if form.is_valid():
        form.save()

        return HttpResponseRedirect("/appdjango1/list")
         
    context['form']= form
         
    return render(request, "appdjango1/list_view.html", context)


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    
 
    # add the dictionary during initialization
    context["data"] = Question.objects.get(id = id)

    obj = get_object_or_404(Question, id = id)
    quantite_stock = obj.quantite

    form = Achatform(request.POST or None, instance = obj)
    if form.is_valid():
        quantite_achat = obj.quantite
        stock_restant = quantite_stock-quantite_achat
        obj.quantite = stock_restant
        form.save()

        return HttpResponseRedirect("/appdjango1/list")
         
    context['form']= form

         
    return render(request, "appdjango1/detail_view.html", context)

 
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
 
    # pass the object as instance in form
    form = Appform(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appdjango1/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "appdjango1/update_view.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/appdjango1/list")
 
    return render(request, "appdjango1/delete_view.html", context)


def login(request):
    context ={}

    login = "user"
    mdp = "1234"

    form = Appform(request.POST or None)
    if form.is_valid():
        #if login = True :
            #if mdp = True :
                #acceder à la page list

        form.save()
        return HttpResponseRedirect("/appdjango1/list")


    return render(request, "appdjango1/login.html", context)



def chat(request):

    return render(request, 'appdjango1/chat.html')

def room(request, room_name):
    return render(request, 'appdjango1/room.html', {
        'room_name': room_name
    })


