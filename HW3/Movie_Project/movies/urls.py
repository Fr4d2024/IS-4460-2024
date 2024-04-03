from django.urls import path
from . import views
from .views import MovieListCreateView, MovieDetailView

urlpatterns = [
    path('list/', views.MovieList.as_view(), name='movie-list'),
    path('edit/<int:movie_id>/', views.MovieEdit.as_view(), name='movie-edit'),
    path('delete/<int:movie_id>/', views.MovieDelete.as_view(), name='movie-delete'),

    path('api/movies/', MovieListCreateView.as_view(), name='movie-api-list-create'),
    path('api/movies/<int:pk>/', MovieDetailView.as_view(), name='movie-api-detail'),
]