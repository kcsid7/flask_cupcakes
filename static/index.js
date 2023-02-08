const cupcake_flavor = $("#c_flavor");
const cupcake_size = $("#c_size");
const cupcake_rating = $("#c_rating");
const cupcake_image = $("#c_image");
const newcupcake_btn = $("#add_cupcake_btn");

const hidden_msg = $("#hidden_messages")

const cupcake_list = $("#cupcake_list");



const URL_BASE = "http://127.0.0.1:5000/api"


function showHiddenMessage(msg) {
    hidden_msg.css("display", "block")
    hidden_msg.text(msg)
    setTimeout(function() {
        hidden_msg.css("display", "none")
    }, 2000)
}


function appendDelBtn() {
    $(".del_cupcake").on("click", async function(evt) {
        cupcake_id = evt.target.closest("li").id.slice(3);
        const del = await axios.delete(`${URL_BASE}/cupcakes/${cupcake_id}`)
        evt.target.closest("li").remove()
        showHiddenMessage("Cupcake Deleted!")
    })
}



async function getAllCupcakes() {
    res = await axios.get(`${URL_BASE}/cupcakes`)

    for (const cupck  of res.data.cupcakes) {
        const newItem = $(appendCupcake(cupck));
        cupcake_list.append(newItem);
    }

    appendDelBtn();
}








function appendCupcake(cupcake) {
    return `
            <li class="list-group-item" id="cc-${cupcake.id}" >
                <img src="${cupcake.image}" alt="${cupcake.flavor}" style="width: 250px; height: 400px">
                <p><strong>Cupcake Flavor:</strong> ${cupcake.flavor}</p>
                <p><strong>Cupcake Size:</strong> ${cupcake.size}</p>
                <p><strong>Cupcake Rating:</strong> ${cupcake.rating}</p>
                <button class="del_cupcake btn btn-md btn-danger">Delete</button>
            </li>
            `
}

newcupcake_btn.on("click", async function(evt){
    evt.preventDefault();

    if ( cupcake_flavor.val() === '' || cupcake_size.val() === '' || cupcake_rating.val() === '') {
        showHiddenMessage("Need valid inputs!")
    } 
    else {
        // get values from form data
        const new_cupcake = {
            "flavor": cupcake_flavor.val(),
            "size": cupcake_size.val(),
            "rating": cupcake_rating.val(),
            "image": cupcake_image.val()
        }

        // post that data to the database
        const new_req = await axios.post(`${URL_BASE}/cupcakes`, new_cupcake);

        cupcake_flavor.val('');
        cupcake_size.val('');
        cupcake_rating.val('');
        cupcake_image.val('');
        showHiddenMessage("Added New Cupcake!")
        
        const newHTML_cupcake = appendCupcake(new_cupcake)
        cupcake_list.append(newHTML_cupcake);   
    }
    appendDelBtn();
})


getAllCupcakes();






