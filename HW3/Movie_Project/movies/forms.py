from django import forms
from movies.models import Movie

class MovieForm(forms.MOdelForm):
    class meta:
        model = Movie
        fields = "__all__"