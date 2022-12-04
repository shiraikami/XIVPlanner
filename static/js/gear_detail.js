"use strict";

const gearid = document.getElementById('gearid')
const url = "http://127.0.0.1:5000/gear/id/" + gearid.innerText;
let acquiredgear;

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

  let weaponbox = document.getElementById('weaponcheck');
  let offhandbox = document.getElementById('offhandcheck')
  let helmetbox = document.getElementById('helmetcheck')
  let bodybox = document.getElementById('bodycheck')
  let glovesbox = document.getElementById('glovescheck')
  let pantsbox = document.getElementById('pantscheck')
  let bootsbox = document.getElementById('bootscheck')
  let earringbox = document.getElementById('earringcheck')
  let necklacebox = document.getElementById('necklacecheck')
  let braceletbox = document.getElementById('braceletcheck')
  let lringbox = document.getElementById('lringcheck')
  let rringbox = document.getElementById('rringcheck')

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
}

//This block of code below is for adding event listeners for each separate gear piece.
//Everytime you check of uncheck it sends a request to the server to add or delete the gear from the database.
let weaponbox = document.getElementById('weaponcheck')

weaponbox.addEventListener('change', async (event) => {
    if(event.currentTarget.checked) {
        let gear = weaponbox.value;
        let checked = true;
        const weaponResponse = await axios.post(url, {
          checked,
          gear
        });
    } else {
        let gear = weaponbox.value;
        let checked = false;
        const weaponResponse = await axios.post(url, {
          checked,
          gear
        });
    }
})

try {
    let offhandbox = document.getElementById('offhandcheck')

    offhandbox.addEventListener('change', async (event) => {
      if (event.currentTarget.checked) {
        let gear = offhandbox.value;
        let checked = true;
        const offhandResponse = await axios.post(url, {
          checked,
          gear
        });
        
    } else {
        let gear = offhandbox.value;
        let checked = false;
        const offhandResponse = await axios.post(url, {
          checked,
          gear
        });
    }
    })
}
catch {

}

let helmetbox = document.getElementById('helmetcheck')

helmetbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = helmetbox.value;
    let checked = true;
    const helmetResponse = await axios.post(url, {
      checked,
      gear
    });
} else {
    let gear = helmetbox.value;
    let checked = false;
    const helmetResponse = await axios.post(url, {
      checked,
      gear
    });
}
})

let bodybox = document.getElementById('bodycheck')

bodybox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = bodybox.value;
    let checked = true;
    const bodyResponse = await axios.post(url, {
      checked,
      gear
    });
} else {
    let gear = bodybox.value;
    let checked = false;
    const bodyResponse = await axios.post(url, {
      checked,
      gear
    });
}
})

let glovesbox = document.getElementById('glovescheck')

glovesbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = glovesbox.value;
    let checked = true;
    const glovesResponse = await axios.post(url, {
      checked,
      gear
    });
} else {
    let gear = glovesbox.value;
    let checked = false;
    const glovesResponse = await axios.post(url, {
      checked,
      gear
    });
}
})

let pantsbox = document.getElementById('pantscheck')

pantsbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = pantsbox.value;
    let checked = true;
    const pantsResponse = await axios.post(url, {
      checked,
      gear
    });
} else {
    let gear = pantsbox.value;
    let checked = false;
    const pantsResponse = await axios.post(url, {
      checked,
      gear
    });
}
})

let bootsbox = document.getElementById('bootscheck')

bootsbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = bootsbox.value;
    let checked = true;
    const bootsResponse = await axios.post(url, {
      checked,
      gear
    });
} else {
    let gear = bootsbox.value;
    let checked = false;
    const bootsResponse = await axios.post(url, {
      checked,
      gear
    });
}
})

let earringbox = document.getElementById('earringcheck')

earringbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = earringbox.value;
    let checked = true;
    const earringResponse = await axios.post(url, {
      checked,
      gear
    });
} else {
    let gear = earringbox.value;
    let checked = false;
    const earringResponse = await axios.post(url, {
      checked,
      gear
    });
}
})

let necklacebox = document.getElementById('necklacecheck')

necklacebox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = necklacebox.value;
    let checked = true;
    const necklaceResponse = await axios.post(url, {
      checked,
      gear
    });
} else {
    let gear = necklacebox.value;
    let checked = false;
    const necklaceResponse = await axios.post(url, {
      checked,
      gear
    });
}
})

let braceletbox = document.getElementById('braceletcheck')

braceletbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = braceletbox.value;
    let checked = true;
    const braceletResponse = await axios.post(url, {
      checked,
      gear
    });
} else {
    let gear = braceletbox.value;
    let checked = false;
    const braceletResponse = await axios.post(url, {
      checked,
      gear
    });
}
})

let lringbox = document.getElementById('lringcheck')

lringbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = lringbox.value;
    let checked = true;
    const lringResponse = await axios.post(url, {
      checked,
      gear
    });
} else {
    let gear = lringbox.value;
    let checked = false;
    const lringResponse = await axios.post(url, {
      checked,
      gear
    });
}
})

let rringbox = document.getElementById('rringcheck')

rringbox.addEventListener('change', async (event) => {
  if (event.currentTarget.checked) {
    let gear = rringbox.value;
    let checked = true;
    const rringResponse = await axios.post(url, {
      checked,
      gear
    });
} else {
    let gear = rringbox.value;
    let checked = false;
    const rringResponse = await axios.post(url, {
      checked,
      gear
    });
}
})