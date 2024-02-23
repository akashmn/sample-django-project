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
    return render(request, 'edit.html')


#delete
def delete(request, pk):
    instance = Movie_info.objects.get(id=pk)
    instance.delete()
    movie_set = Movie_info.objects.all()  #fetching all the data from the database
    print(movie_set)
    return render(request, 'list.html', {'movies' : movie_set})



#list
def list(request):
    movie_set = Movie_info.objects.all()  #fetching all the data from the database
    print(movie_set)
    return render(request, 'list.html', {'movies' : movie_set})

# Create your views here.
