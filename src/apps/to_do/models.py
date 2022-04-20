from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class CardToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Título do card', max_length=120, blank=False, null=False)
    created_date = models.DateField('Data de Criação', auto_now_add=True, editable=False)
    modificated_date = models.DateField('Data de Criação', default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
        
    def __str__(self):
        if self.modificated_date:
            return f"{ self.user.first_name } - {self.modificated_date}"
        else:
            return f"{ self.user.first_name } - {self.created_date}"
        

class Task(models.Model):
    TODO, IN_PROGRESS, TASK_DONE = 'TTD', 'TIP', 'TD'
    
    TASK_STATUS_CHOICES = (
        (TODO, 'todo'), # Task To Do
        (IN_PROGRESS, 'in_progress'),  # Task In Progress
        (TASK_DONE, 'done'), # Task Done
    )
    
    card = models.ForeignKey(CardToDo, on_delete=models.CASCADE)
    title = models.CharField('Título da tarefa', max_length=120, blank=False, null=False)
    description = models.TextField('Descrição da tarefa', blank=True)
    status = models.CharField('Status da tarefa', max_length=3, choices=TASK_STATUS_CHOICES, default=TODO)
    created_date = models.DateField('Data de Criação', auto_now_add=True, editable=False)
    modificated_date = models.DateField('Data de Criação', default=timezone.now, editable=False)
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
    def __str__(self):
        return f"{ self.card.user.first_name } - { self.card.title } - {self.title}"