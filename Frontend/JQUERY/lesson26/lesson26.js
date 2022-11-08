//Ceation of first player and question about name
var player1 = prompt("Player One: Enter Your Name , you will be Blue");
var player1Color = '#307df9';
var player1Wins = false;
//Ceation of second player and question about name
var player2 = prompt("Player Two: Enter Your Name, you will be Red");
var player2Color = '#f95130';
var player2Wins = false;
var currentPlayer;
var currentCol;
var currentRow;
var currentColor;
var round = 1;
var whoStarts = Math.floor(Math.random()*2);
var tb = $('table tr');

function returnColor(rowIndex,colIndex) {
    return tb.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
  }

function colorMatchCheck(firstEl,secondEl,thirdEl,fourthEl){
    return (firstEl===secondEl && firstEl===thirdEl && firstEl===fourthEl && firstEl !== 'rgb(128, 128, 128)' && firstEl !== undefined);
}

function checkBottom() {
    for (let i=4; i>-1; i--){
        var currentButton = tb.eq(i).find('td').eq(currentCol).find('button');
        if (currentButton.css('background-color')=='rgb(128, 128, 128)'){
            currentButton.css('background-color', currentColor);
            currentRow = i;
            break;
        }
    }
}

function whichIsCurrentPlayer() {
    if (whoStarts === 0){
        whoStarts = 1;
        currentPlayer = "player 2"
        currentColor = player2Color;
        $('h3').text(player1 + " Now it's your turn!");
    }
    else if (whoStarts === 1){
        whoStarts = 0;
        currentPlayer = "player 1"
        currentColor = player1Color;
        $('h3').text(player2 + " Now it's your turn!");
    }
}

function whichPlayerWon() {
    if (currentPlayer === "player 1"){
        player1Wins = true;
    }
    else if(currentPlayer === "player 2"){
        player2Wins = true;
    }
}

function displayWin() {
    if (player1Wins){
        $('h1').text("Congrats " + player1 + " you won the cross 4 Game!").css("fontSize", "50px")
        $('h2').fadeOut("fast");
        $('h3').fadeOut("fast");
        $('table').fadeOut("fast");
    }
    else if (player2Wins){
        $('h1').text("Congrats " + player2 + " you won the cross 4 Game!").css("fontSize", "50px")
        $('h2').fadeOut("fast");
        $('h3').fadeOut("fast");
        $('table').fadeOut("fast");
    }
}

function checkIfIsGray(col,row) {
    return (tb.eq(row).find('td').eq(col).find('button').css('background-color')==='rgb(128, 128, 128)');
}

function checkVertically(col,row) {
    let isTrue = false;
    for (let i = 0; i<3; i++){
        if (tb.eq(row+i).find('td').eq(col).find('button').css('background-color') ===tb.eq(row+i+1).find('td').eq(col).find('button').css('background-color') && !checkIfIsGray(col,row+i)){
            isTrue = true;
            continue;
        }
        else{
            isTrue = false;
            break;
        }
    }
    if (isTrue){
        whichPlayerWon();
    }  
} 

function checkHorizontally(row) {
    let isTrue = false;
    for (let i=0; i<4; i++){
        if (colorMatchCheck(returnColor(row,i), returnColor(row,i+1) ,returnColor(row,i+2), returnColor(row,i+3))){
                isTrue = true;
                break;
        }
        else{
            isTrue = false;
            continue;
        }
    }
    if (isTrue){
        whichPlayerWon();
    }
}

function checkDiagonally(col,row) {
    for (var col = 0; col < 5; col++) {
        for (var row = 0; row < 7; row++) {
          if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col+1) ,returnColor(row+2,col+2), returnColor(row+3,col+3))) {
            whichPlayerWon();
            return true;
          }else if (colorMatchCheck(returnColor(row,col), returnColor(row-1,col+1) ,returnColor(row-2,col+2), returnColor(row-3,col+3))) {
            console.log('diag');
            whichPlayerWon();
            return true;
          }else {
            continue;
          }
        }
      }
}

$('.board button').on('click',function() {
    whichIsCurrentPlayer();
    currentRow = $(this).closest("tr").index();
    currentCol = $(this).closest("td").index();
    checkBottom();
    if (round>6){
        checkVertically(currentCol, currentRow);
        checkHorizontally(currentRow);
        checkDiagonally(currentCol, currentRow);
        displayWin();
    }
    round++;
});