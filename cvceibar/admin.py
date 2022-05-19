from django.contrib import admin
from .models import User
from .models import Cargo
from .models import Inform
# Register your models here.
admin.site.register(User)
admin.site.register(Cargo)
admin.site.register(Inform)
