function onLoginClick() {
    const divLogin = document.getElementById("div-login");
    const divSign = document.getElementById("div-sign");
    console.log("LOGIN");
    divSign.hidden = false;
    divLogin.hidden = true;
}

function onSignClick() {
    const divLogin = document.getElementById("div-login");
    const divSign = document.getElementById("div-sign");
    console.log("Sign");
    divSign.hidden = true;
    divLogin.hidden = false;
}