$(document).ready(function(){

$(".nav-link").click(function(){
$('.nav-tabs').find('.nav-link').removeClass("active");
$(this).addClass('active');
});

});