$(document).ready(function() {
    console.log("ready");
    var state = location.search.substring(1);
    console.log("state:"+state);
    $(".state").click(function(){
	var state = $(this).text();
	console.log(state);
    });
});
