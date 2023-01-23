import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    new_bd = []
    page_number = int(request.GET.get('page', 1))
    with open('data-398-2018-08-30.csv', encoding='utf8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            temp = {}
            temp['Name'] = row['Name']
            temp['Street'] = row['Street']
            temp['District'] = row['District']
            new_bd.append(temp)
    pagination = Paginator(new_bd, 10)
    page = pagination.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
