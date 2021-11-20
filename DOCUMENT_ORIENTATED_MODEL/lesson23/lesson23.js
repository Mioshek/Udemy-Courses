var header = document.querySelector("h1");
var red = 0;
var green = 0;
var blue = 0;
var ascendingIsTrue = true;
var descendingIsTrue = false;
var redUpperBound = true;
var greenUpperBound = true;
var blueUpperBound = true;
var redLowerBound = false;
var greenLowerBound = false;
var blueLowerBound = false;

function updateHeader(){
    header.style.color = "rgb(" + red + ", "+ green + ", " + blue + ")";
}

function mioshekFunc(){
    if (ascendingIsTrue && red == 255 && green == 255 && blue == 255 ){
        ascendingIsTrue = false;
        descendingIsTrue = true;
        blueUpperBound = false;
        blueLowerBound = true;
    }
    else if (descendingIsTrue && red == 0 && green == 0 && blue == 0 ){
        descendingIsTrue = false;
        ascendingIsTrue = true;
        blueUpperBound = true;
        blueLowerBound = false;
    }
    else if (ascendingIsTrue){
        if(red == 255){
            redUpperBound = false;
            redLowerBound = true;
        }
        if(green == 255){
            greenUpperBound = false;
            greenLowerBound = true;
        }
        if(blue == 255){
            blueUpperBound = false;
            blueLowerBound = true;
        }
        if (redUpperBound){
            red++;
        }
        else if(greenUpperBound){
            green++;
        }
        else if(blueUpperBound){
            blue++
        } 
    }
    else if (descendingIsTrue) {
        if(red == 0){
            redUpperBound = true;
            redLowerBound = false;
        }
        if(green == 0){
            greenUpperBound = true;
            greenLowerBound = false;
        }
        if(blue == 0){
            blueUpperBound = true;
            blueLowerBound = false;
        }
        if (redLowerBound){
            red--;
        }
        else if(greenLowerBound){
            green--;
        }
        else if(blueLowerBound){
            blue--;
        }
    }
    updateHeader();
    console.log(red,green,blue);
}

//setInterval("mioshekFunc()",50);

