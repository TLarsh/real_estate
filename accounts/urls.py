from django.urls import path
from .views import SignInView, SignupView
from django.views.generic import TemplateView


urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('signin/', SignInView.as_view())
]