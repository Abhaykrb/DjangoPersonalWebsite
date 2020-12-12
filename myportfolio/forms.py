from django.forms import ModelForm
from .models import contact

class contactForm(ModelForm):
    class Meta:
        model= contact
        fields= ["firstname", "lastname", "email", "message"] # these field names should be same as fields of model class contact and names in templates



