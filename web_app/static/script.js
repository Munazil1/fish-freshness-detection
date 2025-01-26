// script.js

document.getElementById('fileInput').onchange = function (event) {
    // Preview selected file (optional)
    const file = event.target.files[0];
    if (file) {
        console.log("File selected:", file.name);
    }
};
