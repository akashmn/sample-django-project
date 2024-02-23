from django.forms import ModelForm

from .models import Movie_info

class MovieForm(ModelForm):
    class Meta:
        model = Movie_info
        fields = '__all__'