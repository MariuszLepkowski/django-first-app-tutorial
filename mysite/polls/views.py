from django.http import Http404
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:3]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


def show_all_questions(request):
    all_questions_list = Question.objects.order_by("-pub_date")
    context = {
        "all_questions_list": all_questions_list,
    }
    return render(request, "polls/all-questions.html", context)


def about(request):
    return render(request, "polls/about.html")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice_list = question.choice_set.all()
    return render(request, "polls/detail.html", {"question": question, "choices": choice_list})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)