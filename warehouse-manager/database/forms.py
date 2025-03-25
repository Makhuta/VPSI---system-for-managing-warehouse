from django import forms
from django.utils.translation import gettext_lazy as _
from .models import UserConfig

class UserConfigForm(forms.ModelForm):
    class Meta:
        model = UserConfig
        fields = ['language', 'currency']
        labels = {
            'language': _('database.forms.userconfig.language'),
            'currency': _('database.forms.userconfig.currency'),
        }
        help_texts = {
            'language': _('database.forms.userconfig.language_help_text'),
            'currency': _('database.forms.userconfig.currency_help_text'),
        }
