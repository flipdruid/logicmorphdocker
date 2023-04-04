from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from accounts.decorators import allowed_users
from django.core.exceptions import ObjectDoesNotExist


@method_decorator(allowed_users(allowed_roles=['admin', 'staff', 'client']),  name="dispatch")
class Index(TemplateView):
    template_name = "dashboard/index.html"
    context_object_name =   'dash_is_active'

    def get_context_data(self, **kwargs):
        context         =    super(Index, self).get_context_data(**kwargs)               
        context['dash_is_active']     =  'active'
        return context


@method_decorator(allowed_users(allowed_roles=['admin', 'staff', 'client']),  name="dispatch")
class Chart(TemplateView):
    template_name = "dashboard/chart.html"
    context_object_name =   'chart_is_active'

    def get_context_data(self, **kwargs):
        context         =    super(Chart, self).get_context_data(**kwargs)               
        context['chart_is_active']     =  'active'
        return context

@method_decorator(allowed_users(allowed_roles=['admin', 'staff', 'client']),  name="dispatch")
class AccountSettings(TemplateView):
    pass