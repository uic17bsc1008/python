from django.urls import path
from .import views
urlpatterns = [
    path('', views.QuizListView.as_view(), name="main-view"),
    path('<pk>/', views.quiz_view, name="quiz-view"),
]