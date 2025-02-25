document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("form").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission

        // Get input values
        let skills = document.getElementById("skills").value.trim();
        let achievements = document.getElementById("achievements").value.trim();
        let description = document.getElementById("description").value.trim();

        // Validation: Ensure required fields are filled
        if (!skills || !achievements || !description) {
            alert("Please fill in all required fields.");
            return;
        }

        // Show success alert
        alert("Your profile has been updated successfully!");

        // Uncomment below if you want to redirect after update
        // window.location.href = "home.html";
    });
});
