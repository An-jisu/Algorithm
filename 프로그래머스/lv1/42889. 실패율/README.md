# [level 1] 실패율 - 42889 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42889#qna) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT

### 채점결과

Empty

### 문제 설명

<h2>실패율</h2>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/bde471d8ac/48ddf1cc-c4ea-499d-b431-9727ee799191.png" title="" alt="failture_rate1.png"></p>

<p>슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.</p>

<p>이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.</p>

<ul>
<li>실패율은 다음과 같이 정의한다.

<ul>
<li>스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수</li>
</ul></li>
</ul>

<p>전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.</p>

<h5>제한사항</h5>

<ul>
<li>스테이지의 개수 N은 <code>1</code> 이상 <code>500</code> 이하의 자연수이다.</li>
<li>stages의 길이는 <code>1</code> 이상 <code>200,000</code> 이하이다.</li>
<li>stages에는 <code>1</code> 이상 <code>N + 1</code> 이하의 자연수가 담겨있다.

<ul>
<li>각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.</li>
<li>단, <code>N + 1</code> 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.</li>
</ul></li>
<li>만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.</li>
<li>스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 <code>0</code> 으로 정의한다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>N</th>
<th>stages</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>5</td>
<td>[2, 1, 2, 6, 2, 4, 3, 3]</td>
<td>[3,4,2,1,5]</td>
</tr>
<tr>
<td>4</td>
<td>[4,4,4,4,4]</td>
<td>[4,1,2,3]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
1번 스테이지에는 총 8명의 사용자가 도전했으며, 이 중 1명의 사용자가 아직 클리어하지 못했다. 따라서 1번 스테이지의 실패율은 다음과 같다.</p>

<ul>
<li>1 번 스테이지 실패율 : 1/8</li>
</ul>

<p>2번 스테이지에는 총 7명의 사용자가 도전했으며, 이 중 3명의 사용자가 아직 클리어하지 못했다. 따라서 2번 스테이지의 실패율은 다음과 같다.</p>

<ul>
<li>2 번 스테이지 실패율 : 3/7</li>
</ul>

<p>마찬가지로 나머지 스테이지의 실패율은 다음과 같다.</p>

<ul>
<li>3 번 스테이지 실패율 : 2/4</li>
<li>4번 스테이지 실패율 : 1/2</li>
<li>5번 스테이지 실패율 : 0/1</li>
</ul>

<p>각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.</p>

<ul>
<li>[3,4,2,1,5]</li>
</ul>

<p>입출력 예 #2</p>

<p>모든 사용자가 마지막 스테이지에 있으므로 4번 스테이지의 실패율은 1이며 나머지 스테이지의 실패율은 0이다.</p>

<ul>
<li>[4,1,2,3]</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ❤️ 문제 핵심: <br>
-> 여기서는 실패율에서 인원수를 감소시키는 것, 끝까지 도달한 사람이 없을 경우(0으로 나누게 되는 경우)에 대한 처리해주는 것, 실패율을 기준으로 스테이지(인덱스) 나열해주는 것이 핵심일듯 <br><br>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/862c6f50-ca8a-49c9-a1f4-d4f1af00c877) <br>
-> 스테이지 수만큼 반복문 돌면서, answer에 실패율을 저장하였다. 그런데 처음에는 num 0인 경우(끝까지 도달한 사람이 없을 경우)에 대한 처리를 해주지 않아서, 런타임 오류가 났다. 따라서 0일 경우에는 그냥 0을 answer에 넣도록 하고, 반복문을 계속하게 하였다. 그리고, answer에 저장된 실패율이 큰 것부터 인덱스를 정렬하게 하였다. 딕셔너리를 이용하였다. 열거형을 통해 인덱스와 실패율을 딕셔너리에 같이 저장하였고, value값을 기준으로 key값을 정렬하게 하였다. 그리고, 마지막에 그 정렬한 값의 0번째 값(인덱스값)들만 리스트로 반환하게 하였다. num==0인 경우, 실패율을 기준으로 인덱스 정렬하는 부분에서 조금 시간이 걸렸다. 다른 사람들은 이 부분을 어떻게 처리했는지 유의깊게 살펴보자. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/2943f6b4-e187-4a49-a757-5539489ec9ab) <br>
-> 여기서도 stage 수만큼 반복했다. 그런데, 조금 다른 점은 나처럼 answr, dic 따로 만들지 않고, 바로 딕셔너리에 그 값을 저장했다는 것!!! 효율적!! 그리고 마지막에는 value값을 기준으로, 키값을 정렬하는 것이다. 이렇게, 딕셔너리를 정렬하면 key값을 기준으로 정렬한다는 것!! 나처럼 저렇게 복잡하게 할 필요가 없었다는 것. value기준으로 key정렬하는 건 계속해서 연습해보자. <br>

## ✔️ What I learned: <br>
-> 리스트의 값을 기준으로 인덱스 정렬하는 문제:  <br>
-> sorted에 딕셔너리 전달: key값을 기준으로 key값 정렬해서 리스트로 !!!! <br>
-> 딕셔너리 get함수: 키 값을 기준으로 'value'값을 얻는 
