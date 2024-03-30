const sidenav = document.getElementById("sidenav");
const sidenavToggle = document.getElementById("sidenav-toggle");

function openNav() {
  sidenav.style.width = "250px";
}

function closeNav() {
  sidenav.style.width = "0";
}

function handleClickOutside(event) {
    if (event.target !== sidenav && event.target !== sidenavToggle) {
        closeNav();
    }
    if (event.target === sidenavToggle) {
        openNav();
    }
}

document.body.addEventListener("mousedown", handleClickOutside);