const editCourseModal = document.getElementById("editCourseModal");
const editCourseBtn = document.getElementById("editCourseButton");

editCourseBtn.onclick = function() {
    editCourseModal.classList.add("show");
}

function closeEditCourseModal() {
    editCourseModal.classList.remove("show");
}

const editCoverPhotoModal = document.getElementById("editCoverPhotoModal");
const editCoverPhotoBtn = document.getElementById("editCoverPhotoButton");

editCoverPhotoBtn.onclick = function() {
    editCoverPhotoModal.classList.add("show");
}

function closeEditCoverPhotoModal() {
    editCoverPhotoModal.classList.remove("show");
}

const deleteCoverPhotoModal = document.getElementById("deleteCoverPhotoModal");
const deleteCoverPhotoBtn = document.getElementById("deleteCoverPhotoButton");

deleteCoverPhotoBtn.onclick = function() {
    deleteCoverPhotoModal.classList.add("show");
}

function closeDeleteCoverPhotoModal() {
    deleteCoverPhotoModal.classList.remove("show");
}

const deleteCourseModal = document.getElementById("deleteCourseModal");
const deleteCourseButton = document.getElementById("deleteCourseButton");

deleteCourseButton.onclick = function() {
    deleteCourseModal.classList.add("show");
}

function closeDeleteCourseModal() {
    deleteCourseModal.classList.remove("show");
}

const addScheduleModal = document.getElementById("addScheduleModal");
const addScheduleButton = document.getElementById("addScheduleButton");

addScheduleButton.onclick = function() {
    addScheduleModal.classList.add("show");
}

function closeAddScheduleModal() {
    addScheduleModal.classList.remove("show");
}

window.onclick = function(event) {
    if (event.target === editCourseModal) {
        closeEditCourseModal();
    }
    if (event.target === deleteCourseModal) {
        closeDeleteCourseModal();
    }
    if (event.target === addScheduleModal) {
        closeAddScheduleModal();
    }
    if (event.target === editCoverPhotoModal) {
        closeEditCoverPhotoModal();
    }
    if (event.target === deleteCoverPhotoModal) {
        closeDeleteCoverPhotoModal();
    }
}
