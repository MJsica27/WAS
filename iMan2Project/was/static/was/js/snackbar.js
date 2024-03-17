function snackbar() {
    const x = document.getElementById("snackbar");
    x.classList.add("show");
    setTimeout(function() {
        x.classList.remove("show");
    }, 3000);
}

window.onload = function() {
    snackbar();
};