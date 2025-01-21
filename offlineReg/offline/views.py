from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration, Event
from django.shortcuts import render
from .models import Category, Event
import json

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Event, Registration
from .forms import RegistrationForm
import json

def register(request):
    categories = Category.objects.all()
    events = Event.objects.all()
    events_json = {
        category.id: [{"id": event.id, "name": event.name} for event in category.events.all()]
        for category in categories
    }

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the form instance
            registration = form.save(commit=False)
            # Ensure the event selected is valid (you can validate further if needed)
            registration.event = Event.objects.get(name=form.cleaned_data["event"])
            registration.save()
            # Display a success message
            messages.success(request, "Registration successful!")
            return redirect("register")  # Redirect to the same page or another page
        else:
            messages.error(request, "Please correct the errors in the form.")

    context = {
        "categories": categories,
        "events_json": json.dumps(events_json),
        "form": RegistrationForm(),
    }
    return render(request, "register.html", context)



def daily_registrations(request, date):
    registrations = Registration.objects.filter(registered_on=date)
    return render(request, 'daily_registrations.html', {'registrations': registrations})

from django.shortcuts import render
from .models import Registration
from datetime import datetime

def registration_list(request):
    # Get the date from the query parameters (from the form)
    search_date = request.GET.get('search_date')
    # Retrieve all registrations by default
    registrations = Registration.objects.all()

    if search_date:
        try:
            # Convert the input date string to a Python date object
            date_object = datetime.strptime(search_date, '%Y-%m-%d').date()
            # Filter registrations to include only those with the matching date
            registrations = registrations.filter(registered_on=date_object)
        except ValueError:
            # Handle invalid date formats gracefully
            pass

    context = {
        'registrations': registrations,
        'search_date': search_date,  # Pass the search date back to the template
    }
    return render(request, 'registrations.html', context)


import openpyxl
from django.http import HttpResponse
from .models import Registration

def export_to_excel(request, date):
    registrations = Registration.objects.filter(registered_on=date)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = f"Registrations {date}"

    # Header row
    headers = ['Name', 'Roll Number', 'Year', 'Branch', 'Section', 'Email', 'Mobile Number', 'Event']
    sheet.append(headers)

    # Data rows
    for reg in registrations:
        sheet.append([
            reg.name, reg.roll_number, reg.year, reg.branch, reg.section,
            reg.email, reg.mobile_number, reg.event.name
        ])

    # Response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="Registrations_{date}.xlsx"'
    workbook.save(response)
    return response
