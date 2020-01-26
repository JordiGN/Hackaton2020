

function display_post(post){
    var poster = post["poster"];
    var date = post["date"];
    var title = post["title"];
    var id = post["id"];
    
    var html = '<a href="" id="'+id+'"><div class="post">'
	+'<div class="posttitle">'+title+'</div>'
	+'<div class="postauthor">'+poster+" - "+date+'</div>'
	+'</div></a>';
    console.log(html);
    $('#posts').append(html);
    return;
}


$(document).ready(function() {
    console.log("ready");
    var state =  location.search.substring(1);
    console.log("state:"+state);


    display_post({
	title:"this is a test post",
	date:"11/11/11",
	id:"6969696969",
	poster:"Dirty Dan"
    });
    display_post({
	title:"this is a test post",
	date:"10/10/20",
	id:"1231233",
	poster:"T. Alberto Barbosa"
    });


});
