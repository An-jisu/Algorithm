function solution(id_pw, db) {
    for (var i of db){
        if(id_pw[0]==i[0] && id_pw[1]==i[1]){
            return 'login';
        }
        else if (id_pw[0]==i[0] && id_pw[1]!=i[1]){
            return 'wrong pw';
        }
        else{
            continue;
        }
    }
    return 'fail'
}