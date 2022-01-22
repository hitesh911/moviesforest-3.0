// making a function for copying the url
console.log("honey singh");
function copyUrl() {
  // if unable to get window
  if (!window.getSelection) {
    alert("Please copy the URL from the location bar.");
    return;
  }
  const dummy = document.createElement("p");
  dummy.textContent = window.location.href;
  document.body.appendChild(dummy);

  const range = document.createRange();
  range.setStartBefore(dummy);
  range.setEndAfter(dummy);

  const selection = window.getSelection();
  // First clear, in case the user already selected some other text
  selection.removeAllRanges();
  selection.addRange(range);

  document.execCommand("copy");
  document.body.removeChild(dummy);
  alert("Link has been copied Go and share Link..");
}

$(document).ready(function () {
  $("#sub_msg").toast("show");
});

// this is for search button
$(".search-button").click(function () {
  $(this).parent().toggleClass("open");
  // this is to close slider if open
  var close_button = document.getElementById("close-slider");
  console.log(close_button);
  if (close_button) {
    close_button.click();
  }

  var i = $("#other-nav-items").attr("class");
  var hided = false;
  var class_list = i.split(/\s+/);

  $.each(class_list, function (index, value) {
    if (value === "rm-other") {
      hided = true;
    } 
    else {
      hided = false;
    }
  });

  if (hided) {
    $("#other-nav-items").show();
    $("#other-nav-items").removeClass("rm-other");
  } else {
    $("#other-nav-items").hide();
    $("#other-nav-items").addClass("rm-other");
  }
});

// for clicking automatically to hollywood button when load home

// if (window.location.pathname == "/") {
//   var clickbutton = document.getElementById("clickhere_home_button");
//   if (clickbutton != null) {
//     clickbutton.click();
//   }
// }

document.onreadystatechange = function () {
  if (document.readyState !== "complete" && window.location.pathname != "/") {
    // document.querySelector("body").style.background ="transparent";
    $("body").addClass("body-while-loading");
    document.querySelector(".loadingbar").style.visibility = "visible";
  } else {
    $("body").removeClass("body-while-loading");
    document.querySelector(".loadingbar").style.visibility = "hidden";
  }
};

// this javascript for swipe right or left
document.addEventListener("touchstart", handleTouchStart, false);
document.addEventListener("touchmove", handleTouchMove, false);

var xDown = null;
var yDown = null;

function getTouches(evt) {
  return (
    evt.touches || // browser API
    evt.originalEvent.touches
  ); // jQuery
}

function handleTouchStart(evt) {
  const firstTouch = getTouches(evt)[0];
  xDown = firstTouch.clientX;
  yDown = firstTouch.clientY;
}

function handleTouchMove(evt) {
  if (!xDown || !yDown) {
    return;
  }

  var xUp = evt.touches[0].clientX;
  var yUp = evt.touches[0].clientY;

  var xDiff = xDown - xUp;
  var yDiff = yDown - yUp;

  if (Math.abs(xDiff) > Math.abs(yDiff)) {
    /*most significant*/
    if (xDiff > 0) {
      var close_button = document.getElementById("close-slider");
      close_button.click();
    } else {
      var trigger_button = document.getElementById("slider-trigger-button");
      trigger_button.click();
    }
  } else {
    if (yDiff > 0) {
    } else {
    }
  }
  /* reset values */
  xDown = null;
  yDown = null;
}
