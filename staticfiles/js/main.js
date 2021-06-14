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
(function(document) {
    var div = document.getElementById('arrow_icon_container');
    var icon = document.getElementById('arrow_icon');
    var open = false;

    div.addEventListener('click', function() {
        if (open) {
            icon.className = 'fa fa-arrow-down';
        } else {
            icon.className = 'fa fa-arrow-down open';
        }

        open = !open;
    });
})(document);