from django import forms
from django.forms import widgets
from To_Do_list.models import STATUS_CHOICES


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label="Название")
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    due_date = forms.DateField(required=False, label="Время выполнения")
    details = forms.CharField(max_length=200, required=False, label="Описание",
                              widget=widgets.Textarea(attrs={"rows": 5, "cols": 50}))
