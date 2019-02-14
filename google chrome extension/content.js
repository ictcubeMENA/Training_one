(function() {
    chrome.runtime.onMessage.addListener(function(msg, sender, sendResponse) {
        if (msg.data !== undefined) {
          x=JSON.parse(msg.data )
            console.log(x);
            // x=JSON.parse(msg.data)
        }
    });
    
    $(document).on('click', '.ghx-issue', function test1 () {
      
       setTimeout(function (){
        //   console.log(x)
           $('.Content__Header-sc-1npw367-2').css('background-color','red');
           $('.kotTne').append(` <div id="bbb"> <table id="table11" style="width:50%" border="1"  >
           <tr>
             <th>ID</th>
             <th>NAme</th>
             <th>Country</th>
           </tr>
           
           
         </table></div>`);
           console.log("hiiiiii")
           
           
        }, 1400);
        setTimeout(function (){
          
          for( i=0;i<x.length;i++)
            
                
                {
                  $('#table11').append(` 
               
                  <tr>
                    <td>`+x[i].firstName+`</td>
                    <td>`+x[i].middleName+`</td>
                    <td>`+x[i].lastName+`</td>
                  </tr>
                  
              `);

                }
                
                
             
               
               
            }, 1400);
        
         
      
   })
 //   kotTne
   
   
 
 })();
 