from django import forms
from .models import Truck


class DateInput(forms.DateInput):
    """Change input type attribute of date field."""
    input_type = 'date'


class TruckForm(forms.ModelForm):
    """Base form for adding new truck instances"""
    class Meta:
        model = Truck
        fields = ('cw', 'truck_number', 'arrival_date', 'specification')
        widgets = {
            'arrival_date': DateInput(),
        }
