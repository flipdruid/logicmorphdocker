from app.models.profile import Profile
from app.models.client import Client
from django.core.exceptions import ObjectDoesNotExist

def currentuserprofileclient(request):
    userprofile=""
    profileclient=""
    main_body_theme=""
    nav_item_font=""

    if request.user.is_authenticated:
        try:
            
            userprofile = Profile.objects.get(user=request.user)
            profileclient = Client.objects.get(profile=userprofile)

            if userprofile.is_dark_theme:                
                main_body_theme ="is_dark"
                nav_item_font = "nav-item-font-dark"
                footer_social = "footer-social-dark"
                lm_logotext = "lm-logotext-dark"
                turn_text_for_dark="turn-text-for-dark"
                contact_us_now ="contactusnow-dark"
                SAP_btn_color ="btn-success"
                
            else:
                nav_item_font = "nav-item-font-light"
                main_body_theme="is_light"
                footer_social = "footer-social"
                lm_logotext = "lm-logotext"
                turn_text_for_dark=""
                contact_us_now ="contactusnow"
                SAP_btn_color ="btn-primary"

        except ObjectDoesNotExist:
            pass
    else:
        nav_item_font = "nav-item-font-light"       
        main_body_theme="is_light"
        footer_social = "footer-social"
        lm_logotext = "lm-logotext"
        turn_text_for_dark=""
        contact_us_now ="contactusnow"
        SAP_btn_color ="btn-primary"
    return {"userprofile": userprofile, 
            "profileclient": profileclient, 
            "main_body_theme":main_body_theme,
            "nav_item_font": nav_item_font, 
            "footer_social": footer_social,
            "lm_logotext":lm_logotext,
            "turn_text_for_dark": turn_text_for_dark,
            "contact_us_now":contact_us_now, 
            "SAP_btn_color":SAP_btn_color}