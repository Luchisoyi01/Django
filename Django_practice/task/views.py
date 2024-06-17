from django.shortcuts import render

# Create your views here.
tasks = ["playing", "baking","cooking"]
def index(request):
  return render(request, "task/index.html", {
    "tasks": tasks
  })
  
def add(request):
  return render(request, "task/add.html",)
