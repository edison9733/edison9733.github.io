from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.

homework = ["a"]

class NewHomeworkForm(forms.Form):
    homework = forms.CharField(label="Homework")
    prioty = forms.IntegerField(label="Priority", min_value=1, max_value=10)



def index(request):
    
    if "homeworkapp" not in request.session:
        request.session["homeworkapp"] = []

    return render(request, "homeworkapp/index.html", {
        "homeworkapp": request.session["homeworkapp"],
    })


def add(request):

    if request.method == "POST":
        form = NewHomeworkForm(request.POST)
        if form.is_valid():
            homework = form.cleaned_data["homework"]
            request.session["homeworkapp"] += [homework]
            return HttpResponseRedirect(reverse("homeworkapp:index"))
        else:
                return render(request, "homeworkapp/add.html", {
                    "form": form,
            })
    return render(request, "homeworkapp/add.html", {
        "form": NewHomeworkForm()
    })

     