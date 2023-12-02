from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/about/
    path("about/", views.about, name="about"),
    # ex: /polls/all-questions/
    path("all-questions/", views.show_all_questions, name="show_all_questions"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]