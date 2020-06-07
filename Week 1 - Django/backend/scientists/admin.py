from django.contrib import admin

from .models import Scientists, Field

# Register your models here.


class ScientistAdmin(admin.ModelAdmin):
    display_inline = ("field",)


admin.site.register(Scientists, ScientistAdmin)
admin.site.register(Field)
