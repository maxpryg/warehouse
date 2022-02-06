from django import forms
from .models import Truck, Entry


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


#class EntryForm(forms.ModelForm):
#    class Meta:
#        model = Entry
#        fields = ('material_description', 'material', 'quantity', 'checked')

class TruckForm(forms.ModelForm):
    """Base form for adding new truck instances"""
    class Meta:
        model = Truck
        fields = ('cw', 'truck_number', 'arrival_date', 'specification')
        widgets = {
            'arrival_date': DateInput(),
        }


#class EntryForm(forms.ModelForm):
#    class Meta:
#        model = Entry
#        fields = ('material_description', 'material', 'quantity', 'checked')
class EntryForm(forms.Form):
    material_description = forms.CharField(max_length=20, disabled=True)
    material = forms.CharField(max_length=10, disabled=True)
    quantity = forms.IntegerField(disabled=True)
    checked = forms.BooleanField(required=False)
    quantity_received = forms.IntegerField()

