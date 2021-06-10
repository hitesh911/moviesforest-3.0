// making a function for copying the url 
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


//grab the video dom element
const video = document.querySelector('iframe');
const notifications = document.querySelectorAll('.notification');
const forwardNotificationValue = document.querySelector('.video-forward-notify span');
const rewindNotificationValue = document.querySelector('.video-rewind-notify span');

let timer;
let rewindSpeed = 0;
let forwardSpeed = 0;

//function for double click event listener on the video
//todo change those variable to html5 data attributes
function updateCurrentTime(delta) {
    let isRewinding = delta < 0;

    if (isRewinding) {
        rewindSpeed = rewindSpeed + delta;
        forwardSpeed = 0;
    } else {
        forwardSpeed = forwardSpeed + delta;
        rewindSpeed = 0;
    }

    //clear the timeout
    clearTimeout(timer);

    let speed = (isRewinding ? rewindSpeed : forwardSpeed);
    video.currentTime = video.currentTime + speed;

    let NotificationValue = isRewinding ? rewindNotificationValue : forwardNotificationValue;
    NotificationValue.innerHTML = `${Math.abs(speed)} seconds`;

    //reset accumulator within 2 seconds of a double click
    timer = setTimeout(function() {
        rewindSpeed = 0;
        forwardSpeed = 0;
    }, 2000); // you can edit this delay value for the timeout, i have it set for 2 seconds
    console.log(`updated time: ${video.currentTime}`);
}


function animateNotificationIn(isRewinding) {
    isRewinding ? notifications[0].classList.add('animate-in') : notifications[1].classList.add('animate-in');
}

function animateNotificationOut() {
    this.classList.remove('animate-in');
}

function forwardVideo() {
    updateCurrentTime(10);
    animateNotificationIn(false);
}

function rewindVideo() {
    updateCurrentTime(-10);
    animateNotificationIn(true);
}

//Event Handlers
function doubleClickHandler(e) {
    console.log(`current time: ${video.currentTime}`);
    const videoWidth = video.offsetWidth;
    (e.offsetX < videoWidth / 2) ? rewindVideo(): forwardVideo();
}

function togglePlay() {
    video.paused ? video.play() : video.pause();
}

//Event Listeners
video.addEventListener('click', togglePlay);
video.addEventListener('dblclick', doubleClickHandler);
notifications.forEach(function(notification) {
    notification.addEventListener('animationend', animateNotificationOut);
});