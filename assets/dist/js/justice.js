$(document).ready(function () {
    
    $('input[type=radio][name=type_client]').change(function() {
    if (this.value == 'allot') {
        alert("Allot Thai Gayo Bhai");
    }
    else {
        alert("Transfer Thai Gayo : " + $(this).val());
    }
});
}); 