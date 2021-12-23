from django.urls import path

from To_Do_list.views import index_view, add_view, new_entry

urlpatterns = [
    path('', index_view),
    path('add/', add_view),
    path('add/new/', add_view)
]