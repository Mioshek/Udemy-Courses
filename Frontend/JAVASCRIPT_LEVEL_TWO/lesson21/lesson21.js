function sleepIn(weekday, vacation) {
    if (!weekday){
        return true;
    }
    else if (vacation) {
        return true;
    }
    else{
        return false;
    }
}

function stringTimes(s, n) {
    var result = "";
    for (var i = 0; i<n; i++){
        result += s; 
    }
    return result;
}

function makeBricks(small, big, target){
    var sum = small + big*5;
    var value = 0;
    if (target > sum){
        return false;
    }
    else{
        for(var i=0; i<=big; i++){
            for(var j=0; j<=small; j++){
                value = i*5 + j;
                if(value == target){
                    return true; 
                }
            }
        }
        return false;
    }
  }