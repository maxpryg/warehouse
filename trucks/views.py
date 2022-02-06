from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_list_or_404, render
from django.urls import reverse
from django.forms import modelformset_factory

from .models import Truck, Entry
from .forms import TruckForm, EntryForm


def results(request, truck_id):
    response = "You're looking at the results of truck %s."
    return HttpResponse(response % truck_id)


def vote(request, truck_id):
    return HttpResponse("You're voting on truck %s." % truck_id)


class TruckListView(generic.ListView):
    model = Truck
    template_name = 'trucks/index.html'
    paginate_by = 10


def add_truck(request):
    """Process form that adds new Truck and it's specification(Entry instances)
        to database"""
    """
        TODO
        Add try-except statement for catching errors while uploading a file
        and saveing rows of that file to database.
        If error, newly created truck must be deleted from database.
    """
    if request.method == 'POST':
        form = TruckForm(request.POST, request.FILES)

        def add_truck_id(row):
            """Initializer function that adds ForeignKey(Truck) to Entry
            before it is saved to database"""
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
    handling_units = Entry.objects.filter(truck__id=pk).values(
        'handling_unit').distinct()

    handling_unit_list = []
    for hu in handling_units:
        handling_unit_list.append(hu['handling_unit'])

    context = {'handling_unit_list': handling_unit_list, 'truck_id': pk}
    return render(
        request, 'trucks/truck-detail.html', context)


#def handling_unit_detail(request, pk, hu):
#    """Return list of entries of certain handling unit"""
#    entries = Entry.objects.filter(
#        truck__id=pk).filter(handling_unit__exact=hu)
#    context = {'entries': entries}
#    return render(request, 'trucks/handling-unit-detail.html', context)



def handling_unit_detail(request, pk, hu):
    EntryFormSet = modelformset_factory(Entry, fields=(
        'material_description', 'material', 'quantity',
            'quantity_received', 'checked'))
    queryset = Entry.objects.filter(
        truck__id=pk).filter(handling_unit__exact=hu)
    if request.method == 'POST':
        formset = EntryFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            pass
    else:
        formset = EntryFormSet(queryset=queryset)
    return render(request, 'trucks/handling-unit-detail.html',
        {'formset': formset})
