# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from mezzanine.pages.models import Page
from www.forms import DDLPFeedbackForm
from www.models import FrequentlyAskedQuestion

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        about_page = Page.objects.filter(slug='about-dr-doos-little-pupcakery').first()
        faq_page = Page.objects.filter(slug='frequently-asked-questions').first()
        contactus_page = Page.objects.filter(slug='contact-us').first()
        faqs = FrequentlyAskedQuestion.objects.all()
        return render(request, self.template_name, {
            'about_page': about_page,
            'faqs': faqs,
            'contactus_page': contactus_page,
            'feedbackform': DDLPFeedbackForm()
        })

    def post(self, request, *args, **kwargs):
        return render(request, 'home.html', {})


def feedbackform_processor(request):
    if request.is_ajax():
        if request.POST:
            response_data = {}
