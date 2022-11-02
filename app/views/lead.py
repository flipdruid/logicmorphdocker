
import profile
from queue import Empty
from app.models.project import Project
import celery
import email
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from accounts.models.user import User
from app.models.profile import Profile
from app.models.lead import Lead
from app.models.reglink import Reglink
from accounts.forms import UserForm
from app.models.client import Client

class LeadCreate(CreateView):
    model = Lead
    template_name = "main/contact_us_mail.html"
    fields = ("first_name", "last_name","email","entity_name", "details")
    success_url = reverse_lazy("main")

@method_decorator(login_required, name="dispatch")
# @method_decorator(permission_required, name='user.is_staff')
class LeadMailList(ListView):
    model = Lead
    paginate_by = 9
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


# @method_decorator(login_required, name="dispatch")
@login_required(login_url= '/accounts/login')
def createreglink(request, lead_id):

    try:
        currentLead =   Lead.objects.get(id=lead_id)
        emailExist = Reglink.objects.get(lead_mail=currentLead.email)

        if emailExist.lead_mail==currentLead.email:
            celery.current_app.send_task(
            "app.tasks.leadtoclient_sendreglink.sendreglink", args=(str(emailExist.id),))    
    
    except ObjectDoesNotExist:
        reglink =   Reglink.objects.create(
                    lead_id=currentLead.id,
                    lead_firstname=currentLead.first_name,
                    lead_lastname=currentLead.last_name,
                    lead_mail=currentLead.email,
                    )
        reglink.save()
        getNewRegLink = Reglink.objects.get(lead_mail=currentLead.email)
        celery.current_app.send_task(
            "app.tasks.leadtoclient_sendreglink.sendreglink", args=(str(getNewRegLink.id),))  

    return HttpResponseRedirect(reverse('lead_client', args=(str(lead_id),)))

# @login_required(login_url= '/accounts/login')
def leadactivation(request, reglink):
    regForm = UserForm()
    currentReglink =   Reglink.objects.get(lead_reglink=reglink)
    regForm=UserForm (initial={'email': str(currentReglink.lead_mail),
                                'first_name': str(currentReglink.lead_firstname), 
                                'last_name': str(currentReglink.lead_lastname)}, auto_id=False)
    if request.method == 'POST':
        regForm=UserForm(request.POST)
        regFormEmail = regForm['email'].value()
        if regForm.is_valid():
            regForm.save()

            profileUser=User.objects.get(email=regFormEmail)
            userProfile = Profile.objects.create(user = profileUser )
            userProfile.save()

            clientProfile = Profile.objects.get(user=profileUser)
            clientProfileCreate = Client.objects.create(profile=clientProfile)
            clientProfileCreate.save()
            return HttpResponseRedirect(reverse('accounts:login'))

    context ={"regForm":regForm}    
    return render(request, 'main/lead_regform.html', context)
