$('document').ready(function(){
    var x = new Object();
    $('.read-more-btn').click(function(){

        console.log("click");
        var val = $(this).val();
        console.log(val);
        var p = '#p_' + val;
        var btn = '#btn_' + val;
        console.log(p);
        if(x[p]){
            $(p).animate({height : '150px'},1000);
            x[p] = false;
            $(btn).text('Read More')
        } else {
            $(p).animate({height : $(p)[0].scrollHeight},1000);
            x[p] = true;
            $(btn).text('Read Less')
        }

    });
});
