$(document).ready(function () {
    
    $('input[type=radio][name=type_client]').on('change', function() {
    
        switch ($(this).val()) {
        case 1:
          alert("Allot Thai Gayo Bhai");
          break;
        case 2':
          alert("Transfer Thai Gayo");
          break;
  }
    if (this.value == 1) {
        $('input[type=radio][name=type_client]')
    }
    else {
        alert("Transfer Thai Gayo : " + $(this).val());
    }
});
}); 