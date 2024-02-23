#create your views here

from django.shortcuts import render
from . models import Movie_info

#import the forms from the forms.py file
from .forms import MovieForm



#create

def create(request):
    frm = MovieForm(request.POST)
    if request.method == 'POST':
        if frm.is_valid():
            frm.save()
        else:
            frm = MovieForm()      

    return render(request, 'create.html',{'frm':frm})



#edit
def edit(request, pk):
    instance_to_be_edited = Movie_info.objects.get(pk=pk)
    frm = MovieForm(request.POST, instance_to_be_edited)
    if request.method == 'POST':
        # ALTERNATIVE WAY 
        # if frm.is_valid():
        #     instance_to_be_edited.save()
    
        
       title  = request.POST.get('title') #fetching data from the form after the edit
       year = request.POST.get('year')
       description = request.POST.get('description')
       instance_to_be_edited.title = title
       instance_to_be_edited.year = year
       instance_to_be_edited.description = description
       instance_to_be_edited.save()
        
    else:
        frm = MovieForm(instance = instance_to_be_edited) #passing the instance to the form to be edited with the instance(existing) data 

    return render(request, 'create.html',{'frm':frm})



#delete
def delete(request, pk):
    instance = Movie_info.objects.get(id=pk)
    instance.delete() #deleting the instance (current data)
    movie_set = Movie_info.objects.all()  #fetching all the data from the database
    print(movie_set)
    return render(request, 'list.html', {'movies' : movie_set})



#list
def list(request):
    movie_set = Movie_info.objects.all()  #fetching all the data from the database
    print(movie_set)
    return render(request, 'list.html', {'movies' : movie_set})

# Create your views here.
