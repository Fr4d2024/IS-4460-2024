# QUERY FOR MOVIE statements
# (Query for ALL) --> movie = Movie.objects.all()....then --> movie.count()
# (Query for FILTER) --> filtered_movie = Movie.objects.filter(title__startswith='Shrek')....then --> filtered.movie.count()
# (Query for GET) --> specific_movie = Movie.objects.get(title='Pure Fight') ... then --> specific_movie.title
# (Query for UPDATE) --> movie_update = Movie.objects.get(pk=2) ... then --> movie_update.release_year = "2023" ... then --> movie_update.save()
# (Query for DELETE) -->  movie_update.delete()