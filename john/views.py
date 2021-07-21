from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Home, Results, Streamers, About, Profile, Category, Skills, Portfolio, Tourn
from django.urls import reverse
from django.views.generic import DetailView

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Tournaments
    
    tourn = Tourn.objects.order_by('-host')
    

    results = Results.objects.all()
    # Skills
    categories = Category.objects.order_by('-updated')

    # Portfolio
    portfolios = Portfolio.objects.order_by('-updated')
    # Streamers
    streamers = Streamers.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'streamers': streamers,
        'tourn': tourn,
        'results': results
    }
    


    return render(request, 'index.html', context)


