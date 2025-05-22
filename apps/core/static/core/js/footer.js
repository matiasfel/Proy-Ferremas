/* Script para año de footer */
document.addEventListener('DOMContentLoaded', () => {
    const yearElements = document.querySelectorAll('#year');
    const currentYear = new Date().getFullYear();
    yearElements.forEach(element => {
        element.textContent = currentYear;
    });
});