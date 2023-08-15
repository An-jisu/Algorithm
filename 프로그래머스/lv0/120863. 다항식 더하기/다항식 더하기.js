function solution(polynomial) {
    var a = 0, b = 0;
    var arr = polynomial.split(' + ');
    for (var k of arr){
        if (k.includes('x')){
            if (k.length===1){
                a+=1;
            }
            else{
                a+=Number(k.split('x')[0]);
            }
        }
        else{
            b+=Number(k);
        }
    }
    return (a===0)? ((b===0)?'0':""+b+""):((b===0)?((a===1)?'x':a+'x'):(a===1)?'x + '+b:a+'x + '+b);
}