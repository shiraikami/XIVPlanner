"use strict";

const gearid = document.getElementById('gearid')
const url = "http://127.0.0.1:5000/gearset/id/" + gearid.innerText;
let acquiredgear;
const weaponbox = document.getElementById('weaponcheck');
const offhandbox = document.getElementById('offhandcheck')
const helmetbox = document.getElementById('helmetcheck')
const bodybox = document.getElementById('bodycheck')
const glovesbox = document.getElementById('glovescheck')
const pantsbox = document.getElementById('pantscheck')
const bootsbox = document.getElementById('bootscheck')
const earringbox = document.getElementById('earringcheck')
const necklacebox = document.getElementById('necklacecheck')
const braceletbox = document.getElementById('braceletcheck')
const lringbox = document.getElementById('lringcheck')
const rringbox = document.getElementById('rringcheck')

//If there is no gear, request acquiredgear from the server and save it to "gear"
window.onload = (evt) => {
  if(!acquiredgear) {
    requestGear()
  }
};

async function mapGear(url) {
  let res = await axios.get(url);

  return res.data.map(data => {
    return {
      gear_id: data.gear_id,
      gearset_id: data.gearset_id,
      user_id: data.user_id
    }
  })
}

async function requestGear() {
  acquiredgear = await mapGear('http://127.0.0.1:5000/api/acquiredgear')

  for(let gear of acquiredgear) {
    if(parseInt(gear.gear_id) == parseInt(weaponbox.value)) {
      weaponbox.checked = true;
    } 

    try {
      if(parseInt(gear.gear_id) == parseInt(offhandbox.value)) {
        offhandbox.checked = true;
      }
    } catch {}

    if(parseInt(gear.gear_id) == parseInt(helmetbox.value)) {
      helmetbox.checked = true;
    }

    if(parseInt(gear.gear_id) == parseInt(bodybox.value)) {
      bodybox.checked = true;
    }

    if(parseInt(gear.gear_id) == parseInt(glovesbox.value)) {
      glovesbox.checked = true;
    }

    if(parseInt(gear.gear_id) == parseInt(pantsbox.value)) {
      pantsbox.checked = true;
    }

    if(parseInt(gear.gear_id) == parseInt(bootsbox.value)) {
      bootsbox.checked = true;
    }

    if(parseInt(gear.gear_id) == parseInt(earringbox.value)) {
      earringbox.checked = true;
    }

    if(parseInt(gear.gear_id) == parseInt(necklacebox.value)) {
      necklacebox.checked = true;
    }

    if(parseInt(gear.gear_id) == parseInt(braceletbox.value)) {
      braceletbox.checked = true;
    }

    if(parseInt(gear.gear_id) == parseInt(lringbox.value)) {
      lringbox.checked = true;
    }

    if(parseInt(gear.gear_id) == parseInt(rringbox.value)) {
      rringbox.checked = true;
    }
  }
  updateRaidList();
}

