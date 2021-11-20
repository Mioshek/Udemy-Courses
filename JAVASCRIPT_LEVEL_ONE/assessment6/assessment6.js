var yourName = prompt("What is your name?");
console.log(yourName);
var surname = prompt("What is your surname?");
console.log(surname);
var age = prompt("What is your age?");
console.log(age);
var height = prompt("What is your height in centimeters?");
console.log(height);
var petName = prompt("What is your pet's name?");
console.log(petName);

if (yourName[0] == surname[0] && age > 20 && age < 30 && height>=170 && petName[petName.length-1] == "y"){
    console.log("So you are a spy and this is your secret message.")
}
else{
    console.log("Zjebales")
}