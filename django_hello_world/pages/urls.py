from django.urls import path

from . import views

urlpatterns = [
    # Root Path
    path('', views.index, name='index')

]