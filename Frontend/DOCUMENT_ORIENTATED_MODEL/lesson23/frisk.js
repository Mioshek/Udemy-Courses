var header = document.querySelector("h1");
var red = 0;
var green = 0;
var blue = 0;
var COLOR_CHANGE_INTERVAL = 5;
var HEAD_CHANGE_INTERVAL = 8;

var TIMEOUT_BASE = COLOR_CHANGE_INTERVAL*255;

var intervalHeader;
var intervalRed;
var intervalGreen;
var intervalBlue;

//<decrements
function decrementRed(){red--;}
function decrementGreen(){green--;}
function decrementBlue(){blue--;}

function dispatchDecrementRedStopBlue(){
    clearInterval(intervalBlue);
    intervalRed = setInterval(decrementRed,COLOR_CHANGE_INTERVAL);
}
function dispatchDecrementGreenStopRed(){
    clearInterval(intervalRed);
    intervalGreen = setInterval(decrementGreen,COLOR_CHANGE_INTERVAL);
}
function dispatchDecrementBlueStopGreen(){
    clearInterval(intervalGreen);
    intervalBlue = setInterval(decrementBlue,COLOR_CHANGE_INTERVAL);
}
function stopBlue(){
    clearInterval(intervalBlue);
}

//decrements!>
function incrementRed(){red++;}
function incrementGreen(){green++;}
function incrementBlue(){blue++;}


function dispatchIncrementGreenStopRed(){
    clearInterval(intervalRed);
    intervalGreen = setInterval(incrementGreen,COLOR_CHANGE_INTERVAL);
}

function dispatchIncrementBlueStopGreen(){
    clearInterval(intervalGreen);
    intervalBlue = setInterval(incrementBlue,COLOR_CHANGE_INTERVAL);
}
function stopBlue(){
    clearInterval(intervalBlue);
}

function friskFunc(){
    intervalHeader = setInterval(updateHeader,HEAD_CHANGE_INTERVAL);
    //initially any?
    illuminate();
    var illuminateInterval = setInterval(illuminate,TIMEOUT_BASE*7);

}
function illuminate(){
    var i = 0;
    //increments
    intervalRed = setInterval(incrementRed,COLOR_CHANGE_INTERVAL);
    setTimeout(dispatchIncrementGreenStopRed,TIMEOUT_BASE*++i);
    setTimeout(dispatchIncrementBlueStopGreen,TIMEOUT_BASE*++i);
    //decrements
    setTimeout(dispatchDecrementRedStopBlue,TIMEOUT_BASE*++i);
    setTimeout(dispatchDecrementGreenStopRed,TIMEOUT_BASE*++i);
    setTimeout(dispatchDecrementBlueStopGreen,TIMEOUT_BASE*++i);
    setTimeout(stopBlue,TIMEOUT_BASE*++i);
}

function updateHeader(){
    header.style.color = "rgb(" + red + ", "+ green + ", " + blue + ")";
    //console.log(red + " "+ green + " "+ blue);
}

friskFunc();