var isOpen = false;
var body = document.getElementsByTagName('body')[0];
var hamMenu = document.getElementsByClassName('ham-menu')[0];

function menu() {
    if (isOpen) {
        body.style.overflow = "visible";
        hamMenu.style.left = "100%";
        isOpen = false;
    } else {
        body.style.overflow = "hidden";
        hamMenu.style.left = "0";
        isOpen = true;
    }
}

var isDown = false;
var dropdownElement = document.getElementsByClassName('dropdown')[0];

function dropdown() {
    if (isDown) {
        dropdownElement.style.top = "-100%";
        dropdownElement.style.opacity = '0';
        isDown = false;
    } else {
        dropdownElement.style.top = "90px";
        dropdownElement.style.opacity = '100%';
        isDown = true;
    }
}