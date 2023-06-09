from django.http import HttpResponse
from django.shortcuts import redirect, render
from polls.models import Feedback

def create(request):

    feedback = Feedback()
    feedback.name = request.POST.get('name')
    feedback.email = request.POST.get('email')
    feedback.text = request.POST.get('text')
    feedback.save()

    return redirect('/')