

$(window).ready(function () {
    
    $('.radio-type').on('change', function() {
      CheckTypeClient($(this).val());
    });
    
  // $("input:radio:first").click();
  $("#basic-non-sticky-notification-toggle").click();
  
  $(".btn-delete").click(function(){
    
    var url = $(this).attr("data-url");
    var $form = $('#delete-confirmation-modal form'). attr('action',url);
    
  });
  
  
  $('select[name=city]').on('change',function(e){
     $('#btn-search').click();
  });
  
  $('.icon-remove').on('click',function(e){
       $('input[name=query]').val('');
       $('input[name=query]').focus();
  });
  
  $('.icon-reset').on('click',function(e){
     
      $("select[name=city] option[value='all']").prop('selected', true);
      $("select[name=city]").change();
     // $('select[name=city]').focus();
  });
  
  $('.btn-edit').on('click',function(e){
     
    var $form = $('#form-action');
    
    var url = $(this).attr('data-url');
    $form.prop('action', url);
    url = $form.attr('action');
    const type = $form.attr('method');
    var id = $form.attr('id');
    // alert(` id= ${id}\n url= ${url}\n type= ${type}`);
     
    $.get(url, function (data) {
            console.log(data);
            $('input[name=nom_depart]').val(data.departement.nom_depart);
    });

  });
  
  $('#new-depart-id, .btn-edit').on("click", function (e) {
      let $element = $(this);
      if ($element.attr('id') === 'new-depart-id'){
          $('input[name=nom_depart]').val('');
      }
      setTimeout(function() {
          $('input[name=nom_depart]').focus();
          $('input[name=nom_depart]').select();
                                
    }, 800);
    
  });

}); 

function CheckTypeClient(value){
  switch (value) {
      case '1': // 1: Physique
          
          $('div[data-type=moral]').find('input:text').each(function() {
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