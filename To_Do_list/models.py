from django.db import models


# Create your models here.


class ToDoList(models.Model):
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=200, null=False, blank=False, verbose_name="Статус", default="new")
    due_date = models.DateField(null=True, blank=True, verbose_name="Дата выполнения")

    def __str__(self):
        return f"{self.pk}. {self.description} - {self.status}"

    class Meta:
        db_table = 'ToDoLists'
        verbose_name = "Список дел"
        verbose_name_plural = "Списки дел"
