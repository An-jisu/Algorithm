function solution(dots) {
    //첫번째 좌표와 x좌표 같은거 찾아서 높이, y좌표 같은 거 찾아서 너비
    var a = dots[0];
    var h, w = 0;
    for (var k = 1;k<dots.length;k++){
        if (dots[k][0]===a[0]){
            console.log()
            h = Math.abs(a[1]-dots[k][1]);
        }
        if (dots[k][1]===a[1]){
            w = Math.abs(a[0]-dots[k][0]);
        }
    }
    return w*h;
}