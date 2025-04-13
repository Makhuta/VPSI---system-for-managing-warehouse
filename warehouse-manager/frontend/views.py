from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.utils.translation import activate
from collections import defaultdict
from django.conf import settings
from database.models import UserConfig
from database.models import *
from database.forms import *

from django.core.paginator import Paginator

def custom_render(request, template_name, context={}):
    default_context = {
        'user': request.user,
        'user_role': request.user.groups.all().first(),
    }

    if request.user.is_authenticated:
        default_context["user_config"], created = UserConfig.objects.get_or_create(user=request.user)
    else:
        default_context["user_config"] = UserConfig(user=None)

    context.update(default_context)
    activate(context["user_config"].language)
    request.LANGUAGE_CODE = context["user_config"].language
    return render(request, template_name, context)

# Create your views here.
def index(request):
    return custom_render(request, 'index.html', {
        'orders': list(Order.objects.all()),
        'stocks': list(Stocks.objects.all()),
        'stocks_history': list(StocksHistory.objects.all()),
        'items': list(Item.objects.all())
    })

def items(request):
    item_list = list(Item.objects.all())
    stocks = Stocks.objects.select_related('warehouse').all()

    item_warehouse_map = defaultdict(list)
    for stock in stocks:
        item_warehouse_map[stock.item_id].append(stock.warehouse)

    for item in item_list:
        item.warehouses = item_warehouse_map.get(item.id, [])

    paginator = Paginator(item_list, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return custom_render(request, 'items.html', {'page_obj': page_obj})

def orders(request):
    orterz = list(Order.objects.all())

    paginator = Paginator(orterz, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return custom_render(request, 'orders.html', {"page_obj": page_obj})

def suppliers(request):
    subblierz = list(Supplier.objects.all())

    paginator = Paginator(subblierz, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return custom_render(request, 'suppliers.html', {"page_obj": page_obj})


@login_required
def page_settings(request):
    context = {}
    if request.user.is_authenticated:
        # Get or create the user-specific UserConfig
        user_config, created = UserConfig.objects.get_or_create(user=request.user)

        # Handle form submission for POST requests
        if request.method == 'POST':
            form = UserConfigForm(request.POST, instance=user_config)
            if form.is_valid():
                form.save()
                return redirect('settings')  # Redirect to avoid resubmission on refresh
        else:
            form = UserConfigForm(instance=user_config)

        # Add the form to the context
        context["form"] = form
        context["currencies"] = UserConfig.CURRENCY
        context["languages"] = settings.LANGUAGES
        context["current_language"] = user_config.language  
        context["current_currency"] = user_config.currency
        context["roles"] = Group.objects.all()
        
    return custom_render(request, 'settings.html', context)

@login_required
def new_item(request):
    if request.method == 'POST':
        pass
    return render(request, 'new_item.html')

@login_required
def new_order(request):
    if request.method == 'POST':
        pass
    return render(request, 'new_order.html')

@login_required
def new_supplier(request):
    if request.method == 'POST':
        pass
    return render(request, 'new_supplier.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        if user_id:
            current_password = request.POST.get("current_password")
            new_password = request.POST.get("new_password")
            new_password_again = request.POST.get("new_password_again")
            if current_password and new_password and new_password_again:
                user_obj = User.objects.get(pk=user_id)
                user = authenticate(username=user_obj.username, password=current_password)
                if user is not None:
                    if new_password == new_password_again:
                        user.set_password(new_password)
                        user.save()
                        return redirect("login")

    return redirect("settings")