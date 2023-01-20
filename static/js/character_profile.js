"user strict;"

let url = "https://xivapi.com/character/";

window.addEventListener('load', async function() {
    url = url + document.getElementById('char-id').innerText;
    charInfo = await requestXIVAPI(url);
    try {
        const token = await axios.get("http://127.0.0.1:5000/fflogs/token");
        if(!token.message) {
            let access_token = token.data.access_token;
            requestFFLogs(access_token, charInfo.name, charInfo.serverSlug, charInfo.serverRegion);
        }
    } catch {
        console.log("Error fetching FFLogs token.");
        $("#fflogs-container").hide();
    }
});

async function requestXIVAPI(url) {
    let res;
    try {
        res = await axios.get(url);
    } catch {
        console.log("Error getting character data from XIVAPI.");
    }

    if(res.data.Character.DC == "Aether" || res.data.Character.DC == "Primal" || res.data.Character.DC == "Crystal") {
        serverRegion = "NA";
    } 
    else if(res.data.Character.DC == "Chaos" || res.data.Character.DC == "Light") {
        serverRegion = "EU";
    }
    else {
        serverRegion = "JP";
    }

    serverSlug = res.data.Character.Server

    document.getElementById("character-thumbnail").src=res.data.Character.Avatar;
    document.getElementById("character-name").innerText = res.data.Character.Name;
    document.getElementById("character-server").innerText = res.data.Character.Server;
    document.getElementById("character-portrait").src=res.data.Character.Portrait;
    $("#followname").val(res.data.Character.Name);
    $("#followserver").val(serverSlug);
    $("#followportrait").val(res.data.Character.Avatar);
    $("#linkname").val(res.data.Character.Name);
    $("#linkserver").val(serverSlug);
    $("#linkportrait").val(res.data.Character.Avatar);

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

    return { "name": res.data.Character.Name, "serverRegion": serverRegion, "serverSlug": serverSlug}
} 

async function requestFFLogs(access_token, name, serverSlug, serverRegion) {
    try {
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
                        }`, variables: { name: name, serverSlug: serverSlug, serverRegion: serverRegion }
            }
        });
    
        console.log(data);
        let rankings = await data.data.data.characterData.character.zoneRankings.rankings;
     
        for (let i = 0; i < rankings.length; i++) {
    
            $(`#boss${i+1}-name`).text(rankings[i].encounter.name);
    
            let bestrank = String(Math.floor(rankings[i].rankPercent))
            if(bestrank < 25)
                $(`#boss${i+1}-rank`).text(bestrank).css("color", "gray");
            else if(bestrank < 50)
                $(`#boss${i+1}-rank`).text(bestrank).css("color", "green");
            else if(bestrank < 75)
                $(`#boss${i+1}-rank`).text(bestrank).css("color", "blue");
            else if(bestrank < 95)
                $(`#boss${i+1}-rank`).text(bestrank).css("color", "purple");
            else if(bestrank < 99)
                $(`#boss${i+1}-rank`).text(bestrank).css("color", "orange");
            else if(bestrank == 99 || bestrank == 100)
                $(`#boss${i+1}-rank`).text(bestrank).css("color", "pink");
    
            $(`#boss${i+1}-job`).text(rankings[i].spec);
            $(`#boss${i+1}-highest`).text(rankings[i].bestAmount.toFixed(1)).css("color", "purple");
            $(`#boss${i+1}-median`).text(Math.floor(rankings[i].medianPercent));
            $(`#boss${i+1}-kills`).text(rankings[i].totalKills);
        }
    } catch {
        console.log("Error getting character rankings from FFLogs API.");
        $("#fflogs-container").hide();
    }
}

$("#unclaim-character").click(() => {
    if(confirm("Unlink this character?")) {
        $("#unlink-form").submit();
    }
});

$("#unfollow-character").click(() => {
    if(confirm("Unfollow this character?")) {
        $("#unfollow-form").submit();
    }
});