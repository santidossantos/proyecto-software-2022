/* Cerrar alertas */
setTimeout(function () {
  $(".alertsuccess").addClass("hidesuccess");
  $(".alertsuccess").removeClass("showsuccess");
}, 5000);

setTimeout(function () {
  $(".alerterror").addClass("hideerror");
  $(".alerterror").removeClass("showerror");
}, 5000);

setTimeout(function () {
  $(".alertwarning").addClass("hidewarning");
  $(".alertwarning").removeClass("showwarning");
}, 5000);
// $(".close-btn").click(function () {
//   $(".alert").addClass("hide");
//   $(".alert").removeClass("show");
// });

// const clase = document.querySelector(".close-btn");

// clase.addEventListener("click", () => {
//   $(".alert").removeClass("show");
// });
