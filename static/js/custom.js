
$(document).ready(function(){
    $(".btnupdateupdate").attr('disabled','disabled')
    $(".menubars").hide()
    $(".hideupdate_button").hide()
    $(".hide_button_user").hide()
    $(".hide_button_profile").hide()
    $(".sidebar-btn").on("click", function(){
        $(".wrapper").toggleClass("collapser");
        $(".menubars").toggle();

    });

    $(".trigger_submit").on("click", function(){
        $(".hideupdate_button").click()
        $(".hide_button_user").click()

    });

    // let currentVal ="";
    $(".user_group_current").on("change", function(){
        let currentVal = $(this).val();
        let currentGroup = $(this).attr("curvalue");
        let groupID = $(this).attr("group-sid");

        if (currentVal != currentGroup) {
            $(".btnupdate_"+groupID).removeAttr('disabled');
        }
        else {
            $(".btnupdate_"+groupID).attr('disabled','disabled')
        }
    });
});

$(".btnupdate_click").on("click", function(){
    const tokenistan = $(this).attr('csrftoken')
    curvalue  = $(this).attr('curvalue')
    currentID = $(this).attr('id')
    currentEmail = $(this).attr('uemail')
    getselectValue = $(".getselectval_"+currentID).val()
    userData = {
        'currentid': currentID,
        'getselectvalue': getselectValue
    }
    // var confirmResult = confirm("Change " + currentEmail +" user's group from " + curvalue + " to " + getselectValue + "?");
    $.ajax({       
        
        url: '../usergroupchange/',   
        method:'POST',     
        data: userData,
        dataType: 'json',
        headers: {"X-CSRFToken": tokenistan},

        success: function(data){
            window.location = "../currentusers/";
        }
    });
});
