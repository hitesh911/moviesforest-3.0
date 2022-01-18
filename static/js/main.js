// making a function for copying the url 
console.log("yes")
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
    console.log("open added")
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

// for clicking automatically to hollywood button when load home 


  if(window.location.pathname == "/"){
      var clickbutton  = document.getElementById("clickhere_home_button")
      if (clickbutton != null){
          clickbutton.click()

      }
  }

// function to show loading screen 

// $('.loading_button').click(function(){
//     console.log("clicked")
//     $(".loadingbar").show()
    
// })
document.onreadystatechange = function(){
    if(document.readyState !== "complete"){
        // document.querySelector("body").style.background ="transparent";
        $("body").addClass("body-while-loading")
        document.querySelector(".loadingbar").style.visibility ="visible";
        
        
    }else{
        $("body").removeClass("body-while-loading")
        document.querySelector(".loadingbar").style.visibility ="hidden";
    
    }
}
