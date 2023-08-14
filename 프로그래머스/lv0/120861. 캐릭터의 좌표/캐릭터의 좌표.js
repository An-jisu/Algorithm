function solution(keyinput, board) {
    var answer = [0,0];
    var x = Math.floor(board[0]/2);
    var y = Math.floor(board[1]/2);
    for (let a of keyinput){
        if(a==='left'){
            if((answer[0]-1)<-x){
                continue;
            }
            else{
                answer[0]=answer[0]-1;
            }
        }
        else if (a==='right'){
            if((answer[0]+1)>x){
                continue;
            }
            else{
                answer[0]=answer[0]+1;
            }
        }
        else if (a==='up'){
            if((answer[1]+1)>y){
                continue;
            }
            else{
                answer[1]=answer[1]+1;
            }
        }
        else{
            if((answer[1]-1)<-y){
                continue;
            }
            else{
                answer[1]=answer[1]-1;
            }
        }
    }
    return answer;
}