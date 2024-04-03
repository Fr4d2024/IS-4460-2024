from django.shortcuts import render, redirect
from django.views import View
from .models import Movie
from django.urls import reverse
from .forms import MovieForm
from rest_framework import generics
from .serializers import MovieSerializer


# Create your views here.
class MovieList(View):
    def get(self,request):
        movies = Movie.objects.all()
        return render(request = request,template_name = 'movie_list.html',context = {'movies': movies})

# Lab-7 like views  
class MovieEdit(View):

    def get(self,request,movie_id):

        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(instance=movie)

        return render(request = request,template_name = 'movie_update.html',context = {'movie':movie,'form':form})
    
    def post(self,request,movie_id):

        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(request.POST,instance=movie)
        return render(request = request,template_name = 'movie_update.html',context = {'movie':movie,'form':form})
    
class MovieDelete(View):

    def get(self,request,movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

      


        form = MovieForm(instance=movie)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'movie_delete.html',context = {'movie':movie,'form':form})
      
    
    def post(self,request,movie_id=None):

        movie = Movie.objects.get(pk=movie_id)

        form = MovieForm(request.POST,instance=movie)

        Movie.delete()

        return redirect(reverse("movies-list"))

#API type views
class MovieListCreateView(generics.ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer