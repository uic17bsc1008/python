from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
# Create your views here.

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/quize_view.html'

def quiz_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {'quiz':quiz}
    return render(request,'quizes/quiz.html',context)