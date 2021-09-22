

$(window).ready(function () {
    
    $('input[type=radio][name=type_client]').on('change', function() {
      CheckTypeClient($(this));
    });
    
  // $("input:radio:first").click();
  $("#basic-non-sticky-notification-toggle").click();
  
  $(".btn-delete").click(function(){
    
    var url = $(this).attr("data-url");
    alert(url);
  });

}); 

function CheckTypeClient($element){
  switch ($element.val()) {
      case '1': // 1: Physique
          
          $('div[data-client=moral]').find('input:text').each(function() {
              // alert($(this).val() +" => " + $(this).attr("id"));
             $(this).val('');
             $(this).prop('required', false);
             $(this).prop('disabled', true);
          });
        break;
      case '2': // 1: Moral
          $('input[name=company]').prop('required', true);
          $('input[name=company]').prop('disabled', false);
          
        break;
  }
}



  //   $('input[type=radio][name=type_client]').on('change', function() {
      
  //     switch ($(this).val()) {
  //       case '1': // 1: Physique
  //           $('div[data-client=moral]').css({'display': 'none'}).find('input:text').each(function() {
  //               // alert($(this).val() +" => " + $(this).attr("id"));
  //               $(this).val('');
  //           });
  //           $('div[data-client=physique]').show();
  //         break;
  //       case '2': // 1: Moral
  //           $('div[data-client=moral]').show();
            
  //           $('div[data-client=physique]').css({'display': 'none'}).find('input:text').each(function() {
  //               // alert($(this).val() +" => " + $(this).attr("id"));
  //               $(this).val('');
  //           });
  //         break;
  //     }
  // });