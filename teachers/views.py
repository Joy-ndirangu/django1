from django.shortcuts import render, redirect
from .models import Students, Sliders

from django.http import HttpResponse

#for alerts import
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, 'home.html', {'navbar': 'home'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})


def add(request):
    return render(request, "add.html", {'navbar': 'add'})


#def viewdata(request):
    # retrieving data from db and storing it in a variable . lets call the variable data
    #data = Students.objects.all()
    #return render(request, "viewdata.html", {'navbar': 'viewdata', 'data': data})

#adding paginations
def viewdata(request):
    #getting all items and specifying how many items should be there per page and storing them in a variable calle dpaginate
    paginate = Paginator(Students.objects.all(),2)
    page = request.GET.get('page')
    data = paginate.get_page(page)
    return render(request, "viewdata.html", {'navbar': 'viewdata', 'data': data})





def delete(request, id):
    std = Students.objects.get(id=id)
    std.delete()

    messages.warning(request, "Record deleted successfully")
    return redirect("/viewdata")


# writing a function that enables user entered data to be stored in db

def insertdata(request):
    # verifying if form method is post
    if request.method == "POST":
        # if yes gets the user input  and stores them  in a variable ith the same exact name as the input
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        # for image
        # checking if image is existing
        if len(request.FILES) != 0:
            image = request.FILES['image']

        # creating a variable that matches the columns in the model Students with the variable names we have above
        query = Students(name=name, email=email, phone=phone, image=image)
        # after comparing save everything in query using save()method
        query.save()

        # for alerts. Message below shows if saved successfully

        messages.success(request, "Record added successfully")

        return redirect("/viewdata")
    return redirect("/viewdata")
    # make sure to call this function in the form action attribute.
    # pass the insertdata path to it


# editing data
def edit(request, id):
    # verifying if form method is post

    if request.method == "POST":

        # get the newly keyed-in values

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        # for image
        # checking if image is existing
        if len(request.FILES) != 0:
            image = request.FILES['image']

        # getting existing data
        student = Students.objects.get(id=id)

        # replacing the existing data with the new value

        student.name = name
        student.email = email
        student.phone = phone
        student.image = image

        student.save()
        messages.success(request,"Record updated Successfully")
        return redirect("/viewdata")

    student = Students.objects.get(id=id)
    return render(request, "edit.html", {'student': student})


def sliders(request):
    slides = Sliders.objects.all()
    return render(request, 'sliders.html', {'navbar': 'sliders', 'slides':slides})



#searching in django
def search(request):
    if request.method =='GET':
        # argument passed to get method should  be the same as the input field name
        query = request.GET.get('query')
        if query:
            student = Students.objects.filter(name__icontains=query)
            return render(request,'search.html',{'data':student}) # in the context the key should be the same name as the variable name used to loop while viewing the data in the database. Check for loop in html file
