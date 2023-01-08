"user strict;"

let url = "https://xivapi.com/character/";
let access_token = ""

window.onload = async (evt) => {
    const token = await axios.get("http://127.0.0.1:5000/search/token");
    access_token = token.data.access_token;
    url = url + document.getElementById('char-id').innerText;
    await requestCharacter(url);
};

async function requestCharacter(url) {
    let res = await axios.get(url);

    let serverRegion = "";
    if(res.data.Character.DC == "Aether" || res.data.Character.DC == "Primal" || res.data.Character.DC == "Crystal") {
        serverRegion = "NA";
    } 
    else if(res.data.Character.DC == "Chaos" || res.data.Character.DC == "Light") {
        serverRegion = "EU";
    }
    else {
        serverRegion = "JP";
    }

    let serverSlug = res.data.Character.Server

    document.getElementById("character-thumbnail").src=res.data.Character.Avatar;
    document.getElementById("character-name").innerText = res.data.Character.Name;
    document.getElementById("name").value = res.data.Character.Name;
    document.getElementById("character-server").innerText = res.data.Character.Server;
    document.getElementById("character-portrait").src=res.data.Character.Portrait;

    data = await axios({
        url: "https://www.fflogs.com/api/v2/client",
        method: 'POST',
        headers: { Authorization: `Bearer ${access_token}`, Content_Type: 'application/json' },
        data: {
            query: `query($name: String, $serverSlug: String, $serverRegion: String) {
                        characterData {
                            character(name: $name, serverSlug: $serverSlug, serverRegion: $serverRegion) {
                                zoneRankings
                            }
                        }
                    }`, variables: { name: res.data.Character.Name, serverSlug: serverSlug, serverRegion: serverRegion }
        }
    });

    if(!data) {
        $("#fflogs-container").hide();
    }

    let rankings = await data.data.data.characterData.character.zoneRankings.rankings;
    console.log(data);
    console.log(rankings);
 
    for (let i = 0; i < rankings.length; i++) {

        $(`#boss${i+1}-name`).text(rankings[i].encounter.name);

        let bestrank = String(Math.floor(rankings[i].rankPercent))
        if(bestrank < 25)
            $(`#boss${i+1}-rank`).text(bestrank + " - " + rankings[i].spec).css("color", "gray");
        else if(bestrank < 50)
            $(`#boss${i+1}-rank`).text(bestrank + " - " + rankings[i].spec).css("color", "green");
        else if(bestrank < 75)
            $(`#boss${i+1}-rank`).text(bestrank + " - " + rankings[i].spec).css("color", "blue");
        else if(bestrank < 95)
            $(`#boss${i+1}-rank`).text(bestrank + " - " + rankings[i].spec).css("color", "purple");
        else if(bestrank < 99)
            $(`#boss${i+1}-rank`).text(bestrank + " - " + rankings[i].spec).css("color", "orange");
        else if(bestrank == 99 || bestrank == 100)
            $(`#boss${i+1}-rank`).text(bestrank + " - " + rankings[i].spec).css("color", "pink");

        $(`#boss${i+1}-highest`).text(rankings[i].bestAmount.toFixed(1)).css("color", "purple");
        $(`#boss${i+1}-median`).text(Math.floor(rankings[i].medianPercent));
        $(`#boss${i+1}-kills`).text(rankings[i].totalKills);
    }

    let joblist = document.getElementById("job-list");
    for(job of res.data.Character.ClassJobs) {
        if(job.UnlockedState.Name.includes("Carpenter"))
            break;
        let row = document.createElement('div');
        row.setAttribute("class", "row");

        let col = document.createElement('div');
        col.setAttribute("class", "col-auto");

        let img = document.createElement('img');
        img.setAttribute("src", `/static/images/job/${job.UnlockedState.Name.toLowerCase().split(" ").join("")}.png`);
        img.setAttribute("width", "25px");
        img.setAttribute("height", "25px");
        img.style.display = "inline-block";
        img.style.margin = "2px";

        let plvl = document.createElement('p');
        plvl.setAttribute("class", "align-middle fs-8 m-0");
        plvl.style.display = "inline-block";
        plvl.innerText = `${job.Level}-`;

        let pname = document.createElement('p');
        pname.setAttribute("class", "align-middle fs-8 m-0");
        pname.style.display = "inline-block";
        pname.innerText = `${job.UnlockedState.Name}`

        col.append(img);
        col.append(plvl);
        col.append(pname);
        row.append(col);
        joblist.append(row);
    }
}

$("#unclaim-character").click(() => {
    if(confirm("Unlink this character?")) {
        $("#unlink-form").submit();
    }
});