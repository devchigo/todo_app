from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView  # for class based view


# Create your views here.
from base.models import Task


class TaskList(ListView):
    model = Task
