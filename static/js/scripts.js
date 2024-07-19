document.addEventListener("DOMContentLoaded", function() {
    var dropdownButton = document.getElementById("dropdownButton");
    var dropdownMenu = document.getElementById("dropdownMenu");

    dropdownButton.addEventListener("click", function() {
        dropdownMenu.classList.toggle("hidden");
    });
});