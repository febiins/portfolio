const togglebtn = document.getElementById("themeToggle");
const body = document.body

if(localStorage.getItem("theme")=="dark"){
    body.classList.add("dark-mode");
    togglebtn.textContent="☀️ Light";
}

togglebtn.addEventListener("click",()=>{
    body.classList.toggle("dark-mode");
    if (body.classList.contains("dark-mode")) {
        toggleBtn.textContent = "☀️ Light";
        localStorage.setItem("theme", "dark");
    } else {
        toggleBtn.textContent = "🌙 Dark";
        localStorage.setItem("theme", "light");
    }
});