from django.forms.models import model_to_dict
from app.models.project import Project
import celery
import email
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from accounts.models.user import User
from app.models.profile import Profile
from app.models.lead import Lead
from app.models.reglink import Reglink
from accounts.forms import UserForm, UserUpdateForm, UserFormNoEmail
from app.models.client import Client
from app.forms.profile import ProfileUpdateForm
from app.forms.client import ClientForm
from accounts.models.user import User
from django.contrib.auth.models import Group


class LeadCreate(CreateView):
    model = Lead
    template_name = "main/contact_us_mail.html"
    fields = ("first_name", "last_name","email","entity_name", "details")
    # success_url = reverse_lazy("main")
    def get_success_url(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return reverse('lead_mail_lists')
        else:
            return reverse('main')



# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff']),  name="dispatch")
class LeadMailList(ListView):
    model = Lead
    paginate_by = 9
    template_name = "main/lead_mail_lists.html"
    fields = ("first_name", "last_name","email","entity_name", "details")
    context_object_name = "leads"

# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff']),  name="dispatch")
class LeadMailView(DetailView):
    model = Lead
    template_name       =   'main/lead_mail_view.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'lead'

    

# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff']),  name="dispatch")
class LeadMailViewLead(DetailView):
    model = Lead
    template_name       =   'main/lead_mail_view_lead.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'lead'

    

@method_decorator(login_required, name="dispatch")
class LeadMailDelete(DeleteView):
    model = Lead        
    # template_name       =   'main/lead_mail_confirm_delete.html'        
    # pk_url_kwarg        =   'pk'
    success_url = reverse_lazy("lead_mail_lists")
    # context_object_name =   'lead'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff']),  name="dispatch")
class LeadToClient(DetailView):
    model = Lead
    template_name       =   'main/lead_client.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'lead'

    def get_context_data(self, **kwargs):
        context         =    super(LeadToClient, self).get_context_data(**kwargs)
        currentObject    =    Lead.objects.get(id=self.kwargs['pk'])
        context['lead_mails']     =    Lead.objects.all().filter(email=currentObject.email)        
        context['show_convert']     =  User.objects.filter(email=currentObject.email)
        return context



@login_required()
@allowed_users(allowed_roles=['admin', 'staff'])
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
    regForm = UserFormNoEmail()
    currentReglink =   Reglink.objects.get(lead_reglink=reglink)
    regForm=UserFormNoEmail(initial={'email': str(currentReglink.lead_mail),
                                'first_name': str(currentReglink.lead_firstname), 
                                'last_name': str(currentReglink.lead_lastname)}, auto_id=False)
    # regForm.fields['email'].disabled = True
                                
    if request.method == 'POST':
        regForm=UserFormNoEmail(request.POST)
        regFormEmail = regForm['email'].value()
        if regForm.is_valid():
            user = regForm.save()
            group = Group.objects.get(name='client')
            user.groups.add(group)
            

            profileUser=User.objects.get(email=regFormEmail)
            userProfile = Profile.objects.create(user = profileUser )
            userProfile.save()

            if "client_enabled" in request.POST:
                clientProfile = Profile.objects.get(user=profileUser)
                clientProfileCreate = Client.objects.create(profile=clientProfile)
                clientProfileCreate.save()
                return HttpResponseRedirect(reverse('accounts:login'))
            else:
                return HttpResponseRedirect(reverse('accounts:login'))

    context ={"regForm":regForm, 'leadmail':str(currentReglink.lead_mail)}    
    return render(request, 'main/lead_regform.html', context)

# @login_required()
@allowed_users(allowed_roles=['admin', 'staff', 'client'])
def userprofile(request):
    # user=request.user
    profileform = ProfileUpdateForm()
    currentUser = request.user    
    currentProfile = Profile.objects.get(user=currentUser)
    profileform = ProfileUpdateForm(initial={
        "avatar" : currentProfile.avatar,
        "is_logicmorph_staff":currentProfile.is_logicmorph_staff,
        "is_dark_theme":currentProfile.is_dark_theme
    },  auto_id=False)
    # Update user form (username, fname, lname) -- START
    userform = UserUpdateForm(initial ={
        'username': currentUser.username,
        'first_name': currentUser.first_name,
        'last_name':currentUser.last_name
    })    
    if request.method == 'POST': 
        if UserUpdateForm(request.POST, instance=request.user):
            userform=UserUpdateForm(request.POST, instance=request.user)
            if userform.is_valid():
                userform.save()
                return HttpResponseRedirect(reverse('user_profile'))
            # else:
            #     return HttpResponseRedirect(reverse('accounts:home'))
        
        # if UserUpdateForm(request.POST, instance=request.user):

        if ProfileUpdateForm(request.POST, instance=currentProfile):
            profileform=ProfileUpdateForm(request.POST,  request.FILES, instance=currentProfile)
            if profileform.is_valid():
                profileform.save()
                return HttpResponseRedirect(reverse('user_profile'))
            # else:
            #     return HttpResponseRedirect(reverse('accounts:home'))
        

        
    # Update user form (username, fname, lname) -- END

    context ={"userform":userform, "profileform":profileform}

    return render(request, 'main/userprofile.html', context)

    
