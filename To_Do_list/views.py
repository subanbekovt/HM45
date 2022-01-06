from django.shortcuts import render, redirect, get_object_or_404

from To_Do_list.forms import TaskForm
from To_Do_list.models import ToDoList
from To_Do_list.models import STATUS_CHOICES


# Create your views here.
def index_view(request):
    todo = ToDoList.objects.order_by("status")
    todo = ToDoList.objects.all()
    return render(request, 'index.html', {'todo': todo, 'choice': STATUS_CHOICES})


def add_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'new.html', {'form': form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            due_date = form.cleaned_data.get('due_date')
            if due_date == '':
                due_date = None
            details = form.cleaned_data.get('details')
            new_task = ToDoList.objects.create(description=description,
                                               status=status,
                                               due_date=due_date,
                                               details=details)
            return redirect('task_view', pk=new_task.pk)
        return render((request, 'add_view', {"form": form}))


def task_view(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)
    context = {"task": task}
    return render(request, "one_entry.html", context)


def del_view(request, pk):
    task = ToDoList.objects.get(pk=pk)
    task.delete()
    return redirect('index_view')


def edit_view(request, pk):
    task = ToDoList.objects.get(pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={'description': task.description,
                                 'status': task.status,
                                 'due_date': task.due_date,
                                 'details': task.details})
        return render(request, 'task_edit.html', {'task': task, 'form': form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = request.POST.get('description')
            task.status = request.POST.get('status')
            task.due_date = request.POST.get('due_date')
            if task.due_date == '':
                task.due_date = None
            task.details = request.POST.get('details')
            task.save()
            return redirect("task_view", pk=task.pk)
        return render(request, 'task_edit.html', {'task': task, 'form': form})

