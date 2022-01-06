from django import forms
from django.forms import widgets

class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label="Название")
    status = forms.CharField(max_length=200, required=True, label="Статус")
    due_date = forms.DateField(required=False, label="Время выполнения")
    details = forms.CharField(max_length=200, required=False, label="Описание", widget=widgets.Textarea(attrs={"rows": 5, "cols": 50}))
