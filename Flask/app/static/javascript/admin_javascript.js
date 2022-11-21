// this function is run when the select a hospital dropdown is clicked
function selectHospital() {
    // add a listener for all items in the dropdown menu
    // selected item should be given active class
    // text content of dropdown button should be updated to match selection
    var header = document.getElementById("selectHospital");
    var hospitals = header.getElementsByClassName("dropdown-item");
    console.log(header);
    console.log(header.getElementsByClassName("btn")[0].innerText);
    for (var i = 0; i < hospitals.length; i++) {
        hospitals[i].addEventListener("click", function() {
            if (header.getElementsByClassName("active").length != 0) {
                var current = header.getElementsByClassName("active");
                current[0].className = current[0].className.replace(" active", "");
            }
            this.className += " active";
            header.getElementsByClassName("btn")[0].innerText = this.innerText;
        });
    }
}

// this function is run when the select an insurer dropdown is clicked
function selectInsurer() {
    // add a listener for all items in the dropdown menu
    // selected item should be given active class
    // text content of dropdown button should be updated to match selection
    var header = document.getElementById("selectInsurer");
    var insurers = header.getElementsByClassName("dropdown-item");
    console.log(header);
    console.log(header.getElementsByClassName("btn")[0].innerText);
    for (var i = 0; i < insurers.length; i++) {
        insurers[i].addEventListener("click", function() {
            if (header.getElementsByClassName("active").length != 0) {
                var current = header.getElementsByClassName("active");
                current[0].className = current[0].className.replace(" active", "");
            }
            this.className += " active";
            header.getElementsByClassName("btn")[0].innerText = this.innerText;
        });
    }
}

// this function is run when the Search button is pressed
function search() {
    var hospital = document.getElementById("selectHospital").getElementsByClassName("active")[0];
    var insurer = document.getElementById("selectInsurer").getElementsByClassName("active")[0];
    var procedure = document.getElementById("procedure");
    console.log(procedure.value);
    // entry will be sent to server, used in SQL query
    var entry = {
        hospital: hospital.innerText,
        insurer: insurer.innerText,
        procedure: procedure.value
    }
    // fetch takes two arguments, url/endpoint to get or post data from 
    // and init construction (instruction for how fetch should operate)
    // back ticks used for js string interpolation
    // window location will get url address
    fetch(`${window.location}/../search`, {
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
                // remove any elements currently in the list
                const to_delete = document.getElementById("search_results");
                to_delete.innerHTML = "";
                                
                // loop through the found procedures and add them to the search_results list box
                // End result example:
                // <button type="button" class="list-group-item list-group-item-action" value="Blood Draw">Blood Draw</button>
                for (var i = 0; i < data.procedures.length; i++) {
                    var text1 = "<button type='button' class='list-group-item list-group-item-action' value='";
                    var text2 = data.procedures[i][0];
                    var text3 = "'>"
                    var text4 = data.procedures[i][0]
                    var text5 = "</option>"
                    var my_html = text1.concat(text2,text3,text4,text5);
                    document.getElementById("search_results").insertAdjacentHTML("beforeend",my_html);
                }
                
                // add listener for when button is pressed
                var header = document.getElementById("search_results");
                var results = header.getElementsByClassName("list-group-item");
                for (var j=0; j<results.length; j++) {
                    results[j].addEventListener("click", function() {
                        if (header.getElementsByClassName("active").length != 0) {
                            var current = header.getElementsByClassName("active");
                            current[0].className = current[0].className.replace(" active", "");
                        }
                        this.className += " active";
                    });
                }
           })
        }    
    })        
}

// this function is run when the Get Price button is pressed
function get_price() {
    var hospital = document.getElementById("selectHospital").getElementsByClassName("active")[0];
    var insurer = document.getElementById("selectInsurer").getElementsByClassName("active")[0];
    var procedure = document.getElementById("search_results").getElementsByClassName("active")[0];
    
    // entry will be sent to server, used in SQL query stmt
    var entry = {
        hospital: hospital.innerText,
        insurer: insurer.innerText,
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
                document.getElementById("price").value = "$ ".concat(data.price);
           })
        }    
    })        
}

// this function is run when the Update Price button is pressed
function set_price() {
    var hospital = document.getElementById("selectHospital").getElementsByClassName("active")[0];
    var insurer = document.getElementById("selectInsurer").getElementsByClassName("active")[0];
    var procedure = document.getElementById("search_results").getElementsByClassName("active")[0];
    var desired_price = document.getElementById("desired_price");
    
    // entry will be sent to server, used in SQL query/update stmts
    var entry = {
        hospital: hospital.innerText,
        insurer: insurer.innerText,
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
                document.getElementById("new_price").value = "$ ".concat(data.new_price);
            }) 
        }  
    })        
}

