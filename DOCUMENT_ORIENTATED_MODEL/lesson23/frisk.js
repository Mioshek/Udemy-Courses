var header = document.querySelector("h1");
var red = 0;
var green = 0;
var blue = 0;
var i = 0;
var HEAD_CHANGE_INTERVAL = 1500;
setInterval(updateHeader,HEAD_CHANGE_INTERVAL,++red,blue,green);

function updateHeader(red,blue,green){
    header.style.color = "rgb(" + red + ", "+ green + ", " + blue + ")";
    console.log("bussy " + red);
}