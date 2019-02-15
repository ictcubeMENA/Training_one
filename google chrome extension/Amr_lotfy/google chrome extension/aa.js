 localArray = [];
    
    if (!localStorage.keyWords) {
      localStorage.setItem('keyWords', JSON.stringify(localArray));
    }
    
    loadKeyWords();
    
    function loadKeyWords() {
        $('#keyWords').html('');
        localArray = JSON.parse(localStorage.getItem('keyWords'));
        for(var i = 0; i < localArray.length; i++) {
          $('#keyWords').prepend('<li>'+localArray[i]+'</li>'); 
            }
        }
    
    $('#add').click( function() {
       var Description = $('#description').val();
      if($("#description").val() === '') {
        $('#alert').html("<strong>Warning!</strong> You left the to-do empty");
        $('#alert').fadeIn().delay(1000).fadeOut();
        
        return false;
       }
       $('#form')[0].reset();
       var keyWords = $('#keyWords').html();
       localArray.push(Description);
       localStorage.setItem('keyWords', JSON.stringify(localArray));
       loadKeyWords();
       return false;
    });
    
    $('#clear').click( function() {
    window.localStorage.clear();
    location.reload();
    return false;
    });