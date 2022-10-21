/* Cerrar alertas */

setTimeout(function () {
  $(".alertsuccess").removeClass("showsuccess");
  $(".alertsuccess").addClass("hidesuccess");
}, 5000);

setTimeout(function () {
  $(".alerterror").addClass("hideerror");
  $(".alerterror").removeClass("showerror");
}, 5000);

setTimeout(function () {
  $(".alertwarning").addClass("hidewarning");
  $(".alertwarning").removeClass("showwarning");
}, 5000);

setTimeout(function () {
  $(".alertsuccess").addClass("display");
}, 6000);

setTimeout(function () {
  $(".alerterror").addClass("display");
}, 6000);