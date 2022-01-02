from django.urls import path

from To_Do_list.views import index_view, add_view, task_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('add/', add_view, name='add_view'),
    path('task/<int:pk>/', task_view, name='task_view')
]