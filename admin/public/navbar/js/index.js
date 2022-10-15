const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-menu");
const clase = document.querySelector(".dropdown-container");
const btnDelete = document.querySelectorAll(".deleteconfirm");

navToggle.addEventListener("click", () => {
  navMenu.classList.toggle("nav-menu_visible");

  if (navMenu.classList.contains("nav-menu_visible")) {
    navToggle.setAttribute("aria-label", "Cerrar menú");
  } else {
    navToggle.setAttribute("aria-label", "Abrir menú");
  }
});

clase.addEventListener("click", () => {
  document.querySelector(".dropdown-container ul").classList.toggle("show");
});

if (btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (!confirm("Esta seguro de querer eliminar este usuario?")) {
        e.preventDefault();
      }
    });
  });
}
