from django import forms
from movies.models import Movie

class MovieForm(forms.ModelForm):
    class meta:
        model = Movie
        fields = "__all__"