from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from payir.models import Gateway, Transaction

from shop.models import Basket


def current_datetime(request):
    token = request.GET.get('token')
    status = request.GET.get('status')
    if status == '1' and token:
        gateway = Gateway.objects.filter(api_key='test').first()
        transaction, gateway_verification = gateway.find_and_verify(token)
        if transaction.verified == gateway_verification:
            return_status = True
            basket = transaction.order.basket
            basket.is_paid = True
            basket.save()
            Basket.objects.filter(updated_at__lt=basket.updated_at, is_paid=False).delete()
        else:
            return_status = False
    json = {'status': return_status}
    return JsonResponse(json)
