// making a function for copying the url
console.log("honey singh");
// copy url for home page 
function copypostUrl(parm) {
    // if unable to get window
    if (!window.getSelection) {
        alert("Please copy the URL from the location bar.");
        return;
    }
    const dummy = document.createElement("p");
    dummy.textContent = window.location.hostname + "/forest/download?post_id=" + parm;
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

// copy url for download page 
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

$(document).ready(function() {
    $("#sub_msg").toast("show");
});

// this is for search button
$(".search-button").click(function() {
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

    $.each(class_list, function(index, value) {
        if (value === "rm-other") {
            hided = true;
        } else {
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

document.onreadystatechange = function() {
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
const elements = document.querySelectorAll("body > :not(.disable-slider)");
for (i = 0; i < elements.length; i++) {
    elements[i].addEventListener("touchstart", handleTouchStart, false);
    elements[i].addEventListener("touchmove", handleTouchMove, false);
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
                if (close_button != null) {
                    close_button.click();
                }
            } else {
                // right swipe
                // opening left slider
                var trigger_button = document.getElementById("slider-trigger-button");
                if (trigger_button != null) {
                    trigger_button.click();
                }
                // if someone swipe right so closing all opened modal or offcanvases
                var download_bottom_slider_close = document.getElementsByClassName("download-bottom-slider-close");
                if (download_bottom_slider_close != null) {
                    // console.log(download_bottom_slider_close)
                    Array.from(download_bottom_slider_close).forEach(function(element) {
                        element.click()

                    })
                }
                var share_modal_close = document.getElementsByClassName("share-modal-close");
                if (share_modal_close != null) {
                    Array.from(share_modal_close).forEach(function(element) {
                        element.click();
                    })
                }
                var more_details_modal = document.getElementsByClassName("more-details-close")
                if (more_details_modal != null) {
                    Array.from(more_details_modal).forEach(function(element) {
                        element.click()
                    })
                }
            }
        } else {
            if (yDiff > 0) {
                // if someone swipe top close share modal if open 
                var share_modal_close = document.getElementsByClassName("share-modal-close");
                if (share_modal_close != null) {
                    Array.from(share_modal_close).forEach(function(element) {
                        element.click()
                    })
                }
            } else {
                // if user swipe down 
                var more_details_modals = document.getElementsByClassName("more-details-fullscreen-modal")
                // intilizing modal status 
                read_more_modal_showing = false
                if (more_details_modals != undefined) {
                    Array.from(more_details_modals).forEach(function(element) {
                        if (element.style.display === "block") {
                            read_more_modal_showing = true
                        } else {

                        }
                    })
                    if (!read_more_modal_showing) {
                        // getting download_botton_slider and closing all 
                        var download_bottom_slider_close = document.getElementsByClassName("download-bottom-slider-close");
                        if (download_bottom_slider_close != null) {
                            // console.log(download_bottom_slider_close)
                            Array.from(download_bottom_slider_close).forEach(function(element) {
                                element.click()

                            })
                        }
                        // getting share modal and closeing all
                        var share_modal_close = document.getElementsByClassName("share-modal-close");
                        if (share_modal_close != null) {
                            Array.from(share_modal_close).forEach(function(element) {
                                element.click();
                            })
                        }

                    }
                }

            }
        }
        /* reset values */
        xDown = null;
        yDown = null;

    }
}

