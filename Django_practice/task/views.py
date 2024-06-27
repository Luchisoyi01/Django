from django.shortcuts import render
from django import forms

# Create your views here.
tasks = ["playing", "baking","cooking", "watching"]



def index(request):
  return render(request, "task/index.html", {
    "tasks": tasks
  })
  
def add(request):
  return render(request, "task/add.html",)
