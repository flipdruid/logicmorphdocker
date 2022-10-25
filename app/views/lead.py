from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from app.models import Lead

class LeadCreate(CreateView):
    model = Lead
    template_name = "main/contact_us.html"
    fields = ("first_name", "last_name","email","entity_name", "details")
    success_url = reverse_lazy("main")

@method_decorator(login_required, name="dispatch")
class LeadList(ListView):
    model = Lead
    paginate_by = 3
    template_name = "main/leads.html"
    fields = ("first_name", "last_name","email","entity_name", "details")
    context_object_name = "leads"

@method_decorator(login_required, name="dispatch")
class LeadView(ListView):
    model = Lead
    paginate_by = 3
    template_name = "main/leads.html"
    fields = ("first_name", "last_name","email","entity_name", "details")
    context_object_name = "leads"