"user strict;"

let url = "https://xivapi.com/character/search?name=";
let data = [];

window.onload = async (evt) => {
    url = url + document.getElementById('term').innerText;
    await searchCharacter({url: url, page:0});
};

function customizer(objValue, srcValue) {
  if (_.isArray(objValue)) {
      return objValue.concat(srcValue);
  }
}

async function searchCharacter({url, page}) {
    page++;

    let res = await axios.get(url + "&page=" + page.toString());

    for(character of res.data.Results) {
      data.push(character)
    }

    if(res.data.Pagination.PageNext != null) {
      searchCharacter({url:url, page: page});
    } else {
      listCharacters();
    }
}

function listCharacters() {
    document.getElementById("loader").style.display = "none";
    let index = 0;
    let row;
    let charList = document.getElementById('characterList');

    for(character of data) {
      if(index == 0 || index % 3 == 0) {
        let rowDiv = document.createElement("div");
        rowDiv.setAttribute("class", "row");

        let charDiv = document.createElement("div");
        charDiv.innerText = character.Name;
        charDiv.setAttribute("class", "col-2 border border-end-0");
        charDiv.style.fontSize = "13px";

        let serverDiv = document.createElement("div");
        serverDiv.innerText = character.Lang + " - " + character.Server;
        serverDiv.setAttribute("class", "col border border-start-0");
        serverDiv.style.fontSize = "12px";

        rowDiv.append(charDiv)
        rowDiv.append(serverDiv)
        charList.append(rowDiv);
        row = rowDiv;
        index++;
      } 
      else {
        let charDiv = document.createElement("div");
        charDiv.innerText = character.Name;
        charDiv.setAttribute("class", "col-2 border border-end-0");
        charDiv.style.fontSize = "13px";

        let serverDiv = document.createElement("div");
        serverDiv.innerText = character.Lang + " - " + character.Server;
        serverDiv.setAttribute("class", "col border border-start-0");
        serverDiv.style.fontSize = "12px";

        row.append(charDiv);
        row.append(serverDiv);
        index++;
      }
    }
}
