// 🌙 THEME TOGGLE
const toggleBtn = document.getElementById("themeToggle");

if (toggleBtn) {
    toggleBtn.onclick = () => {
        const html = document.documentElement;
        const current = html.getAttribute("data-theme");

        if (current === "dark") {
            html.setAttribute("data-theme", "light");
            localStorage.setItem("theme", "light");
        } else {
            html.setAttribute("data-theme", "dark");
            localStorage.setItem("theme", "dark");
        }
    };
}

// LOAD SAVED THEME
const savedTheme = localStorage.getItem("theme");
if (savedTheme) {
    document.documentElement.setAttribute("data-theme", savedTheme);
}

// 🔥 TOAST
function showToast(msg) {
    const toast = document.getElementById("toast");
    toast.textContent = msg;
    toast.classList.remove("hidden");

    setTimeout(() => {
        toast.classList.add("hidden");
    }, 3000);
}

// 🔥 LOADER
function showLoader() {
    document.getElementById("loader").classList.remove("hidden");
}

function hideLoader() {
    document.getElementById("loader").classList.add("hidden");
}
