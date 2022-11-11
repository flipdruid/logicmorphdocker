
$(document).ready(function(){
    $(".menubars").hide()
    $(".sidebar-btn").on("click", function(){
        $(".wrapper").toggleClass("collapser");
        $(".menubars").toggle();

    });
});