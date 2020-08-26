from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Genre
from .forms import ContactForm
from django import forms


# Create your views here.

def home(request):
    return render(request, 'index.html', { "title" : "Welcome"})

def catalog_ssr(request):
    all_movies = Movie.objects.all() # read the movie table to a list
    return render(request, 'catalog_ssr.html', { "title" : "Catalog SSR", "movies": all_movies})

def details(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'details.html', {"title": "Movie details", "movie": movie})

def about(request):
    return render(request, 'about.html', { "title" : "About me"})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            # you can change/add data to post before saving it
            # message.created = timezone.now()
            message.save()
            return redirect('home')
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {'form': form})

def catalog_csr(request):
    return render(request, 'catalog_csr.html', { "title": "Catalog CSR" })
