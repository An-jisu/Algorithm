# [level 1] 신고 결과 받기 - 92334 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/92334) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT

### 채점결과

Empty

### 문제 설명

<h5>문제 설명</h5>

<p>신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.</p>

<ul>
<li>각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.

<ul>
<li>신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.</li>
<li>한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.</li>
</ul></li>
<li>k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.

<ul>
<li>유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.</li>
</ul></li>
</ul>

<p>다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.</p>
<table class="table">
        <thead><tr>
<th>유저 ID</th>
<th>유저가 신고한 ID</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>"muzi"</td>
<td>"frodo"</td>
<td>"muzi"가 "frodo"를 신고했습니다.</td>
</tr>
<tr>
<td>"apeach"</td>
<td>"frodo"</td>
<td>"apeach"가 "frodo"를 신고했습니다.</td>
</tr>
<tr>
<td>"frodo"</td>
<td>"neo"</td>
<td>"frodo"가 "neo"를 신고했습니다.</td>
</tr>
<tr>
<td>"muzi"</td>
<td>"neo"</td>
<td>"muzi"가 "neo"를 신고했습니다.</td>
</tr>
<tr>
<td>"apeach"</td>
<td>"muzi"</td>
<td>"apeach"가 "muzi"를 신고했습니다.</td>
</tr>
</tbody>
      </table>
<p>각 유저별로 신고당한 횟수는 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>유저 ID</th>
<th>신고당한 횟수</th>
</tr>
</thead>
        <tbody><tr>
<td>"muzi"</td>
<td>1</td>
</tr>
<tr>
<td>"frodo"</td>
<td>2</td>
</tr>
<tr>
<td>"apeach"</td>
<td>0</td>
</tr>
<tr>
<td>"neo"</td>
<td>2</td>
</tr>
</tbody>
      </table>
<p>위 예시에서는 2번 이상 신고당한 "frodo"와 "neo"의 게시판 이용이 정지됩니다. 이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>유저 ID</th>
<th>유저가 신고한 ID</th>
<th>정지된 ID</th>
</tr>
</thead>
        <tbody><tr>
<td>"muzi"</td>
<td>["frodo", "neo"]</td>
<td>["frodo", "neo"]</td>
</tr>
<tr>
<td>"frodo"</td>
<td>["neo"]</td>
<td>["neo"]</td>
</tr>
<tr>
<td>"apeach"</td>
<td>["muzi", "frodo"]</td>
<td>["frodo"]</td>
</tr>
<tr>
<td>"neo"</td>
<td>없음</td>
<td>없음</td>
</tr>
</tbody>
      </table>
<p>따라서 "muzi"는 처리 결과 메일을 2회, "frodo"와 "apeach"는 각각 처리 결과 메일을 1회 받게 됩니다.</p>

<p>이용자의 ID가 담긴 문자열 배열 <code>id_list</code>, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 <code>report</code>, 정지 기준이 되는 신고 횟수 <code>k</code>가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>id_list</code>의 길이 ≤ 1,000

<ul>
<li>1 ≤ <code>id_list</code>의 원소 길이 ≤ 10</li>
<li><code>id_list</code>의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.</li>
<li><code>id_list</code>에는 같은 아이디가 중복해서 들어있지 않습니다.</li>
</ul></li>
<li>1 ≤ <code>report</code>의 길이 ≤ 200,000

<ul>
<li>3 ≤ <code>report</code>의 원소 길이 ≤ 21</li>
<li><code>report</code>의 원소는 "이용자id 신고한id"형태의 문자열입니다.</li>
<li>예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.</li>
<li>id는 알파벳 소문자로만 이루어져 있습니다.</li>
<li>이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.</li>
<li>자기 자신을 신고하는 경우는 없습니다.</li>
</ul></li>
<li>1 ≤ <code>k</code> ≤ 200, <code>k</code>는 자연수입니다.</li>
<li>return 하는 배열은 <code>id_list</code>에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>id_list</th>
<th>report</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>["muzi", "frodo", "apeach", "neo"]</code></td>
<td><code>["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]</code></td>
<td>2</td>
<td>[2,1,1,0]</td>
</tr>
<tr>
<td><code>["con", "ryan"]</code></td>
<td><code>["ryan con", "ryan con", "ryan con", "ryan con"]</code></td>
<td>3</td>
<td>[0,0]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제의 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>"ryan"이 "con"을 4번 신고했으나, 주어진 조건에 따라 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리합니다. 따라서 "con"은 1회 신고당했습니다. 3번 이상 신고당한 이용자는 없으며, "con"과 "ryan"은 결과 메일을 받지 않습니다. 따라서 [0, 0]을 return 합니다.</p>

<hr>

<h5>제한시간 안내</h5>

<ul>
<li>정확성 테스트 : 10초</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ❤️ 문제 핵심: <br>
-> 각각 id의 신고횟수를 count하고, 신고받은 횟수가 k이상인 경우에는, 그 신고한 사람들에게 안내 메일을 보내는 것이다. 그 안내 메일을 각 id에게 몇 회씩 보낼 지 return해야한다. 이 문제는 복잡해서, 차근차근 하나씩 처리하는 것이 중요한 문제이다. 문제 속에 정답이 있는 법. 문제가 어떤 흐름으로 흘러가는지, 어떤 제한 조건을 주었는지 한 문장씩 자세히 살펴보고 문제를 풀자! <br><br>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/35290881-6f10-4604-9f47-8f729ffd91c2) <br>
-> 난 문제를 풀기에 앞서, 주석으로 전체적인 알고리즘 풀이를 적고 코딩을 한다. <br>
-> 한 사람이 같은 사람을 여러 번 신고한 경우에는 1회로 친다고 하였기에, 중복을 허용하지 않는 set 자료형을 이용하여 중복을 제거한 후, 다시 list로 바꿔주었다. <br>
-> 다음 report 당한 수를 딕셔너리로 나타냈다. k번 이상인 되는 경우에는 out 배열에 저장했고, report 다시 하나씩 접근하면서, out에 있는 사람을 신고한 경우에는 mail 받을 횟수 딕셔너리의 값을 증가시켜주었다. 그리고 마지막에는 values를 반환해서 결괏값을 얻었다는 것! <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/8180914a-330e-4478-a955-88b80f13eaca) <br>
-> 내 코드는 너무 과하게 딕셔너리를 생성하진 않는지, 같은 동작을 여러 번씩 해서 비효율적인건 아닌가라는 생각을 했다. 그런데, 위의 코드는 아주 간단하고 굳이다! 그래도 set을 활용해서 중복 제거해 준 , report 받은 횟수를 딕셔너리로 만들어준 건 나도 잘한 것 같다 ㅎㅎ 여기서는 out인 사람 배열을 굳이 만들지 않고, 두번째 그 사림 이름이 reports에서 k이상이면, id_list에서 첫번째 사람의 인덱스를 찾아서 answer 배열의 값을 증가시켰다. 여기서 answer 배열을 활용한 것은 정말 잘 한 것 같다!!! <br><br>

## ✔️ What I learned: <br>
-> 요구사항에 대해 어떻게 최적화할 수 있을지 고민하고 코드짜보기!!!! 같은 길이의 리스트에 맞는 결괏값을 하나씩 출력해주어야하는 경우에는 리스트 배열을 하나 더 만들어줘보자!!
