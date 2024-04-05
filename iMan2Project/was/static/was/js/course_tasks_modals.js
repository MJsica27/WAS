let addTaskModal = document.getElementById("addTaskModal");
let addTaskBtn = document.getElementById("btnAddTask");

if (addTaskModal != null && addTaskBtn != null) {
  addTaskBtn.onclick = function() {
    addTaskModal.classList.add("show");
  }
  function closeAddTaskModal() {
    addTaskModal.classList.remove("show");
  }
}

let editTaskModal = document.getElementById("editTaskModal");
let editTaskBtn = document.getElementById("btnEditTask");

if (editTaskModal != null && editTaskBtn != null) {
  editTaskBtn.onclick = function() {
    editTaskModal.classList.add("show");
  }
  function closeEditTaskModal() {
    editTaskModal.classList.remove("show");
  }
}

let completeTaskModal = document.getElementById("completeTaskModal");
let completeTaskBtn = document.getElementById("btnCompleteTask");

if (completeTaskModal != null && completeTaskBtn != null) {
  completeTaskBtn.onclick = function() {
    completeTaskModal.classList.add("show");
  }
  function closeCompleteTaskModal() {
    completeTaskModal.classList.remove("show");
  }
}

let updateTaskScoreModal = document.getElementById("updateTaskScoreModal");
let updateTaskScoreBtn = document.getElementById("btnUpdateTaskScore");

if (updateTaskScoreModal != null && updateTaskScoreBtn != null) {
  updateTaskScoreBtn.onclick = function() {
    updateTaskScoreModal.classList.add("show");
  }
  function closeUpdateTaskScoreModal() {
    updateTaskScoreModal.classList.remove("show");
  }
}

let deleteTaskScoreModal = document.getElementById("deleteTaskScoreModal");
let deleteTaskScoreBtn = document.getElementById("btnDeleteTaskScore");

if (deleteTaskScoreModal != null && deleteTaskScoreBtn != null) {
  deleteTaskScoreBtn.onclick = function() {
    deleteTaskScoreModal.classList.add("show");
  }
  function closeDeleteTaskScoreModal() {
    deleteTaskScoreModal.classList.remove("show");
  }
}

let deleteTaskModal = document.getElementById("deleteTaskModal");
let deleteTaskBtn = document.getElementById("btnDeleteTask");

if (deleteTaskModal != null && deleteTaskBtn != null) {
  deleteTaskBtn.onclick = function() {
    deleteTaskModal.classList.add("show");
  }

  function closeDeleteTaskModal() {
    deleteTaskModal.classList.remove("show");
  }
}

window.onclick = function(event) {
  if (event.target === addTaskModal) {
    closeAddTaskModal();
  }
  if (event.target === editTaskModal) {
    closeEditTaskModal();
  }
  if (event.target === completeTaskModal) {
    closeCompleteTaskModal();
  }
  if (event.target === updateTaskScoreModal) {
    closeUpdateTaskScoreModal();
  }
  if (event.target === deleteTaskScoreModal) {
    closeDeleteTaskScoreModal();
  }
  if (event.target === deleteTaskModal) {
    closeDeleteTaskModal();
  }
}