"use strict";

let gears;

window.onload = (event) => {
  if(!gears) {
    requestGear()
  }
};

async function mapGear(url) {
  let res = await axios.get(url);

  return res.data.map(data => {
    return {
      id: data.id,
      name: data.name,
      url: data.url,
      ilevel: data.ilevel,
      icon: data.icon,
      classjob: data.classjob,
      equipslot: data.equipslot
    }
  })
}

async function requestGear() {
  gears = await mapGear('http://127.0.0.1:5000/api/gear')
}

$('#JobSelect').change(function(evt) {
  $("#WeaponSelect").empty()
  $("#OffhandSelect").empty()
  $("#HelmetSelect").empty()
  $("#BodySelect").empty()
  $("#GlovesSelect").empty()
  $("#PantsSelect").empty()
  $("#BootsSelect").empty()
  $("#EarringSelect").empty()
  $("#NecklaceSelect").empty()
  $("#BraceletSelect").empty()
  $("#LRingSelect").empty()
  $("#RRingSelect").empty()

  let selected = $('#JobSelect').find(":selected").val();
  for(let gear of gears) {
    if(gear.classjob.includes(selected)) {
      if(gear.equipslot == 1 || gear.equipslot == 13) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#WeaponSelect").append(option)
      }
      if(gear.equipslot == 2) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#OffhandSelect").append(option)
      }
      if(gear.equipslot == 3) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#HelmetSelect").append(option)
      }
      if(gear.equipslot == 4) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#BodySelect").append(option)
      }
      if(gear.equipslot == 5) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#GlovesSelect").append(option)
      }
      if(gear.equipslot == 7) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#PantsSelect").append(option)
      }
      if(gear.equipslot == 8) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#BootsSelect").append(option)
      }
      if(gear.equipslot == 9) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#EarringSelect").append(option)
      }
      if(gear.equipslot == 10) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#NecklaceSelect").append(option)
      }
      if(gear.equipslot == 11) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#BraceletSelect").append(option)
      }
      if(gear.equipslot == 12) {
        let option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#LRingSelect").append(option)
        option = $('<option></option>').attr("value", gear.id).text(gear.name)
        $("#RRingSelect").append(option)
      }
    }
  }
});

$('#WeaponSelect').change(function(evt) {
  alert('Changed Weapon');
});