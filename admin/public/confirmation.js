const btnDelete = document.querySelectorAll(".deleteconfirm");
const btnActiv = document.querySelectorAll(".activconfirm");
const btnBloquo = document.querySelectorAll(".bloqueoconfirm");

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

if (btnActiv) {
  const btnArrayActiv = Array.from(btnActiv);
  btnArrayActiv.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (!confirm("Esta seguro de querer Bloquear este usuario?")) {
        e.preventDefault();
      }
    });
  });
}

if (btnBloquo) {
  const btnArrayBloqueo = Array.from(btnBloquo);
  btnArrayBloqueo.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (!confirm("Esta seguro de querer Activar este usuario?")) {
        e.preventDefault();
      }
    });
  });
}