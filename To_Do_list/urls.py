from django.urls import path

from To_Do_list.views import index_view, add_view, task_view

urlpatterns = [
    path('', index_view),
    path('add/', add_view),
    path('task/', task_view)
]