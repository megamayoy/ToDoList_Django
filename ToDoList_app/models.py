from django.db import models

# Create your models here.


class ToDoList(models.Model):

    item_content = models.CharField(max_length=264)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.item_content + '( ' + str(self.completed) + ')'