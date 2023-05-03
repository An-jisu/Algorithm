# [unrated] 추억 점수 - 176963 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/176963) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>사진들을 보며 추억에 젖어 있던 루는 사진별로 추억 점수를 매길려고 합니다. 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수가 됩니다. 예를 들어 사진 속 인물의 이름이 ["may", "kein", "kain"]이고 각 인물의 그리움 점수가 [5점, 10점, 1점]일 때 해당 사진의 추억 점수는 16(5 + 10 + 1)점이 됩니다. 다른 사진 속 인물의 이름이 ["kali", "mari", "don", "tony"]이고 ["kali", "mari", "don"]의 그리움 점수가 각각 [11점, 1점, 55점]]이고, "tony"는 그리움 점수가 없을 때, 이 사진의 추억 점수는 3명의 그리움 점수를 합한 67(11 + 1 + 55)점입니다.</p>

<p>그리워하는 사람의 이름을 담은 문자열 배열 <code>name</code>, 각 사람별 그리움 점수를 담은 정수 배열 <code>yearning</code>, 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 <code>photo</code>가 매개변수로 주어질 때, 사진들의 추억 점수를 <code>photo</code>에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>name</code>의 길이 = <code>yearning</code>의 길이≤ 100

<ul>
<li>3 ≤ <code>name</code>의 원소의 길이 ≤ 7</li>
<li><code>name</code>의 원소들은 알파벳 소문자로만 이루어져 있습니다.</li>
<li><code>name</code>에는 중복된 값이 들어가지 않습니다.</li>
<li>1 ≤ <code>yearning[i]</code> ≤ 100</li>
<li><code>yearning[i]</code>는 i번째 사람의 그리움 점수입니다.</li>
</ul></li>
<li>3 ≤ <code>photo</code>의 길이 ≤ 100

<ul>
<li>1 ≤ <code>photo[i]</code>의 길이 ≤ 100</li>
<li>3 ≤ <code>photo[i]</code>의 원소(문자열)의 길이 ≤ 7</li>
<li><code>photo[i]</code>의 원소들은 알파벳 소문자로만 이루어져 있습니다.</li>
<li><code>photo[i]</code>의 원소들은 중복된 값이 들어가지 않습니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>name</th>
<th>yearning</th>
<th>photo</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["may", "kein", "kain", "radi"]</td>
<td>[5, 10, 1, 3]</td>
<td>[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]</td>
<td>[19, 15, 6]</td>
</tr>
<tr>
<td>["kali", "mari", "don"]</td>
<td>[11, 1, 55]</td>
<td>[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]</td>
<td>[67, 0, 55]</td>
</tr>
<tr>
<td>["may", "kein", "kain", "radi"]</td>
<td>[5, 10, 1, 3]</td>
<td>[["may"],["kein", "deny", "may"], ["kon", "coni"]]</td>
<td>[5, 15, 0]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<p>첫 번째 사진 속 "may", "kein", "kain", "radi"의 그리움 점수를 합치면 19(5 + 10 + 1 + 3)점 입니다. 두 번째 사진 속 그리워하는 사람들인 "may"와 "kein"의 그리움 점수를 합치면 15(5 + 10)점입니다. 세 번째 사진의 경우 "kain"과 "may"만 그리워하므로 둘의 그리움 점수를 합한 6(1 + 5)점이 사진의 추억 점수입니다. 따라서 [19, 15, 6]을 반환합니다.</p>

<p>입출력 예 #2</p>

<p>첫 번째 사진 속 그리워하는 사람들인 "kali", "mari", "don"의 그리움 점수를 합치면 67(11 + 1 + 55)점입니다. 두 번째 사진 속엔 그리워하는 인물이 없으므로 0점입니다. 세 번째 사진 속 그리워하는 사람은 "don"만 있으므로 55점입니다. 따라서 [67, 0, 55]를 반환합니다.</p>

<p>입출력 예 #3</p>

<p>설명 생략</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 😀 나의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/235828869-92220006-da0d-4bce-8421-293ce2a6e0fd.png) <br>
-> 딕셔너리로 문제 푼 거 너무 잘함!!!! 일단, 딕셔너리를 이용해서 {이름: 그리움점수}를 매칭시켰다. 그리고 중첩 반복문을 통해서, 하나의 사진 그리고 사진 속의 인물들에 하나씩 접근하면서, 만약 그 인물이 딕셔너리에 존재하면 그리움 점수가 0이 아니므로, sum에 그 이름에 해당하는 그리움점수를 더해주었다. 그리고 안쪽 반복문(하나의 사진)에 대한 추억점수 계산이 끝나면, 그 값을 answer에 append해주었고, 최종적으로는 answer값을 return하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
1.
![image](https://user-images.githubusercontent.com/70849122/235829770-368fddd4-263e-4e50-9393-acc0d1ec4c51.png) <br>
-> 2개의 배열을 하나의 딕셔너리로 합칠 때, 이렇게 간단하게도 할 수 있다는 것!! <br>
2. ![image](https://user-images.githubusercontent.com/70849122/235829842-ad8acaf8-396f-4219-9f92-b86da6c662cd.png) <br>
-> 같은 방법인데, 한 줄로 해결한 것이다. 여기서는 딕셔너리가 아니라, name과 yearning의 인덱스가 같음을 이용하여 풀이했다.<br><br>

## ✔️ What I learned: <br><br> 
- 두 개의 배열의 합쳐 하나의 리스트로 나타내기 위해서는 나의 풀이와 같이 zip함수 사용하기! <br>
- 어떤 배열의 값이 어떤 배열의 값에 해당하면, 위와 같이 딕셔너리로 값들 매칭해놓기!! <br><br>
