import os
from datetime import datetime
import requests
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from loguru import logger

from eazylab.settings import BASE_DIR
from ordering.forms import OrderingForm
from ordering.models import Order, StatusOrder


# Create your views here.


@login_required(login_url='login')
@logger.catch
def ordering_form(request: WSGIRequest) -> HttpResponse:
    context = {
        'title': 'Замовлення',
        'status': False
    }

    if request.method == 'POST':
        form = OrderingForm(request.POST, request.FILES)
        logger.info(f'Sing Up Form: {form.is_valid()}')
        logger.info(f'{form.data}')
        logger.info(f'FILES request: {request.FILES}')
        logger.info(f'FILES form: {form.files}')
        if form.is_valid():
            if request.FILES:
                order = Order(
                    user=request.user,
                    type_work=form.cleaned_data['type_work'],
                    subject=form.cleaned_data['subject'],
                    name_work=form.cleaned_data['name_work'],
                    deadline=form.cleaned_data['deadline'],
                    description=form.cleaned_data['description_work'],
                    status_order_id=StatusOrder.objects.get(status='В обробці'),
                    file_order=request.FILES['file_order'],
                    cost_work=form.cleaned_data['cost_work'],
                )
                order.save()

                message_bot = f'<b>Нове замовлення № {order.id}</b>.\n\n' \
                              f'Статус замовлення: {order.status_order_id}.\n' \
                              f'Користувач: {order.user}.\n' \
                              f'Дата створення: {order.date_created.strftime("%d.%m.%Y %H:%M")}.\n\n' \
                              f'Тип роботи: {order.type_work}.\n' \
                              f'Предмет: {order.subject}.\n' \
                              f'Назва роботи: {order.name_work}.\n' \
                              f'Термін виконання: {order.deadline}.\n' \
                              f'Вартість роботи: {order.cost_work}.\n' \
                              f'Опис роботи: {order.description}.\n'
                files = {
                    'chat_id': (None, -1001703899156),
                    'photo': open(f'{order.file_order.path}', 'rb'),
                    'caption': (None, message_bot),
                    'parse_mode': (None, 'HTML'),
                }

                response = requests.post(
                    f'https://api.telegram.org/bot{os.getenv("TOKEN_BOT")}/sendPhoto',
                    files=files
                )
                logger.info(f'Response Telegram: {response.json()}')

                message_site = f'Ваше замовлення прийнято. Номер замовлення: {order.id}'
                return render(request, 'index/index.html', {'title': 'EazyLab', 'user': request.user,
                                                            'status': True, 'message': message_site})
            else:
                order = Order(
                    user=request.user,
                    type_work=form.cleaned_data['type_work'],
                    subject=form.cleaned_data['subject'],
                    name_work=form.cleaned_data['name_work'],
                    deadline=form.cleaned_data['deadline'],
                    description=form.cleaned_data['description_work'],
                    status_order_id=StatusOrder.objects.get(status='В обробці'),
                    cost_work=form.cleaned_data['cost_work'],
                )
                order.save()

                message_bot = f'Нове замовлення № {order.id}.\n\n' \
                              f'Статус замовлення: {order.status_order_id}.\n' \
                              f'Користувач: {order.user}.\n' \
                              f'Дата створення: {order.date_created.strftime("%d.%m.%Y %H:%M")}.\n\n' \
                              f'Тип роботи: {order.type_work}.\n' \
                              f'Предмет: {order.subject}.\n' \
                              f'Назва роботи: {order.name_work}.\n' \
                              f'Термін виконання: {order.deadline}.\n' \
                              f'Вартість роботи: {order.cost_work}.\n' \
                              f'Опис роботи: {order.description}.\n' \

                files = {
                    'chat_id': (None, -1001703899156),
                    'text': (None, message_bot),
                }

                response = requests.post(
                    f'https://api.telegram.org/bot{os.getenv("TOKEN_BOT")}/sendMessage',
                    files=files
                )
                logger.info(f'Response Telegram: {response.json()}')

                message_site = f'Ваше замовлення прийнято. Номер замовлення: {order.id}'
                return render(request, 'index/index.html', {'title': 'EazyLab', 'user': request.user,
                                                            'status': True, 'message': message_site})
        else:
            context['status'] = True
            context['message'] = 'Сталася помилка при обробці замовлення'

    return render(request, 'ordering/order.html', context)
