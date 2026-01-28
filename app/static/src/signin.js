// // signin.js

// let findJobBtn = document.getElementById("find-job");
// let postJobBtn = document.getElementById("post-job");
// let findJobForm = document.getElementById("find-job-form");
// let postJobForm = document.getElementById("post-job-form");
// let catchText = document.getElementById("catch-text");


// findJobBtn.addEventListener("click",()=>{
//     postJobForm.style.display = "none";
//     postJobBtn.style.borderBottomColor = "oklch(55.1% 0.027 264.364)";
//     findJobForm.style.display = "block";
//     // postJobBtn.classList.remove("border-b-blue-500");
//     // findJobBtn.classList.add("border-b-blue-500");
//     findJobBtn.style.borderBottomColor = " oklch(62.3% 0.214 259.815)"
//     catchText.textContent = "Start mining your next carrer gem."
// });

// postJobBtn.addEventListener("click",()=>{
//     findJobForm.style.display = "none";
//     findJobBtn.style.borderBottomColor = "oklch(55.1% 0.027 264.364)";
//     postJobForm.style.display = "block";
//     // findJobBtn.classList.rem("border-b-blue-500");
//     // postJobBtn.classList.add("border-b-blue-500");
//     postJobBtn.style.borderBottomColor = " oklch(62.3% 0.214 259.815)"
//     catchText.textContent = "Mine the gems your team is missing."
// });


  let uploadedImage = null;

        document.getElementById('dropzone-file').addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                document.getElementById('fileName').textContent = `Selected: ${file.name}`;
                const reader = new FileReader();
                reader.onload = function(event) {
                    uploadedImage = event.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
