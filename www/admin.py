from django.contrib import admin
from www.forms import FAQForm
from www.models import FrequentlyAskedQuestion
# Register your models here.


class FAQAdmin(admin.ModelAdmin):
    form = FAQForm
    list_display = ('question',)


admin.site.register(FrequentlyAskedQuestion, FAQAdmin)