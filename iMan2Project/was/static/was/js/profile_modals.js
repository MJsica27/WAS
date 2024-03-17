const deleteAccountModal = document.getElementById("deleteAccountModal");
const deleteAccountBtn = document.getElementById("deleteAccountButton");

deleteAccountBtn.onclick = function() {
    deleteAccountModal.classList.add("show");
}

function closeDeleteAccountModal() {
    deleteAccountModal.classList.remove("show");
}

const logoutModal = document.getElementById("logoutModal");
const logoutBtn = document.getElementById("logoutButton");

logoutBtn.onclick = function() {
    logoutModal.classList.add("show");
}

function closeLogoutModal() {
    logoutModal.classList.remove("show");
}

const editAccountDetailsModal = document.getElementById("editAccountDetailsModal");
const editAccountDetailsBtn = document.getElementById("editAccountDetailsButton");

editAccountDetailsBtn.onclick = function() {
    editAccountDetailsModal.classList.add("show");
}

function closeEditAccountDetailsModal() {
    editAccountDetailsModal.classList.remove("show");
}

const editEmailAddressModal = document.getElementById("editEmailAddressModal");
const editEmailAddressBtn = document.getElementById("editEmailAddressButton");

editEmailAddressBtn.onclick = function() {
    editEmailAddressModal.classList.add("show");
}

function closeEditEmailAddressModal() {
    editEmailAddressModal.classList.remove("show");
}

const editPersonalInformationModal = document.getElementById("editPersonalInformationModal");
const editPersonalInformationBtn = document.getElementById("editProfileInformationButton");

editPersonalInformationBtn.onclick = function() {
    editPersonalInformationModal.classList.add("show");
}

function closeEditPersonalInformationModal() {
    editPersonalInformationModal.classList.remove("show");
}

const changePasswordModal = document.getElementById("changePasswordModal");
const changePasswordBtn = document.getElementById("changePasswordButton");

changePasswordBtn.onclick = function() {
    changePasswordModal.classList.add("show");
}

function closeChangePasswordModal() {
    changePasswordModal.classList.remove("show");
}

window.onclick = function(event) {
    if (event.target === logoutModal) {
        closeLogoutModal();
    }
    if (event.target === deleteAccountModal) {
        closeDeleteAccountModal();
    }
    if (event.target === editAccountDetailsModal) {
        closeEditAccountDetailsModal();
    }
    if (event.target === editEmailAddressModal) {
        closeEditEmailAddressModal();
    }
    if (event.target === editPersonalInformationModal) {
        closeEditPersonalInformationModal();
    }
    if (event.target === changePasswordModal) {
        closeChangePasswordModal();
    }
}