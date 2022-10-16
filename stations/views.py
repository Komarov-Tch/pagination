import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('settings.BUS_STATION_CSV', mode='r', encoding='utf-8') as f:
        table = list(csv.DictReader(f))
    page = int(request.GET.get('page', 1))
    paginator = Paginator(table, 10)
    n_page = paginator.get_page(page)
    context = {
        'bus_stations': n_page.object_list,
        'page': n_page,
    }
    return render(request, 'stations/index.html', context)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
