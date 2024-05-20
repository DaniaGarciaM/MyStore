from django.shortcuts import render
from .models import Question, Choice
# Create your views here.
def home(request):
    return render(request,'home.html')

def get_polls(request):
    questions = Question.objects.all()
    return render(
        request, 'poll/home.html',
        {
            "questions":questions
        }
    )

def vote(request, q_id):
    q = Question.objects.get(pk=q_id)
    return render(request, 'poll/vote.html', {
        "question": q
    })
    

def result(request, q_id):
    pass