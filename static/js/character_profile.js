"user strict;"

let url = "https://xivapi.com/character/";

window.onload = async (evt) => {
    url = url + document.getElementById('char-id').innerText;
    await requestCharacter(url);
};

async function requestCharacter(url) {
    let res = await axios.get(url);

    document.getElementById("character-thumbnail").src=res.data.Character.Avatar;
    document.getElementById("character-name").innerText = res.data.Character.Name;
    document.getElementById("character-server").innerText = res.data.Character.Server;
    document.getElementById("character-portrait").src=res.data.Character.Portrait;
    console.log(res.data);
}
