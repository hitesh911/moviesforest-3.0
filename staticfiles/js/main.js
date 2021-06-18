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

$(function() {
    $("#query_input").autocomplete({
        source: "jquery_search"
    });
});