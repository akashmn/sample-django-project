from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def print_hello(request):
    movie_data = { 
        'movies' :[ 
    {
        "title" : "The Godfather",
        "year" : "1972",
        "summary": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    },

    {
        "title" : "The Godfather",
        "year" : "1972",
        "summary": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    },

    {
        "title" : "The Godfather",
        "year" : "1972",
        "summary": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    },

    {
        "title" : "The Godfather",
        "year" : "1972",
        "summary": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    },

    {
        "title" : "The Godfather",
        "year" : "1972",
        "summary": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    }
    
    ]}
    return render(request, 'hello.html', movie_data)
    

# Create your views here.
