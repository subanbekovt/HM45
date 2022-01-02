from django.shortcuts import render

from To_Do_list.models import ToDoList
from To_Do_list.models import STATUS_CHOICES


# Create your views here.
def index_view(request):
    todo = ToDoList.objects.order_by("status")
    return render(request, 'index.html', {'todo': todo})


def add_view(request):
    if request.method == 'GET':
        return render(request, 'new.html', {'status': STATUS_CHOICES})
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        if due_date == '':
            due_date = None
        entry = ToDoList.objects.create(description=description, status=status, due_date=due_date)
        context = {
            "entry": entry
        }
        return render(request, "one_entry.html", context)


def task_view(request, pk):
    task = ToDoList.objects.get(pk=pk)
    context = {"task": task}
    return render(request, "one_entry.html", context)
