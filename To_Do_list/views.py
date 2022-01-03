from django.shortcuts import render, redirect, get_object_or_404

from To_Do_list.models import ToDoList
from To_Do_list.models import STATUS_CHOICES


# Create your views here.
def index_view(request):
    todo = ToDoList.objects.order_by("status")
    todo = ToDoList.objects.all()
    return render(request, 'index.html', {'todo': todo, 'choice': STATUS_CHOICES})


def add_view(request):
    if request.method == 'GET':
        return render(request, 'new.html', {'status': STATUS_CHOICES})
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        details = request.POST.get('details')
        if due_date == '':
            due_date = None
        entry = ToDoList.objects.create(description=description, status=status, due_date=due_date, details=details)
        return redirect('task_view', pk=entry.pk)


def task_view(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)
    context = {"task": task}
    return render(request, "one_entry.html", context)


def del_view(request, pk):
    task = ToDoList.objects.get(pk=pk)
    task.delete()
    return redirect('index_view')

