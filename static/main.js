



function sendEmail() {
    var useremail = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var data = JSON.parse("credentials");
    data[useremail] = password;
    alert(data[useremail]) 
}

function showPass(){
    var pass = document.getElementById("password");
    if (pass.type === "password"){
        pass.type = "text";
    }else {
        pass.type = "password";
    }
}