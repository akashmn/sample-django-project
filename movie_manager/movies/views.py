from django.shortcuts import render
from . models import Movie_info


#create
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        year = request.POST['year']
        description = request.POST['summary']
        movie_obj = Movie_info(title=title, year=year, description=description)
        movie_obj.save()

    return render(request, 'create.html')



#edit
def edit(request):
    return render(request, 'edit.html')



#list
def list(request):

    movie_data = { 
    'movies': [ 
        {
            "title": "The Godfather",
            "year": "1972",
            "summary": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
            "success": True,
            'img':'camera.png',
        },

        {
            "title": "Pulp Fiction",
            "year": "1994",
            "summary": "The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
            "success": False,
            'img':'camera.png',
        },

        {
            "title": "Inception",
            "year": "2010",
            "summary": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
            "success": True,
            'img':'camera.png',
        },

        {
            "title": "The Shawshank Redemption",
            "year": "1994",
            "summary": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
            "success": False,
            'img':'camera.png',
        },

        {
            "title": "Parasite",
            "year": "2019",
            "summary": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
            "success": True,
            'img':'camera.png',
        }
    ]
}

    return render(request, 'list.html', movie_data)

# Create your views here.
