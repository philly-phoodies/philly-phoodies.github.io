var $ = function (id) {
  console.log("hello");
 return document.getElementById(id);
}

var enter_click = function () {
  var searchEntry = $("searchEntry").value;
  var price = $("price").value;
  var distance = $("distance").value;
  alert (searchEntry);
  alert (price);
  alert (distance);
  window.location="./searchResults.html";

  if ( searchEntry == Pizza || pizza) {
    window.location="https://www.google.com";
  }
}
window.onload = function () {
  $("enter").onclick = enter_click;
}
