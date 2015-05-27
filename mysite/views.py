# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from models import *


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
