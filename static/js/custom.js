
$(document).ready(function(){
    $(".menubars").hide()
    $(".hideupdate_button").hide()
    $(".sidebar-btn").on("click", function(){
        $(".wrapper").toggleClass("collapser");
        $(".menubars").toggle();

    });

    $(".trigger_submit").on("click", function(){
        $(".hideupdate_button").click()

    });
});