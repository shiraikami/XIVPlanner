"use strict;"

window.addEventListener('load', async function() {
    let data;
    try {
        const token = await axios.get("http://127.0.0.1:5000/fflogs/token");
        if(token) {
            let access_token = token.data.access_token;
            let response = await requestFFLogs(access_token);
            data = response.data.data;
            $("#zonename").text(data.worldData.zone.name);
        }
    } catch {
        console.log("Error fetching FFLogs token.");
        $("#zone").hide();
        $("#rankings").hide();
    }
    Boss1(data);
    Boss2(data);
    Boss3(data);
    Boss4(data);
    Boss5(data);
});


async function requestFFLogs(access_token) {
    try {
        let data = await axios({
            url: "https://www.fflogs.com/api/v2/client",
            method: 'POST',
            headers: { Authorization: `Bearer ${access_token}`, Content_Type: 'application/json' },
            data: {
                query: `query($id: Int) {
                            worldData {
                                zone(id: $id) {
                                    id
                                    name
                                    encounters {
                                        id
                                        name
                                        characterRankings
                                    }
                                }
                            }
                        }`, variables: { id: 49 }
            }
        });
        return data;
    } catch {
        console.log("Error requesting data from FFLogs API");
    }
}

function Boss1(data) {
    let encounterData = data.worldData.zone.encounters[0];
    $("#boss1name").text(encounterData.name);
    let rankings = data.worldData.zone.encounters[0].characterRankings.rankings;
    for(let i = 0; i < 5; i++) {
        let row = $(`<div class="row"></div>`);

        let rankdiv = $(`<div class="col-1 border"></div>`);
        let rank = $(`<p class="text-center mx-auto m-2"></p>`).text(i+1).css('color', 'green');
        rankdiv.append(rank);
        
        let namediv = $(`<div class="col-3 border"></div>`);
        let name = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].name);
        namediv.append(name);

        let jobdiv = $(`<div class="col border"></div>`);
        let job = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].spec);
        jobdiv.append(job);

        let patchdiv = $(`<div class="col-1 border"></div>`);
        let patch = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].bracketData);
        patchdiv.append(patch);

        let dpsdiv = $(`<div class="col border"></div>`);
        let dps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].pDPS.toFixed(1)).css('color', 'lime');
        dpsdiv.append(dps);

        let rdpsdiv = $(`<div class="col border"></div>`);
        let rdps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].rDPS.toFixed(1)).css('color', '#CBC3E3');
        rdpsdiv.append(rdps);

        let adpsdiv = $(`<div class="col border"></div>`);
        let adps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].aDPS.toFixed(1)).css('color', 'lightblue');
        adpsdiv.append(adps);

        let ndpsdiv = $(`<div class="col border"></div>`);
        let ndps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].nDPS.toFixed(1)).css('color', 'orange');
        ndpsdiv.append(ndps);

        row.append(rankdiv);
        row.append(namediv);
        row.append(jobdiv);
        row.append(patchdiv);
        row.append(dpsdiv);
        row.append(rdpsdiv);
        row.append(adpsdiv);
        row.append(ndpsdiv);
        $("#boss1").append(row);
    }
}

function Boss2(data) {
    let encounterData = data.worldData.zone.encounters[1];
    $("#boss2name").text(encounterData.name);
    let rankings = data.worldData.zone.encounters[1].characterRankings.rankings;
    for(let i = 0; i < 5; i++) {
        let row = $(`<div class="row"></div>`);

        let rankdiv = $(`<div class="col-1 border"></div>`);
        let rank = $(`<p class="text-center mx-auto m-2"></p>`).text(i+1).css('color', 'green');
        rankdiv.append(rank);
        
        let namediv = $(`<div class="col-3 border"></div>`);
        let name = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].name);
        namediv.append(name);

        let jobdiv = $(`<div class="col border"></div>`);
        let job = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].spec);
        jobdiv.append(job);

        let patchdiv = $(`<div class="col-1 border"></div>`);
        let patch = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].bracketData);
        patchdiv.append(patch);

        let dpsdiv = $(`<div class="col border"></div>`);
        let dps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].pDPS.toFixed(1)).css('color', 'lime');
        dpsdiv.append(dps);

        let rdpsdiv = $(`<div class="col border"></div>`);
        let rdps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].rDPS.toFixed(1)).css('color', '#CBC3E3');
        rdpsdiv.append(rdps);

        let adpsdiv = $(`<div class="col border"></div>`);
        let adps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].aDPS.toFixed(1)).css('color', 'lightblue');
        adpsdiv.append(adps);

        let ndpsdiv = $(`<div class="col border"></div>`);
        let ndps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].nDPS.toFixed(1)).css('color', 'orange');
        ndpsdiv.append(ndps);

        row.append(rankdiv);
        row.append(namediv);
        row.append(jobdiv);
        row.append(patchdiv);
        row.append(dpsdiv);
        row.append(rdpsdiv);
        row.append(adpsdiv);
        row.append(ndpsdiv);
        $("#boss2").append(row);
    }
}

