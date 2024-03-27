from django.shortcuts import render, redirect
from django.views import View
from .models import Movie
from django.urls import reverse
from .forms import MovieForm


# Create your views here.
class MovieList(View):
    def get(self,request):
        movies = Movie.objects.all()
        return render(request = request,template_name = 'movies/movie_list.html',context = {'movies': movies})
    
class MovieEdit(View):

    def get(self,request,customer_id):

        customer = Movie.objects.get(pk=customer_id)
        form = MovieForm(instance=customer)

        return render(request = request,template_name = 'customer_app/customer_edit.html',context = {'customer':customer,'form':form})
    
    def post(self,request,customer_id):

        customer = Movie.objects.get(pk=customer_id)
        form = MovieForm(request.POST,instance=customer)
        return render(request = request,template_name = 'customer_app/customer_edit.html',context = {'customer':customer,'form':form})