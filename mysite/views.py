# -*- coding: utf-8 -*-
from models import *
from django.shortcuts import redirect
from django.views.generic.base import TemplateView, View
from django.db import models


class MasterAdd(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        lastName_value = self.request.POST['lastName']
        firstName_value = self.request.POST['firstName']
        middleName_value = self.request.POST['middleName']
        sex_value = self.request.POST['sex']
        Masters.objects.create(lastName=lastName_value,
                               firstName=firstName_value,
                               middleName=middleName_value,
                               sex=sex_value)
        return redirect('/')


class MasterDelete(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        delete_name = self.request.POST['name_delete']
        Masters.objects.filter(id=int(delete_name)).delete()
        return redirect('/')


class ServiceAdd(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        name_value = self.request.POST['name']
        price_value = self.request.POST['price']
        description_value = self.request.POST['description']
        Services.objects.create(name=name_value,
                               price=price_value,
                               description=description_value)
        return redirect('/')


class ServiceDelete(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        delete_name = self.request.POST['deleteService']
        Services.objects.filter(id=int(delete_name)).delete()
        return redirect('/')


class ServicesOfMastersAdd(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        master_value = self.request.POST['master']
        service_value = self.request.POST['service']
        ServicesOfMasters.objects.create(
            master=Masters.objects.filter(id=int(master_value))[0],
            service = Services.objects.filter(id=int(service_value))[0]
        )
        return redirect('/')


class ServicesOfMastersDelete(View):

    def post(self, *args, **kwargs):
        usluga_delete = self.request.POST['deleteSom']
        ServicesOfMasters.objects.filter(id=int(usluga_delete)).delete()
        return redirect('/')


class BookingAdd(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
            master_value = self.request.POST['master']
            service_value = self.request.POST['service']
            date_value = self.request.POST['date']
            time_value = self.request.POST['time']
            Booking.objects.create(
                master=Masters.objects.get(id=int(master_value)),
                service=Services.objects.get(id=int(service_value)),
                date=date_value,
                time=time_value
            )

            return redirect('/')


class BookingDelete(View):
    def post(self, *args, **kwargs):
        delete_name = self.request.POST['deleteBo']
        Booking.objects.filter(id=int(delete_name)).delete()
        return redirect('/')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        service_list = Services.objects.all()
        masters = Masters.objects.all()
        services_of_masters = ServicesOfMasters.objects.all()
        booking = Booking.objects.all()
        context.update(
            {
                'service_list': service_list,
                'masters': masters,
                'ServicesOFMasters': services_of_masters,
                'Booking': booking
            }
        )
        return context

