function get_creads(){
    var email_id = document.getElementById("email_id_login").value
    var pwd = document.getElementById("pwd_login").value
    var client_id = document.getElementById('client_id_login').value
    eel.catch_creads(email_id,pwd,client_id)
    location.replace("/chatpage.html");
}

function response_loop(){
    eel.get_reply()(set_recieve_value)
}


function set_send_value(){
    var send_msg = document.getElementById("sendMessage").value
    document.getElementById("send").innerHTML = send_msg
    document.getElementById("sendMessage").value = ''
    eel.catch_send_message(send_msg)

    var a = setInterval(response_loop(), 500) 
    
}


function set_recieve_value(reply){
    document.getElementById('rply').innerHTML = reply
}