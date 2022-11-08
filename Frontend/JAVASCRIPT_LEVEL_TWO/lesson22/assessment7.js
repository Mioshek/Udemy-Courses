// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31
  }
  
  // Add a method called nameLength that prints out the
  // length of the employees name to the console.
  function nameLength(employee){
    console.log(employee.name.length);
  }
  
  nameLength(employee);
  ///////////////////
  // PROBLEM 2 /////
  /////////////////
  
  // Given the object:
  var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31
  }
  
  // Write program that will create an Alert in the browser of each of the
  // object's values for the key value pairs. For example, it should alert:
  
function program(employee) {
    for (elements in employee)
        if (elements === "name") {
            alert("Name is " + employee.name)
        }
        else if (elements === "job") {
           alert("Job is " + employee.job); 
        }
        else{
            alert("Age is " + employee.age);
        }   
}

  program(employee);
  // Name is John Smith, Job is Programmer, Age is 31.
  
  
  
  ///////////////////
  // PROBLEM 3 /////
  /////////////////
  
  // Given the object:
  var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31
  }
function split(employee) {
    var lettersArr = [];
    var nameLength =  employee.name.length;
    while (employee.name[nameLength] !== " "){
        lettersArr.push(employee.name[nameLength])
        nameLength--;
    }
    var surname;
    var surnameLength = lettersArr.length;
    for (var element = surnameLength; element>=0; element--){
        surname += lettersArr[element];
    }
    console.log(surname.slice(3,-9));
    
}

split(employee);
  // Add a method called lastName that prints
  // out the employee's last name to the console.
  
  // You will need to figure out how to split a string to an array.
  // Hint: http://www.w3schools.com/jsref/jsref_split.asp