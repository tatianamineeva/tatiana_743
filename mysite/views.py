# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from models import Masters

Masters.objects.filter().delete()
m1 = Masters.objects.create(id = 1, firstName='Евгений', lastName='Рассказов', middleName='Владимирович', sex='мужской')
m2 = Masters.objects.create(id = 2, firstName='Татьяна', lastName='Минеева', middleName='Евгеньевна', sex='женский')


from models import Services

Services.objects.filter().delete()
s1 = Services.objects.create(id = 1, name = 'Стрижка', price = 500.50, description = 'Модельная')
s2 = Services.objects.create(id = 2, name = 'Маникюр', price = 700, description = 'Аппаратный')

from models import ServicesOfMasters

ServicesOfMasters.objects.filter().delete()
sm1 = ServicesOfMasters
sm1.master = m1.id
sm1.service = s1.id

sm2 = ServicesOfMasters()
sm2.master = m1.id
sm2.service = s2.id

sm3 = ServicesOfMasters()
sm3.master = m2.id
sm3.service = s1.id

from models import Booking

Booking.objects.filter().delete()
b = Booking
b.service = s1.id
b.id = 1
b.master = m1.id
b.date = '25 мая 2015'
b.time = '15-00'

b1 = Booking()
b1.service = s1.id
b1.id = 1
b1.master = m1.id
b1.date = '25 мая 2015'
b1.time = '15-00'

b2 = Booking()
b2.service = s2.id
b2.id = 2
b2.master = m2.id
b2.date = '25 мая 2015'
b2.time = '17-45'

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'service_list':
                [
                    s1, s2,
                    {
                        'id':'',
                        'name':'',
                        'price':'',
                        'description': ''
                    }
                ],

                'masters':
                    [
                        m1, m2,
                        {
                                'id':'',
                                'firstName':'',
                                'lastName':'',
                                'middleName':'',
                                'sex':''
                        }
                    ],

                'ServicesOFMasters':
                [
                         sm1, sm2, sm3,
                         {

                         }
                ],

                'Booking':
                [
                    b1,b2,
                    {

                        'service':'',
                        'master':'',
                        'date':'',
                        'time':''
                    }
                ]
            }
        )
        return context
