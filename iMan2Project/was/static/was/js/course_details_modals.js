const editCourseModal = document.getElementById("editCourseModal");
const editCourseBtn = document.getElementById("editCourseButton");

editCourseBtn.onclick = function() {
    editCourseModal.classList.add("show");
}

function closeEditCourseModal() {
    editCourseModal.classList.remove("show");
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
}
