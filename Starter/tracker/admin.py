from django.contrib import admin
from tracker.models import Category
from tracker.models import Transaction
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Category)
