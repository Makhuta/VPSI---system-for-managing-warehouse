from django.shortcuts import render
from database.models import *

# Create your views here.
def index(request):
    orders = Order.objects.all()
    return render(request, 'index.html', {'user': request.user, 'orders': orders, 'orders_sum': sum([o.item.price for o in orders])})