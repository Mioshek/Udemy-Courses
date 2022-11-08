var firstUnit = document.querySelector('#one')
var secondUnit = document.querySelector('#two')
var thirdUnit = document.querySelector('#three')
var fourthUnit = document.querySelector('#four')
var fifthUnit = document.querySelector('#five')
var sixthUnit = document.querySelector('#six')
var seventhUnit = document.querySelector('#seven')
var eighthUnit = document.querySelector('#eight')
var ninthUnit = document.querySelector('#nine')

function changeToX(unit){
    unit.textContent = "X";
    unit.style.size = '30px';
}

function changeToO(unit){
    unit.textContent = "O";
    unit.style.size = '30px';
}

function changeToEmpty(unit){
    unit.textContent = "";
    unit.style.size = '30px';
}

function changeValue(unit){
    if (unit.textContent === ""){
        changeToX(unit);
    }
    else if (unit.textContent === "X") {
        changeToO(unit);
    }
    else if (unit.textContent === "O"){
        changeToEmpty(unit);
    }
}

firstUnit.addEventListener("click", function(){changeValue(firstUnit)});
secondUnit.addEventListener("click",function(){changeValue(secondUnit)});
thirdUnit.addEventListener("click",function(){changeValue(thirdUnit)});
fourthUnit.addEventListener("click",function(){changeValue(fourthUnit)});
fifthUnit.addEventListener("click",function(){changeValue(fifthUnit)});
sixthUnit.addEventListener("click",function(){changeValue(sixthUnit)});
seventhUnit.addEventListener("click",function(){changeValue(seventhUnit)});
eighthUnit.addEventListener("click",function(){changeValue(eighthUnit)});
ninthUnit.addEventListener("click",function(){changeValue(ninthUnit)});