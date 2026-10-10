function validateLogin() {
    let u = document.getElementsByName("username")[0].value;
    let p = document.getElementsByName("password")[0].value;
    if (u === "" || p === "") {
        alert("Username / Password খালি রাখা যাবে না!\nUsername: admin\nPassword: 1234@1234");
        return false;
    }
    return true;
}
console.log("BOU DCS Project - Balay Karmaker - 24150892008 - DIIT - System Loaded");
