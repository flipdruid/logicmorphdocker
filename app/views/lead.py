from django.views.generic import CreateView
from django.urls import reverse_lazy
from app.models import Lead

class LeadCreate(CreateView):
    model = Lead
    template_name = "main/contact_us.html"
    fields = "__all__"
    success_url = reverse_lazy("main")