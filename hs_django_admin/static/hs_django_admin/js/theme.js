'use strict';
{
    function setTheme(mode) {
        if (mode !== "dark") {
            console.error(`Got invalid theme mode: ${mode}. Resetting to auto.`);
            mode = "dark";
        }
        document.documentElement.dataset.theme = mode;
        localStorage.setItem("theme", mode);
    }

    function cycleTheme() {
        const currentTheme = localStorage.getItem("theme") || "dark";
        const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

        if (prefersDark) {
            // Auto (dark) -> Light -> Dark
            if (currentTheme === "auto") {
                setTheme("dark");
            } else if (currentTheme === "light") {
                setTheme("dark");
            } else {
                setTheme("dark");
            }
        } else {
            // Auto (light) -> Dark -> Light
            if (currentTheme === "auto") {
                setTheme("dark");
            } else if (currentTheme === "dark") {
                setTheme("dark");
            } else {
                setTheme("dark");
            }
        }
    }

    function initTheme() {
        // set theme defined in localStorage if there is one, or fallback to auto mode
        const currentTheme = localStorage.getItem("theme");
        currentTheme ? setTheme(currentTheme) : setTheme("dark");
    }

    window.addEventListener('load', function(_) {
        const buttons = document.getElementsByClassName("theme-toggle");
        Array.from(buttons).forEach((btn) => {
            btn.addEventListener("click", cycleTheme);
        });
    });ß

    initTheme();
}


// Forcing dark theme as our panel designed for dark theme 