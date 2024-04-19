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



// fetch('side_bar.html')
//         .then(response => response.text())
//         .then(data => {
//             document.getElementById('navbar-placeholder').innerHTML = data;
//         });