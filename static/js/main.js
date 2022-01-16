// making a function for copying the url 
console.log("i am here")
function copyUrl() {
    // if unable to get window 
    if (!window.getSelection) {
        alert('Please copy the URL from the location bar.');
        return;
    }
    const dummy = document.createElement('p');
    dummy.textContent = window.location.href;
    document.body.appendChild(dummy);

    const range = document.createRange();
    range.setStartBefore(dummy);
    range.setEndAfter(dummy);

    const selection = window.getSelection();
    // First clear, in case the user already selected some other text
    selection.removeAllRanges();
    selection.addRange(range);

    document.execCommand('copy');
    document.body.removeChild(dummy);
    alert("Link has been copied Go and share Link..");
}

$(document).ready(function() {
    $("#sub_msg").toast('show');
});

// this is for search button 
$('.search-button').click(function(){
    $(this).parent().toggleClass('open');

    
    var i = $("#other-nav-items").attr("class");
    var hided = false;
    var class_list = i.split(/\s+/);
    
    $.each(class_list , function (index , value){

        if(value === "rm-other" ){
            hided = true;
            
        }else{
            hided = false;
            
        }
    })

    if(hided){
        $("#other-nav-items").show();
        $("#other-nav-items").removeClass("rm-other");
    }
    else{
        $("#other-nav-items").hide();
        $("#other-nav-items").addClass("rm-other");
    }



    
  });


// $('.search-button').click(function (){
    
    // item.toggleClass("display") === 'block'?'none' : 'block';
   
// })

