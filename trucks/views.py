from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_list_or_404, render
from django.urls import reverse
from django.forms import modelformset_factory, formset_factory
from django.db.models import Count, Q

from .models import Truck, Entry
from .forms import TruckForm, EntryForm


class TruckListView(generic.ListView):
    model = Truck
    template_name = 'trucks/index.html'
    paginate_by = 10


def add_truck(request):
    """Process form that adds new Truck and it's specification(Entry instances)
        to database"""
    if request.method == 'POST':
        form = TruckForm(request.POST, request.FILES)

        def add_truck_id(row):
            """Initializer function that adds ForeignKey(Truck) to Entry
            before it is saved to database"""
            if row[0].startswith('Y'):
                row[0] = row[0].partition('-')[2]
            row = [new_truck] + row
            return row

        if form.is_valid():
            # add new Truck instance to database
            cw = form.cleaned_data['cw']
            truck_number = form.cleaned_data['truck_number']
            arrival_date = form.cleaned_data['arrival_date']
            new_truck = Truck(
                cw=cw, truck_number=truck_number, arrival_date=arrival_date)
            new_truck.save()

            #if file upload or reading fails, the newly created truck instance
            #must be deleted
            try:
            #save rows from uploaded file to DB as Entry instances
                specification = form.cleaned_data['specification']
                specification.isave_to_database(
                    model=Entry,
                    initializer=add_truck_id,
                    mapdict=['truck', 'material', 'material_description',
                        'quantity', 'weight', 'handling_unit'],
                )
                return HttpResponseRedirect(reverse('trucks:trucks'))
            except Exception as exc:
                new_truck.delete()
                raise exc
    else:
        form = TruckForm()
    return render(request, 'trucks/add_truck.html', {'form': form})


def truck_detail(request, pk):
    """Return a list of handling units of certain truck"""
    checked_qty = Count('handling_unit', filter=Q(checked=True))
    unchecked_qty = Entry.objects.filter(truck__id=pk).filter(
        checked=False).count()
    handling_units = Entry.objects.filter(truck__id=pk).order_by(
        'handling_unit').values_list(
        'handling_unit', flat=True).distinct()
    handling_units.annotate(checked_qty=checked_qty)
#    total_entries = Entry.objects.filter(truck__id=pk).filter(
#        handling_unit__exact=hu).count()
#    checked_entries = Entry.objects.filter(truck__id=pk).filter(
#        handling_unit__exact=hu).filter(checked=True).count()
    context = {'handling_units': handling_units, 'truck_id': pk}
    print(handling_units)
    print(type(handling_units))
    return render(
        request, 'trucks/truck-detail.html', context)


def handling_unit_detail(request, pk, hu):
    EntryFormSet = modelformset_factory(Entry, form=EntryForm, extra=0)
    queryset=Entry.objects.filter(truck__id=pk).filter(handling_unit__exact=hu)
    if request.method == 'POST':
        formset = EntryFormSet(request.POST, request.FILES, queryset=queryset)
        truck = Truck.objects.get(id=pk)
        if formset.is_valid():
            #entries contain only forms, that were changed
            entries = formset.save(commit=False)
            for entry in entries:
                #new forms added by user, will have entry.id None
                if entry.id is None:
                    entry.truck = truck
                    entry.handling_unit = hu
                entry.save()
            return HttpResponseRedirect(
                reverse('trucks:truck-detail', args=[pk]))
    else:
        formset = EntryFormSet(queryset=queryset)
    return render(request, 'trucks/handling-unit-detail.html',
        {'formset': formset})
