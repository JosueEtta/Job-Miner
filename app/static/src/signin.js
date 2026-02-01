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

// Add Skills Functionality
const addSkillsBtn = document.getElementById('add-skills');
const skillsContainer = document.getElementById('skills-container');

if (addSkillsBtn && skillsContainer) {
    // Function to attach remove event listener
    const attachRemoveListener = (removeBtn) => {
        removeBtn.addEventListener('click', function(e) {
            e.preventDefault();
            this.closest('.skill-input-wrapper').remove();
        });
    };
    
    // Attach remove listener to existing remove buttons
    document.querySelectorAll('.remove-skill').forEach(btn => {
        attachRemoveListener(btn);
    });
    
    addSkillsBtn.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Create a new skill input wrapper
        const newSkillWrapper = document.createElement('div');
        newSkillWrapper.className = 'skill-input-wrapper mt-4 relative flex items-center group';
        
        newSkillWrapper.innerHTML = `
            <input type="text" name="skills" class="block w-full py-3 text-gray-700 bg-white border rounded-lg px-2 focus:border-blue-400 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40" placeholder="Skills">
            <button type="button" class="remove-skill ml-2 px-3 py-2 text-sm font-medium text-red-600 bg-red-50 rounded-lg hover:bg-red-100 transition-colors">Remove</button>
        `;
        
        // Add remove functionality to the new skill input
        const removeBtn = newSkillWrapper.querySelector('.remove-skill');
        attachRemoveListener(removeBtn);
        
        // Append the new skill wrapper to the container
        skillsContainer.appendChild(newSkillWrapper);
    });
}

