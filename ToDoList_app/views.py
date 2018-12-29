from django.shortcuts import render,redirect
from django.http import HttpResponse
from ToDoList_app import forms
from ToDoList_app import models
from django.contrib import messages


# Create your views here.
def home_view(request):

    list_items = models.ToDoList.objects.all()

    if request.method == "POST":

        addItem_from_obj = forms.AddOrEditItemForm(request.POST)

        if addItem_from_obj.is_valid():
            print("form is valid")
            addItem_from_obj.save()
            messages.success(request," New Item Added")
            return redirect('ToDoList_app:home_page')


    return render(request, 'ToDoList_app/home.html', { "list_items": list_items })



def delete_item(request, list_item_id):

    list_item = models.ToDoList.objects.get(pk = list_item_id)
    list_item.delete()
    messages.success(request,"Item Deleted ")
    return redirect('ToDoList_app:home_page')

def crossoff_item(request,list_item_id):

    list_item = models.ToDoList.objects.get(pk = list_item_id)
    list_item.completed = True
    list_item.save()
    return redirect('ToDoList_app:home_page')

def uncross_item(request,list_item_id):

    list_item = models.ToDoList.objects.get(pk = list_item_id)
    list_item.completed = False
    list_item.save()
    return redirect('ToDoList_app:home_page')




def edit_item(request,list_item_id):


    list_item = models.ToDoList.objects.get(pk=list_item_id)
    item_content = list_item.item_content

    if request.method == 'POST':

        edit_form = forms.AddOrEditItemForm(request.POST, instance = list_item)

        if edit_form.is_valid():

            edit_form.save()
            messages.success(request,"Item Edited")
            return redirect("ToDoList_app:home_page")

    else:
        edit_form = forms.AddOrEditItemForm( instance=list_item )

    return render(request, "ToDoList_app/edit_item.html", {"edit_form": edit_form} )
