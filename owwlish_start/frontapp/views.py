from django.views.generic import TemplateView
from customerapp.models import Customer

class CustomerGeneric(TemplateView):
    template_name = 'show_all_customers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['customers'] = Customer.objects.all()
        return context

class HomeGeneric(TemplateView):
    template_name = 'home.html'


