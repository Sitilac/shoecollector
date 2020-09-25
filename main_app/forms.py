from django.forms import ModelForm
from .models import *

class CleaningForm(ModelForm):
  class Meta:
    model = Cleaning
    fields = ['date', 'shoe_clean']