function updateRaidList() {
  if(weaponbox.checked == true) {
    if(document.getElementById('weapon-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("weapon").style.display = "none";
    } else {
      document.getElementById("weapon-twine").style.display = "none"
    }
  } else {
    if(document.getElementById('weapon-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("weapon").style.display = "block";
    }
    else {
      document.getElementById("weapon-twine").style.display = "block"
    }
  }

  try {
    if(offhandbox.checked == true) {
      if(document.getElementById('offhand-name').innerText.indexOf("Augmented") == -1) {
        document.getElementById("offhand").style.display = "none";
      } else {
        document.getElementById("offhand-twine").style.display = "none";
      }
    }
    else {
      if(document.getElementById('offhand-name').innerText.indexOf("Augmented") == -1) {
        document.getElementById("offhand").style.display = "block";
      } else {
        document.getElementById("offhand-twine").style.display = "block";
      }
    }
  } catch {}
 
  if(helmetbox.checked == true) {
    if(document.getElementById('helmet-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("helmet").style.display = "none";
      document.getElementById("helmet2").style.display = "none";
    }
    else {
      document.getElementById("helmet-twine").style.display = "none";
    }
  } else {
    if(document.getElementById('helmet-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("helmet").style.display = "block";
      document.getElementById("helmet2").style.display = "block";
    }
    else {
      document.getElementById("helmet-twine").style.display = "block";
    }
  }

  if(bodybox.checked == true) {
    if(document.getElementById('body-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("body").style.display = "none";
    }
    else {
      document.getElementById("body-twine").style.display = "none";
    }
  }
  else {
    if(document.getElementById('body-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("body").style.display = "block";
    }
    else {
      document.getElementById("body-twine").style.display = "block";
    }
  }

  if(glovesbox.checked == true) {
    if(document.getElementById('gloves-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("gloves").style.display = "none";
      document.getElementById("gloves2").style.display = "none";
    }
    else {
      document.getElementById("gloves-twine").style.display = "none";
    }
  }
  else {
    if(document.getElementById('gloves-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("gloves").style.display = "block";
      document.getElementById("gloves2").style.display = "block";
    }
    else {
      document.getElementById("gloves-twine").style.display = "block";
    }
  }

  if(pantsbox.checked == true) {
    if(document.getElementById('pants-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("pants").style.display = "none";
    } 
    else {
      document.getElementById("pants-twine").style.display = "none";
    }
  }
  else {
    if(document.getElementById('pants-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("pants").style.display = "block";
    } 
    else {
      document.getElementById("pants-twine").style.display = "block";
    }
  }

  if(bootsbox.checked == true) {
    if(document.getElementById('boots-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("boots").style.display = "none";
      document.getElementById("boots2").style.display = "none";
    }
    else {
      document.getElementById("boots-twine").style.display = "none";
    }
  }
  else {
    if(document.getElementById('boots-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("boots").style.display = "block";
      document.getElementById("boots2").style.display = "block";
    }
    else {
      document.getElementById("boots-twine").style.display = "block";
    }
  }

  if(earringbox.checked == true) {
    if(document.getElementById('earring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("earrings").style.display = "none";
    }
    else {
      document.getElementById("earrings-shine").style.display = "none";
    }
  } 
  else {
    if(document.getElementById('earring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("earrings").style.display = "block";
    }
    else {
      document.getElementById("earrings-shine").style.display = "block";
    }
  }

  if(necklacebox.checked == true) {
    if(document.getElementById('necklace-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("necklace").style.display = "none";
    }
    else {
      document.getElementById("necklace-shine").style.display = "none";
    }
  } 
  else {
    if(document.getElementById('necklace-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("necklace").style.display = "block";
    }
    else {
      document.getElementById("necklace-shine").style.display = "block";
    }
  }

  if(braceletbox.checked == true) {
    if(document.getElementById('bracelet-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("bracelet").style.display = "none";
    }
    else {
      document.getElementById("bracelet-shine").style.display = "none";
    }
  } 
  else {
    if(document.getElementById('bracelet-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("bracelet").style.display = "block";
    }
    else {
      document.getElementById("bracelet-shine").style.display = "block";
    }
  }

  if(lringbox.checked == true) {
    if(document.getElementById('lring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("lring").style.display = "none";
    }
    else {
      document.getElementById("lring-shine").style.display = "none";
    }
  } 
  else {
    if(document.getElementById('lring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("lring").style.display = "block";
    }
    else {
      document.getElementById("lring-shine").style.display = "block";
    }
  }

  if(rringbox.checked == true) {
    if(document.getElementById('rring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("rring").style.display = "none";
    }
    else {
      document.getElementById("rring-shine").style.display = "none";
    }
  } 
  else {
    if(document.getElementById('rring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("rring").style.display = "block";
    }
    else {
      document.getElementById("rring-shine").style.display = "block";
    }
  }
}

//This block of code below is for adding event listeners for each separate gear piece.
//Everytime you check of uncheck it sends a request to the server to add or delete the gear from the database.

weaponbox.addEventListener('change', async (event) => {
    if(event.currentTarget.checked) {
        let gear = weaponbox.value;
        let checked = true;
        const weaponResponse = await axios.post(url, {
          checked,
          gear
        });
        if(document.getElementById('weapon-name').innerText.indexOf("Augmented") == -1) {
          document.getElementById("weapon").style.display = "none";
        } else {
          document.getElementById("weapon-twine").style.display = "none";
        }
    } else {
        let gear = weaponbox.value;
        let checked = false;
        const weaponResponse = await axios.post(url, {
          checked,
          gear
        });
        if(document.getElementById('weapon-name').innerText.indexOf("Augmented") == -1) {
          document.getElementById("weapon").style.display = "block";
        } else {
          document.getElementById("weapon-twine").style.display = "block";
        }
    }
})

try {

    offhandbox.addEventListener('change', async (event) => {
      if (event.currentTarget.checked) {
        let gear = offhandbox.value;
        let checked = true;
        const offhandResponse = await axios.post(url, {
          checked,
          gear
        });
        if(document.getElementById('offhand-name').innerText.indexOf("Augmented") == -1) {
          document.getElementById("offhand").style.display = "none";
        } else {
          document.getElementById("offhand-twine").style.display = "none";
        }
    } else {
        let gear = offhandbox.value;
        let checked = false;
        const offhandResponse = await axios.post(url, {
          checked,
          gear
        });
        if(document.getElementById('offhand-name').innerText.indexOf("Augmented") == -1) {
          document.getElementById("offhand").style.display = "block";
        } else {
          document.getElementById("offhand-twine").style.display = "block";
        }
    }
  })
}
catch {

}

helmetbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = helmetbox.value;
    let checked = true;
    const helmetResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('helmet-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("helmet").style.display = "none";
      document.getElementById("helmet2").style.display = "none";
    }
    else {
      document.getElementById("helmet-twine").style.display = "none";
    }
  } else {
    let gear = helmetbox.value;
    let checked = false;
    const helmetResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('helmet-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("helmet").style.display = "block";
      document.getElementById("helmet2").style.display = "block";
    }else {
      document.getElementById("helmet-twine").style.display = "block";
    }
  }
})

bodybox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = bodybox.value;
    let checked = true;
    const bodyResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('body-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("body").style.display = "none";
    }
    else {
      document.getElementById("body-twine").style.display = "none";
    }
  } else {
    let gear = bodybox.value;
    let checked = false;
    const bodyResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('body-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("body").style.display = "block";
    }
    else {
      document.getElementById("body-twine").style.display = "block";
    }
  }
})

glovesbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = glovesbox.value;
    let checked = true;
    const glovesResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('gloves-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("gloves").style.display = "none";
      document.getElementById("gloves2").style.display = "none";
    }
    else {
      document.getElementById("gloves-twine").style.display = "none";
    }
  } else {
    let gear = glovesbox.value;
    let checked = false;
    const glovesResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('gloves-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("gloves").style.display = "block";
      document.getElementById("gloves2").style.display = "block";
    }
    else {
      document.getElementById("gloves-twine").style.display = "block";
    }
  }
})

pantsbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = pantsbox.value;
    let checked = true;
    const pantsResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('pants-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("pants").style.display = "none";
    }
    else {
      document.getElementById("pants-twine").style.display = "none";
    }
  } else {
    let gear = pantsbox.value;
    let checked = false;
    const pantsResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('pants-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("pants").style.display = "block";
    }
    else {
      document.getElementById("pants-twine").style.display = "block";
    }
  }
})

bootsbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = bootsbox.value;
    let checked = true;
    const bootsResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('boots-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("boots").style.display = "none";
      document.getElementById("boots2").style.display = "none";
    }
    else {
      document.getElementById("boots-twine").style.display = "none";
    }
  } else {
    let gear = bootsbox.value;
    let checked = false;
    const bootsResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('boots-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("boots").style.display = "block";
      document.getElementById("boots2").style.display = "block";
    }
    else {
      document.getElementById("boots-twine").style.display = "block";
    }
  }
})

earringbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = earringbox.value;
    let checked = true;
    const earringResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('earring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("earrings").style.display = "none";
    }
    else {
      document.getElementById("earrings-shine").style.display = "none";
    }
  } else {
    let gear = earringbox.value;
    let checked = false;
    const earringResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('earring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("earrings").style.display = "block";
    }
    else {
      document.getElementById("earrings-shine").style.display = "block";
    }
  }
})

necklacebox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = necklacebox.value;
    let checked = true;
    const necklaceResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('necklace-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("necklace").style.display = "none";
    }
    else {
      document.getElementById("necklace-shine").style.display = "none";
    }
  } else {
    let gear = necklacebox.value;
    let checked = false;
    const necklaceResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('necklace-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("necklace").style.display = "block";
    }
    else {
      document.getElementById("necklace-shine").style.display = "block";
    }
  }
})

braceletbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = braceletbox.value;
    let checked = true;
    const braceletResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('bracelet-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("bracelet").style.display = "none";
    }
    else {
      document.getElementById("bracelet-shine").style.display = "none";
    }
  } else {
    let gear = braceletbox.value;
    let checked = false;
    const braceletResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('bracelet-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("bracelet").style.display = "block";
    }
    else {
      document.getElementById("bracelet-shine").style.display = "block";
    }
  }
})

lringbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = lringbox.value;
    let checked = true;
    if(rringbox.value == lringbox.value) {
      if(rringbox.checked == false) 
        rringbox.checked = true;
    }
    const lringResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('lring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("lring").style.display = "none";
    }
    else {
      document.getElementById("lring-shine").style.display = "none";
    }
  } else {
    let gear = lringbox.value;
    let checked = false;
    if(rringbox.value == lringbox.value) {
      if(rringbox.checked == true)
        rringbox.checked = false
    }
    const lringResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('lring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("lring").style.display = "block";
    }
    else {
      document.getElementById("lring-shine").style.display = "block";
    }
  }
})

rringbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = rringbox.value;
    let checked = true;
    if(lringbox.value == rringbox.value) {
      if(lringbox.checked == false) 
        lringbox.checked = true;
    }
    const rringResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('rring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("rring").style.display = "none";
    }
    else {
      document.getElementById("rring-shine").style.display = "none";
    }
  } else {
    let gear = rringbox.value;
    let checked = false;
    if(lringbox.value == rringbox.value) {
      if(lringbox.checked == true) 
        lringbox.checked = false;
    }
    const rringResponse = await axios.post(url, {
      checked,
      gear
    });
    if(document.getElementById('rring-name').innerText.indexOf("Augmented") == -1) {
      document.getElementById("rring").style.display = "block";
    }
    else {
      document.getElementById("rring-shine").style.display = "block";
    }
  }
})