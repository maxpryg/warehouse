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


class EntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields['material_description'].widget.attrs.update({
            'readonly': 'readonly',
            #'size':15,
            'class': 'form-control form-control-sm form-control-plaintext text-end',
        })
        self.fields['material'].widget.attrs.update({
            'readonly': 'readonly',
            #'size':8,
            'class': 'form-control form-control-sm form-control-plaintext text-end',
        })
        self.fields['quantity'].widget.attrs.update({
            'readonly': 'readonly',
            'class': 'right-align form-control form-control-sm form-control-plaintext text-end',
        })
        self.fields['quantity_received'].widget.attrs.update({
            #'size':4,
            'class': 'form-control form-control-sm text-end',
        })

    class Meta:
        model = Entry
        fields = ('material_description', 'material', 'quantity', 'checked',
            'quantity_received')
