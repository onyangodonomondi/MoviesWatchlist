from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'movies/index.html')
def movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': movies})
def movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/movie.html', {'movie': movie})
def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/edit.html', {'movie': movie})
def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    messages.success(request, 'Movie deleted successfully')
    return redirect('movies')
def add(request):  
    return render(request, 'movies/add.html') 
def save(request):
    title = request.POST['title']
    description = request.POST['description']
    year = request.POST['year']
    rating = request.POST['rating']
    movie = Movie(title=title, description=description, year=year, rating=rating)
    movie.save()
    messages.success(request, 'Movie added successfully')
    return redirect('movies')
def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.title = request.POST['title']
    movie.description = request.POST['description']
    movie.year = request.POST['year']
    movie.rating = request.POST['rating']
    movie.save()
    messages.success(request, 'Movie updated successfully')
    return redirect('movies')
    