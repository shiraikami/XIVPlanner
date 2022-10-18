"use strict";

$('#JobSelect').change(function(evt) {
  var selected = $('#JobSelect').find(":selected").val();
  
});

$("#WeaponSelect").change(function(evt) {
  var selected = $('#WeaponSelect').find(":selected").val();
  alert(selected);
  console.log(selected);
});