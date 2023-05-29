# [level 1] 완주하지 못한 선수 - 42576 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42576#qna) 

### 성능 요약

메모리: 26 MB, 시간: 71.99 ms

### 구분

코딩테스트 연습 > 해시

### 채점결과

Empty

### 문제 설명

<p>수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.</p>

<p>마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.</li>
<li>completion의 길이는 participant의 길이보다 1 작습니다.</li>
<li>참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.</li>
<li>참가자 중에는 동명이인이 있을 수 있습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>participant</th>
<th>completion</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>["leo", "kiki", "eden"]</td>
<td>["eden", "kiki"]</td>
<td>"leo"</td>
</tr>
<tr>
<td>["marina", "josipa", "nikola", "vinko", "filipa"]</td>
<td>["josipa", "filipa", "marina", "nikola"]</td>
<td>"vinko"</td>
</tr>
<tr>
<td>["mislav", "stanko", "mislav", "ana"]</td>
<td>["stanko", "ana", "mislav"]</td>
<td>"mislav"</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>예제 #1<br>
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.</p>

<p>예제 #2<br>
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.</p>

<p>예제 #3<br>
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.</p>

<hr>

<p>※ 공지 - 2023년 01월 25일 테스트케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ❤️ 문제 핵심: <br>
동명이인을 어떻게 처리할 지가 관건인 문제같다. <br><br>

## 😀 나의 풀이: <br>
-> 처음에는 반복문을 돌면서, completion 배열에 있으면 거기서 그 값을 삭제해주었고, 마지막에 i값을 return 시켜주었다. 그랬더니 테스트케이스는 모두 돌아가지만, 효율성에서 문제가 생기는 것이다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d3653086-05e3-4afd-8724-df4f8ea368da) <br>
-> 두 배열은 먼저 sort한 다음에, completion 만큼 돌면서, 같지 않으면 그것이 완주하지 못한 것이므로 그것을 반환한다. 끝까지 반환하지 않았으면, 마지막 주자가 완주하지 못한 것이므로 그 값을 반환한다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
- hash를 활용한 풀이<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/5b4bf3aa-0406-400c-9fb5-085f2753f102) <br>
-> Participant는 있고 Completion에는 없는 한 명을 찾는 것이다. participant의 해쉬값을 모두 구하고 completon의 해쉬값들을 모두 뺀다. 그러면, 남은 해쉬값이 완주하지 못한 선수이다. 그 해쉬값에 해당하는 value값(사람)을 찾으면 된다. 해쉬 맵을 이용해서 hashdic에 key와 value를 저장해주자!<br>
- counter를 활용한 풀이<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/a61b1e57-d44a-48d4-9859-dfa4000abcee) <br>
-> collection의 counter 클래스를 이용한다. set은 중복을 허용하지 않고, 리스트는 뺄셈을 허용하지 않는다. counter는 키값과 value count 값을 가지고 있다. 따라서 위와 같이 구할 수 있다. <br><br>

## ✔️ What I learned: <br>
- 중복 허용해서 두 리스트의 공통되지 않는 값 구하는 방법: collcetions.Counter 클래스 이용<br>
- 해쉬함수: 
