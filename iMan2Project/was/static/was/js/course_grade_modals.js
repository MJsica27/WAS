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

window.onclick = function(event) {
    if (event.target === addFinalGradeModal) {
        closeAddFinalGradeModal();
    }
    if (event.target === addMidtermGradeModal) {
        closeAddMidtermGradeModal();
    }
};




//Edit Midterm
// const editMidtermGradeModal = document.getElementById("editMidtermGradeModal");
// const editMidtermGradeBtn = document.getElementById("editMidtermGradeBtn");

// editMidtermGradeBtn.onclick = function() {
//     editMidtermGradeModal.classList.add("show");
// }

// function closeEditMidtermGradeModal() {
//     editMidtermGradeModal.classList.remove("show");
// }

//Edit Final
// const editFinalGradeModal = document.getElementById("editFinalGradeModal");
// const editFinalGradeBtn = document.getElementById("editFinalGradeBtn");

// editFinalGradeBtn.onclick = function() {
//     editFinalGradeModal.classList.add("show");
// }

// function closeEditFinalGradeModal() {
//     editFinalGradeModal.classList.remove("show");
// }

//Delete Midterm
// const deleteMidtermGradeModal = document.getElementById("deleteMidtermGradeModal");
// const deleteMidtermGradeBtn = document.getElementById("deleteMidtermGradeBtn");

// deleteMidtermGradeBtn.onclick = function() {
//     deleteMidtermGradeModal.classList.add("show");
// }

// function closeDeleteMidtermGradeModal() {
//     deleteMidtermGradeModal.classList.remove("show");
// }

//Delete Final
// const deleteFinalGradeModal = document.getElementById("deleteFinalGradeModal");
// const deleteFinalGradeBtn = document.getElementById("deleteFinalGradeBtn");

// deleteFinalGradeBtn.onclick = function() {
//     deleteFinalGradeModal.classList.add("show");
// }

// function closeDeleteFinalGradeModal() {
//     deleteFinalGradeModal.classList.remove("show");
// }
