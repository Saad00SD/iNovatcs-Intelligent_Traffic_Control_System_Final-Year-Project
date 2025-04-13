document.addEventListener("DOMContentLoaded", function () {
    const usernameField = document.querySelector("#usernameField");
    const feedBackArea = usernameField.nextElementSibling; // Selects the next sibling (.invalid-feedback)

    usernameField.addEventListener("keyup", (e) => {
        const usernameVal = e.target.value.trim();

        usernameField.classList.remove("is-invalid");
        feedBackArea.style.display = "none";
        feedBackArea.innerHTML = "";

        if (usernameVal.length > 0) {
            fetch("/users/validate-username/", {  // Ensure correct endpoint
                body: JSON.stringify({ username: usernameVal }),
                method: "POST",
                headers: { "Content-Type": "application/json" },
            })
                .then((res) => res.json())
                .then((data) => {
                    if (data.username_error) {
                        usernameField.classList.add("is-invalid");
                        feedBackArea.style.display = "block";
                        feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
                    }
                })
                .catch((error) => console.error("Error:", error));
        }
    });
});
