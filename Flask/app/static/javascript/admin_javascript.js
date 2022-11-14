// this function is run when the Get Price button is pressed
function get_price() {
    var hospital = document.getElementById("hosp_name");
    var insurer = document.getElementById("insurer");
    var procedure = document.getElementById("procedure");
    var entry = {
        hospital: hospital.value,
        insurer: insurer.value,
        procedure: procedure.value
    }
    //console.log(entry);
    // fetch takes two arguments, url/endpoint to get or post data from 
    // and init construction (instruction for how fetch should operate)
    // back ticks used for js string interpolation
    // window location will get url address
    fetch(`${window.location}/../get_price`, {
        method: "POST",
        credentials: "include", // useful for cookies, will not use
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
    // it will run fetch, then process the response and update the page
    .then(function(response) {
        if (response.status != 200) {
            console.log(`Response was not 200: ${response.status}`);
            return ;
        } else {
            response.json().then(function(data) {
                console.log(data);
                document.getElementById("price").textContent = data.price;
           })
        }    
    })        
}

// this function is run when the Set Price button is pressed
function set_price() {
    var hospital = document.getElementById("hosp_name");
    var insurer = document.getElementById("insurer");
    var procedure = document.getElementById("procedure");
    var desired_price = document.getElementById("desired_price");
    var entry = {
        hospital: hospital.value,
        insurer: insurer.value,
        procedure: procedure.value,
        desired_price: desired_price.value
    }
    // fetch takes two arguments, url/endpoint to get or post data from 
    // and init construction (instruction for how fetch should operate)
    // back ticks used for js string interpolation
    // window location will get url address
    fetch(`${window.location}/../set_price`, {
        method: "POST",
        credentials: "include", // useful for cookies, will not use
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
           })
        })
    // it will run fetch, then process the response and update the page
    .then(function(response) {
        // if you don't get a 200, print status code to console
        if (response.status != 200) {
            console.log(`Response was not 200: ${response.status}`);
            return ;
        } else { // rec'd 200, update the html
            response.json().then(function(data) {
                console.log(data);
                document.getElementById("new_price").textContent = data.new_price;
            }) 
        }  
    })        
}