const addCourseModal = document.getElementById("addCourseModal");
const addCard = document.getElementById("addCard");

addCard.onclick = function() {
    addCourseModal.classList.add("show");
}

function closeAddCourseModal() {
    addCourseModal.classList.remove("show");
}

window.onclick = function(event) {
    if (event.target === addCourseModal) {
        addCourseModal.classList.remove("show");
    }
}