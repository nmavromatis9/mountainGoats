
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
        // it will run fetch then do the thing below
        .then(function(response) {
           if (response.status != 200) {
               console.log(`Response was not 200: ${response.status}`);
               return ;
           }
           
           response.json().then(function(data) {
              console.log(data);
              document.getElementById("price").textContent = data.price;
           })
        
        })
        
}

