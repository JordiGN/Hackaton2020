

function display_post(post){



}


$(document).ready(function() {
    console.log("ready");
    var state =  location.search.substring(1);
    console.log("state:"+state);


    display_post({
	title:"this is a test post",
	date:"11/11/11",
	poster:"richard dickson"
    });


});
