from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.models import Lead

class LeadCreate(CreateView):
    model = Lead
    template_name = "main/contact_us_mail.html"
    fields = ("first_name", "last_name","email","entity_name", "details")
    success_url = reverse_lazy("main")

@method_decorator(login_required, name="dispatch")
class LeadMailList(ListView):
    model = Lead
    paginate_by = 3
    template_name = "main/lead_mail_lists.html"
    fields = ("first_name", "last_name","email","entity_name", "details")
    context_object_name = "leads"

@method_decorator(login_required, name="dispatch")
class LeadMailView(DetailView):
    model = Lead
    template_name       =   'main/lead_mail_view.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'lead'

@method_decorator(login_required, name="dispatch")
class LeadMailViewLead(DetailView):
    model = Lead
    template_name       =   'main/lead_mail_view_lead.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'lead'

@method_decorator(login_required, name="dispatch")
class LeadMailDelete(DeleteView):
    model = Lead        
    template_name       =   'main/lead_mail_confirm_delete.html'        
    pk_url_kwarg        =   'pk'
    success_url = reverse_lazy("main")
    context_object_name =   'lead'


@method_decorator(login_required, name="dispatch")
class LeadToClient(DetailView):
    model = Lead
    template_name       =   'main/lead_client.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'lead'

    def get_context_data(self, **kwargs):
        context         =    super(LeadToClient, self).get_context_data(**kwargs)
        currentObject    =    Lead.objects.get(id=self.kwargs['pk'])
        context['lead_mails']     =    Lead.objects.all().filter(email=currentObject.email)
        return context

