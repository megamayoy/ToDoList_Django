from ToDoList_app.models import ToDoList
from django import forms
from django.core import validators


class AddOrEditItemForm(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = ['item_content']