function Boss3(data) {
    let encounterData = data.worldData.zone.encounters[2];
    $("#boss3name").text(encounterData.name);
    let rankings = data.worldData.zone.encounters[2].characterRankings.rankings;
    for(let i = 0; i < 5; i++) {
        let row = $(`<div class="row"></div>`);

        let rankdiv = $(`<div class="col-1 border"></div>`);
        let rank = $(`<p class="text-center mx-auto m-2"></p>`).text(i+1).css('color', 'green');
        rankdiv.append(rank);
        
        let namediv = $(`<div class="col-3 border"></div>`);
        let name = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].name);
        namediv.append(name);

        let jobdiv = $(`<div class="col border"></div>`);
        let job = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].spec);
        jobdiv.append(job);

        let patchdiv = $(`<div class="col-1 border"></div>`);
        let patch = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].bracketData);
        patchdiv.append(patch);

        let dpsdiv = $(`<div class="col border"></div>`);
        let dps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].pDPS.toFixed(1)).css('color', 'lime');
        dpsdiv.append(dps);

        let rdpsdiv = $(`<div class="col border"></div>`);
        let rdps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].rDPS.toFixed(1)).css('color', '#CBC3E3');
        rdpsdiv.append(rdps);

        let adpsdiv = $(`<div class="col border"></div>`);
        let adps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].aDPS.toFixed(1)).css('color', 'lightblue');
        adpsdiv.append(adps);

        let ndpsdiv = $(`<div class="col border"></div>`);
        let ndps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].nDPS.toFixed(1)).css('color', 'orange');
        ndpsdiv.append(ndps);

        row.append(rankdiv);
        row.append(namediv);
        row.append(jobdiv);
        row.append(patchdiv);
        row.append(dpsdiv);
        row.append(rdpsdiv);
        row.append(adpsdiv);
        row.append(ndpsdiv);
        $("#boss3").append(row);
    }
}

function Boss4(data) {
    let encounterData = data.worldData.zone.encounters[3];
    $("#boss4name").text(encounterData.name);
    let rankings = data.worldData.zone.encounters[3].characterRankings.rankings;
    for(let i = 0; i < 5; i++) {
        let row = $(`<div class="row"></div>`);

        let rankdiv = $(`<div class="col-1 border"></div>`);
        let rank = $(`<p class="text-center mx-auto m-2"></p>`).text(i+1).css('color', 'green');
        rankdiv.append(rank);
        
        let namediv = $(`<div class="col-3 border"></div>`);
        let name = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].name);
        namediv.append(name);

        let jobdiv = $(`<div class="col border"></div>`);
        let job = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].spec);
        jobdiv.append(job);

        let patchdiv = $(`<div class="col-1 border"></div>`);
        let patch = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].bracketData);
        patchdiv.append(patch);

        let dpsdiv = $(`<div class="col border"></div>`);
        let dps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].pDPS.toFixed(1)).css('color', 'lime');
        dpsdiv.append(dps);

        let rdpsdiv = $(`<div class="col border"></div>`);
        let rdps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].rDPS.toFixed(1)).css('color', '#CBC3E3');
        rdpsdiv.append(rdps);

        let adpsdiv = $(`<div class="col border"></div>`);
        let adps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].aDPS.toFixed(1)).css('color', 'lightblue');
        adpsdiv.append(adps);

        let ndpsdiv = $(`<div class="col border"></div>`);
        let ndps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].nDPS.toFixed(1)).css('color', 'orange');
        ndpsdiv.append(ndps);

        row.append(rankdiv);
        row.append(namediv);
        row.append(jobdiv);
        row.append(patchdiv);
        row.append(dpsdiv);
        row.append(rdpsdiv);
        row.append(adpsdiv);
        row.append(ndpsdiv);
        $("#boss4").append(row);
    }
}

function Boss5(data) {
    let encounterData = data.worldData.zone.encounters[4];
    $("#boss5name").text(encounterData.name);
    let rankings = data.worldData.zone.encounters[4].characterRankings.rankings;
    for(let i = 0; i < 5; i++) {
        let row = $(`<div class="row"></div>`);

        let rankdiv = $(`<div class="col-1 border"></div>`);
        let rank = $(`<p class="text-center mx-auto m-2"></p>`).text(i+1).css('color', 'green');
        rankdiv.append(rank);
        
        let namediv = $(`<div class="col-3 border"></div>`);
        let name = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].name);
        namediv.append(name);

        let jobdiv = $(`<div class="col border"></div>`);
        let job = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].spec);
        jobdiv.append(job);

        let patchdiv = $(`<div class="col-1 border"></div>`);
        let patch = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].bracketData);
        patchdiv.append(patch);

        let dpsdiv = $(`<div class="col border"></div>`);
        let dps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].pDPS.toFixed(1)).css('color', 'lime');
        dpsdiv.append(dps);

        let rdpsdiv = $(`<div class="col border"></div>`);
        let rdps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].rDPS.toFixed(1)).css('color', '#CBC3E3');
        rdpsdiv.append(rdps);

        let adpsdiv = $(`<div class="col border"></div>`);
        let adps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].aDPS.toFixed(1)).css('color', 'lightblue');
        adpsdiv.append(adps);

        let ndpsdiv = $(`<div class="col border"></div>`);
        let ndps = $(`<p class="text-center mx-auto m-2"></p>`).text(rankings[i].nDPS.toFixed(1)).css('color', 'orange');
        ndpsdiv.append(ndps);

        row.append(rankdiv);
        row.append(namediv);
        row.append(jobdiv);
        row.append(patchdiv);
        row.append(dpsdiv);
        row.append(rdpsdiv);
        row.append(adpsdiv);
        row.append(ndpsdiv);
        $("#boss5").append(row);
    }
}