let a = 0, b = 0;

function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    const passwordIcon = document.getElementById("password-icon");

    if (a === 0) {
        passwordInput.type = "text";
        passwordIcon.src = "/static/was/icons/show_password.ico";
        a = 1;
    } else {
        passwordInput.type = "password";
        passwordIcon.src = "/static/was/icons/hide_password.ico";
        a = 0;
    }
}

function toggleConfirmPasswordVisibility() {
    const passwordInput = document.getElementById("confirm_password");
    const passwordIcon = document.getElementById("confirm-password-icon");

    if (b === 0) {
        passwordInput.type = "text";
        passwordIcon.src = "/static/was/icons/show_password.ico";
        b = 1;
    } else {
        passwordInput.type = "password";
        passwordIcon.src = "/static/was/icons/hide_password.ico";
        b = 0;
    }
}

function togglePasswordIcon(inputId, iconId) {
    const passwordIcon = document.getElementById(iconId);
    if (document.getElementById(inputId).value.trim() === "") {
        passwordIcon.style.display = "none";
    } else {
        passwordIcon.style.display = "block";
    }
}

function addPasswordInputListener(inputId, iconId) {
    document.getElementById(inputId).addEventListener("input", function() {
        togglePasswordIcon(inputId, iconId);
    });
}

addPasswordInputListener("password", "password-icon");
addPasswordInputListener("confirm_password", "confirm-password-icon");