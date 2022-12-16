"user strict;"

let url = "https://xivapi.com/character/search?name=";

window.onload = async (evt) => {
    url = url + document.getElementById('term').innerText;
    await searchCharacter(url);
};

async function searchCharacter(url) {
    let res = await axios.get(url);
    console.log(res);
    data = [];

    for(character of res.data.Results) {
      data.push(character);
    }

    listCharacters(data);

    $('#list-pagination').twbsPagination({
      totalPages: res.data.Pagination.PageTotal,
      visiblePages: 3,
      onPageClick: async function (event, page) {
          data = [];
          let res = await axios.get(url + "&page=" + page.toString());
    
          for(character of res.data.Results) {
            data.push(character);
          }
    
          listCharacters(data);
      }
    });

    // if(res.data.Pagination.PageNext != null) {
    //   searchCharacter({url:url, page: page});
    // } else {
    //   listCharacters();
    // }
}

function listCharacters(data) {
    $('#characterList').empty();
    document.getElementById("spinner").style.display = "none";
    let index = 0;
    let row;
    let charList = document.getElementById('characterList');


    for(character of data) {
      if(index == 0 || index % 3 == 0) {
        let rowDiv = document.createElement("div");
        rowDiv.setAttribute("class", "row");

        let charDiv = document.createElement("div");
        charDiv.setAttribute("class", "col-2 border border-end-0");
        charDiv.style.fontSize = "13px";

        let anchor = document.createElement("a");
        anchor.innerText = character.Name;
        anchor.setAttribute("href", `/character/id/${character.ID}`);

        let serverDiv = document.createElement("div");
        serverDiv.innerText = character.Lang + " - " + character.Server;
        serverDiv.setAttribute("class", "col-2 border border-start-0 text-end");
        serverDiv.style.fontSize = "12px";

        charDiv.append(anchor);
        rowDiv.append(charDiv);
        rowDiv.append(serverDiv);
        charList.append(rowDiv);
        row = rowDiv;
        index++;
      } 
      else {
        let charDiv = document.createElement("div");
        charDiv.setAttribute("class", "col-2 border border-end-0");
        charDiv.style.fontSize = "13px";

        let anchor = document.createElement("a");
        anchor.innerText = character.Name;
        anchor.setAttribute("href", `/character/id/${character.ID}`);

        let serverDiv = document.createElement("div");
        serverDiv.innerText = character.Lang + " - " + character.Server;
        serverDiv.setAttribute("class", "col-2 border border-start-0 text-end");
        serverDiv.style.fontSize = "12px";

        charDiv.append(anchor);
        row.append(charDiv);
        row.append(serverDiv);
        index++;
      }
    }
}
