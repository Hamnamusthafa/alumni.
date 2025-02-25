<script>
    document.addEventListener("DOMContentLoaded", function () {
        document.querySelector("form").addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent actual form submission

            // Show success alert
            alert("The request has been sent!");

            // Reset the form after submission
            document.querySelector("form").reset();
        });
    });
</script>
