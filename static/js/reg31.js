/*document.getElementById("signupForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Fetch form data
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;
    let password = document.getElementById("password").value;
    let role = document.getElementById("role").value;
    let academicYear = document.getElementById("academicYear").value;

    // Basic validation
    if (!name || !email || !phone || !password || !role || !academicYear) {
        alert("Please fill in all fields.");
        return;
    }

    // Simulate successful registration (Replace this with actual backend authentication logic)
    setTimeout(() => {
        alert("Registration successful! Redirecting to home page...");
        window.location.href = "home.html"; // Redirect to home page
    }, 1000);
});*/







document.getElementById("signupForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        password: document.getElementById("password").value,
        role: document.getElementById("role").value,
        academicYear: document.getElementById("academicYear").value,
    };

    const response = await fetch("http://127.0.0.1:5000/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
    });

    const result = await response.json();
    alert(result.message);

    if (response.ok) {
        window.location.href = "enter_otp.html";
    }
});





