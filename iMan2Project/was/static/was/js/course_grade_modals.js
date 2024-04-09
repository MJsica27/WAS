//Add Midterm
const addMidtermGradeModal = document.getElementById("addMidtermGradeModal");
const addMidtermGradeBtn = document.getElementById("addMidtermGradeBtn");

if (addMidtermGradeBtn) {
    addMidtermGradeBtn.onclick = function() {
        addMidtermGradeModal.classList.add("show");
    }
}

function closeAddMidtermGradeModal() {
    addMidtermGradeModal.classList.remove("show");
}

//Add Final
const addFinalGradeModal = document.getElementById("addFinalGradeModal");
const addFinalGradeBtn = document.getElementById("addFinalGradeBtn");

if (addFinalGradeBtn) {
    addFinalGradeBtn.onclick = function() {
        addFinalGradeModal.classList.add("show");
    }
}

function closeAddFinalGradeModal() {
    addFinalGradeModal.classList.remove("show");
}

//Edit Midterm
const editMidtermGradeModal = document.getElementById("editMidtermGradeModal");
const editMidtermGradeBtn = document.getElementById("editMidtermGradeBtn");
 
if (editMidtermGradeBtn) {
    editMidtermGradeBtn.onclick = function() {
        editMidtermGradeModal.classList.add("show");
    }
}

function closeEditMidtermGradeModal() {
    editMidtermGradeModal.classList.remove("show");
}

//Edit Final
const editFinalGradeModal = document.getElementById("editFinalGradeModal");
const editFinalGradeBtn = document.getElementById("editFinalGradeBtn");

if (editFinalGradeBtn) {
    editFinalGradeBtn.onclick = function() {
        editFinalGradeModal.classList.add("show");
    }
}

function closeEditFinalGradeModal() {
    editFinalGradeModal.classList.remove("show");
}

//Delete Midterm
const deleteMidtermGradeModal = document.getElementById("deleteMidtermGradeModal");
const deleteMidtermGradeBtn = document.getElementById("deleteMidtermGradeBtn");

if (deleteMidtermGradeBtn) {
    deleteMidtermGradeBtn.onclick = function() {
        deleteMidtermGradeModal.classList.add("show");
    }
}

function closeDeleteMidtermGradeModal() {
    deleteMidtermGradeModal.classList.remove("show");
}

//Delete Final
const deleteFinalGradeModal = document.getElementById("deleteFinalGradeModal");
const deleteFinalGradeBtn = document.getElementById("deleteFinalGradeBtn");

if (deleteFinalGradeBtn) {
    deleteFinalGradeBtn.onclick = function() {
        deleteFinalGradeModal.classList.add("show");
    }
}

function closeDeleteFinalGradeModal() {
    deleteFinalGradeModal.classList.remove("show");
}

window.onclick = function(event) {
    if (event.target === addMidtermGradeModal) {
        closeAddMidtermGradeModal();
    }
    if (event.target === addFinalGradeModal) {
        closeAddFinalGradeModal();
    }
    if (event.target === editMidtermGradeModal) {
        closeEditMidtermGradeModal();
    }
    if (event.target === editFinalGradeModal) {
        closeEditFinalGradeModal();
    }
    if (event.target === deleteMidtermGradeModal) {
        closeDeleteMidtermGradeModal();
    }
    if (event.target === deleteFinalGradeModal) {
        closeDeleteFinalGradeModal();
    }
};
