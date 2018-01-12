from django.urls import path
from . import views

urlpatterns = [
    path('password-specs/',
         views.PasswordSpecsView.as_view(),
         name='password-specs'),
]
