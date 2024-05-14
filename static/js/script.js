// static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    // Code to run after the document is loaded
    console.log("Website loaded!");

    // Example of event listener for a button (make sure to add your own selectors)
    const someButton = document.querySelector("#some-button");
    if (someButton) {
        someButton.addEventListener("click", function() {
            alert("Button clicked!");
        });
    }
});

// You can expand this file with more complex logic or API calls as needed
