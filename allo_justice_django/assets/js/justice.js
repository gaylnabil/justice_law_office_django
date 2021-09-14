// var replyText = '';
var sub_html = '';

$(document).ready(function () {
    
    jQuery("time.timeago").timeago();
    // Comments Form

    $('#confirmed').click(function (e) {

        console.log("it clicked !!!");

        $.get("/content_subcomment", function (data) {
            value = data.sub_html;
            console.log(value);
            alert(value);
            $("#gayl").html(value);
        });

    });

    // $('#btn-comment').mouseover(function () {
        
    //     $.get("/content_subcomment", function (data) {
    //         sub_html = data.sub_html;
    //         alert("btn-comment : " + sub_html);
    //     });
        
    // });
    
    $('#comment-form').submit(function (e) { 
        e.preventDefault(); // prevent actual form submit
        var $form = $(this);
        var url = $form.attr('action');
        var type = $form.attr('method');
        var id = $form.attr('id');
        // alert("form : " + id + "; type :" + type + "; action : " + url);
       
        $.ajax({
             type: type,
            url: url,
            data: $form.serialize(),
            success: function (response) {
                
                var comment = response.comment;
                console.log(comment);
                $('#last-reply-'+ id).remove();
                alert("textarea : " + $form.find('textarea').val());
                var created_at = jQuery.timeago(comment.created_at);
                alert(created_at);
                // alert("good : " + sub_html);
                var html = ('<li>'+ 
                    '<div div class= "media comment-author" > ' +
                    '<a class="media-left" href="#"><img class="img-thumbnail" alt=""></a>' +
                    '<div class="media-body">'+
                        '<h5 class="media-heading comment-heading text-theme-colored">');
                
                html += comment.type == 0 ? '<i class="fa fa-user fa-lg text-theme-colored"></i>' : '<i class="fa fa-graduation-cap fa-lg text-theme-colored"></i>';
                html += (comment.fullName + ':' +
                    '</h5>' +
                    '<div class="comment-date mb-5"><span><i class="fa fa-calendar text-theme-colored"></i> ' + created_at + '</span></div> ' +
                    '<p style="white-space:pre-wrap;">' + comment.text + '</p>' +
                    '<form class="form-delete" action="/justice/' + comment.id + '/Comment" method="GET" >' +
                        '<a class="replay-icon pull-right text-theme-colored link-delete ml-15" href=""> <i class="fa fa-trash-o text-theme-colored"></i> '+ gettext('Supprimer') +'</a>' +
                    '</form>' +
                    '<a id="last-reply-' + comment.id + '" class="replay-icon pull-right text-theme-colored btn-delete link-reply" data-id="' + comment.id + '" href=""> <i class="fa fa-commenting-o text-theme-colored"></i> ' + gettext('Réponse') + '</a>' +
                    '<div class="clearfix"></div>' +
                    '<div id="new-subcomment-' + comment.id + '"></div>' +
                    '<div id="nga"></div>' +
                    '</div>' +
                    '</div>'+
                    '<li>');
                
                $(".comment-list").append(html);
                $form.find('textarea').val('');

                $.get("/content_subcomment/"+ comment.id, function (data) {
                    sub_html = data.sub_html;
                    alert("btn-comment : " + sub_html);
                    $("#nga").replaceWith(sub_html);
                });
            },
            error : function(xhr,msg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                alert(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        }, 'json');

    });



    $('.form-sub').submit(function (e) { 
        e.preventDefault(); // prevent actual form submit
        var $form = $(this);
        var url = $form.attr('action');
        var type = $form.attr('method');
        var id = $form.attr('data-form-id');
        // alert("form-sub: "  +id);

        $.ajax({
            type: type,
            url: url,
            data: $form.serialize(),
            success: function (response) {
                
                var subComment = response.subComment;
                console.log(subComment);
                $('#last-reply-'+ id).remove();
                // alert("textarea : " + $form.find('textarea').val());
                // document.getElementById("post-form").reset();
                var created_at = jQuery.timeago(subComment.created_at);
                // alert(created_at);
                var html = ('<div class= "media comment-author nested-comment" > <a href="#" class="media-left pt-20"><img alt="" class="img-thumbnail"></a>'+
                    '<div class="media-body p-20 bg-lighter"> '+
                        '<h5 class="media-heading comment-heading text-theme-colored">');
                
                html += subComment.type == 0 ? '<i class="fa fa-user fa-lg text-theme-colored"></i>' : '<i class="fa fa-graduation-cap fa-lg text-theme-colored"></i>';
                html+= ( subComment.fullName + ':'+
                '</h5>'+
                    '<div class="comment-date mb-5"><span><i class="fa fa-calendar text-theme-colored"></i> '+ created_at +'</span></div> ' +
                    '<p style="white-space:pre-wrap;">' + subComment.text + '</p>' +
                    '<a id="last-reply-'+ subComment.cmt_id +'" class="replay-icon pull-right text-theme-colored btn-delete link-reply" data-id="'+ subComment.cmt_id +'" href=""> <i class="fa fa-commenting-o text-theme-colored"></i>'+ replyText +'</a>'+
                    '<div class="clearfix"></div>'+
                    '</div>' +
                    '</div>');
                
                html += '<div id="new-subcomment-' + id + '"></div>';

                $("#new-subcomment-" + id).replaceWith(html);

                $form.find('textarea').val('');
            },
            error : function(xhr,msg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                alert(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        }, 'json');

    });



    $(document).on('click', '.link-reply', function(e) {
        e.preventDefault();
        $link = $(this);
        var id = $link .attr('data-id');
    
        id = "sub-" + id;
        // replyText = $link.text();
        // alert("Reply: " + replyText);
        $("#"+id).css({'display':'inherit'});
        //$("#"+id).show('slow');
    
        $('.new-comment').each(function () {
    
            if (id != $(this).attr('id'))
            {
                $(this).css({ 'display': 'none' });
            }
        }); 
    });
});
