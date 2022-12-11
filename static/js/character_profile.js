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
    document.getElementById("name").value = res.data.Character.Name;
    document.getElementById("character-server").innerText = res.data.Character.Server;
    document.getElementById("character-portrait").src=res.data.Character.Portrait;

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