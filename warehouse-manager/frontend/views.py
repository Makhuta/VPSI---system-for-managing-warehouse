from django.shortcuts import render, redirect
from django.utils.translation import activate
from database.models import *
from database.forms import *

from django.core.paginator import Paginator

def custom_render(request, template_name, context={}):
    default_context = {
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
        'user': request.user,
        'orders': list(Order.objects.all()),
        'stocks': list(Stocks.objects.all()),
        'items': list(Item.objects.all())
    })

def items(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 10)  

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    return render(request, 'items.html', {'page_obj': page_obj})

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
    return custom_render(request, 'settings.html', context)