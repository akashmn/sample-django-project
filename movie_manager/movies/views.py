#create your views here

from django.shortcuts import render
from . models import Movie_info

#import the forms from the forms.py file
from .forms import MovieForm



#create

def create(request):

    frm = MovieForm()

    if request.method == 'POST':
        title = request.POST['title']
        year = request.POST['year']
        description = request.POST['description']
        movie_obj = Movie_info(title=title, year=year, description=description)
        movie_obj.save()

    return render(request, 'create.html',{'frm':frm})



#edit
def edit(request):
    return render(request, 'edit.html')



#list
def list(request):
    movie_set = Movie_info.objects.all()  #fetching all the data from the database
    print(movie_set)
    return render(request, 'list.html', {'movies' : movie_set})

# Create your views here.
