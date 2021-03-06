from django.db import models


# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class ToDoList(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=200, null=False, blank=False, verbose_name="Статус", default="new", choices=STATUS_CHOICES)
    due_date = models.DateField(null=True, blank=True, verbose_name="Дата выполнения")
    details = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Подробное описание")

    def __str__(self):
        return f"{self.pk}. {self.description} - {self.status}"

    class Meta:
        db_table = 'ToDoLists'
        verbose_name = "Список дел"
        verbose_name_plural = "Списки дел"
