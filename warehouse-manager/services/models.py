from django.db import models
from enum import Enum
import json
from .services_functions import check_stock_level, send_stock_history, simulate_customer
from django.forms.models import model_to_dict

class ServiceFunction(Enum):
    CHECK_STOCK = ("check_stock", "Check Stock Levels", check_stock_level.run)
    SEND_EMAIL = ("send_email", "Send Stock History Email", send_stock_history.run)
    SIMULATE_CUSTOMER = ("simulate_customer", "Simulate customer interaction", simulate_customer.run)

    @classmethod
    def choices(cls):
        return [(tag.value[0], tag.value[1]) for tag in cls]  # Returns (id, name)

    @classmethod
    def get_function(cls, function_id):
        for func in cls:
            if func.value[0] == function_id:
                return func.value[2]  # Return function reference
        return None  # If function_id is not found

    @classmethod
    def get_name(cls, function_id):
        for func in cls:
            if func.value[0] == function_id:
                return func.value[1]  # Return the function (second item in tuple)
        return None

class ServiceConfig(models.Model):
    name = models.CharField(max_length=255, unique=True)
    schedule = models.CharField(max_length=100)  # CRON expression
    arguments = models.JSONField(default=dict, blank=True)  # JSON field for function arguments
    last_run = models.DateTimeField(null=True, blank=True)
    function = models.CharField(max_length=50, choices=ServiceFunction.choices())
    enabled = models.BooleanField(default=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial = self._dict

    @property
    def diff(self):
        d1 = self.__initial
        d2 = self._dict
        diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
        return dict(diffs)

    @property
    def has_changed(self):
        return bool(self.diff)

    @property
    def changed_fields(self):
        return self.diff.keys()

    def get_field_diff(self, field_name):
        """
        Returns a diff for field if it's changed and None otherwise.
        """
        return self.diff.get(field_name, None)

    def save(self, *args, **kwargs):
        """
        Saves model and set initial state.
        """
        if self.id is not None and 'update_fields' not in kwargs:
            kwargs.update({'update_fields': self.changed_fields})

        super().save(*args, **kwargs)
        self.__initial = self._dict

    @property
    def _dict(self):
        return model_to_dict(self, fields=[
            field.name
            for field in self._meta.get_fields()
        ])

    def get_arguments(self):
        """Return parsed arguments as a dictionary."""
        return self.arguments if isinstance(self.arguments, dict) else json.loads(self.arguments)

    def get_function_reference(self):
        """Return the actual function from the enum."""
        return ServiceFunction.get_function(self.function)
    
    def __str__(self):
        return f"{self.name} ({ServiceFunction.get_name(self.function)})"