# [unrated] 명예의 전당 (1) - 138477 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/138477) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>"명예의 전당"이라는 TV 프로그램에서는 매일 1명의 가수가 노래를 부르고, 시청자들의 문자 투표수로 가수에게 점수를 부여합니다. 매일 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념합니다.&nbsp;즉 프로그램 시작 이후 초기에 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오르게 됩니다. k일 다음부터는 출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면, 출연 가수의 점수가 명예의 전당에 오르게 되고 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됩니다.</p>

<p>이 프로그램에서는 매일 "명예의 전당"의 최하위 점수를 발표합니다. 예를 들어, <code>k</code> = 3이고, 7일 동안 진행된 가수의 점수가 [10, 100, 20, 150, 1, 100, 200]이라면, 명예의 전당에서 발표된 점수는 아래의 그림과 같이 [10, 10, 10, 20, 20, 100, 100]입니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/b0893853-7471-47c0-b7e5-1e8b46002810/%EA%B7%B8%EB%A6%BC1.png" title="" alt="그림1.png"></p>

<p>명예의 전당 목록의 점수의 개수 <code>k</code>, 1일부터 마지막 날까지 출연한 가수들의 점수인 <code>score</code>가 주어졌을 때, 매일 발표된 명예의 전당의 최하위 점수를 return하는 solution 함수를 완성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>k</code> ≤ 100</li>
<li>7 ≤ <code>score</code>의 길이 ≤ 1,000

<ul>
<li>0 ≤ <code>score[i]</code> ≤ 2,000</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>k</th>
<th>score</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>[10, 100, 20, 150, 1, 100, 200]</td>
<td>[10, 10, 10, 20, 20, 100, 100]</td>
</tr>
<tr>
<td>4</td>
<td>[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]</td>
<td>[0, 0, 0, 0, 20, 40, 70, 70, 150, 300]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li>문제의 예시와 같습니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li>아래와 같이, [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]을 return합니다.
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/5175c32d-44d7-4b13-be47-360bbe6a553c/%EA%B7%B8%EB%A6%BC2.png" title="" alt="그림2.png"></li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>
<hr>


## ❤️ 문제핵심: <br>
-> 명예의 전당에 k명의 사람을 올림(매일 그 날의 가수가 명예의 전당 k번째 사람보다 높으면 명예의전당으로-> k번째 명예의 전당 사람의 점수 배열 반환- 배열의 크기는 score의 수와 같을 것) <br><br>

## 😀 나의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/236729717-12351501-7a3e-45a8-bd2d-507d37da498c.png) <br>
-> 나는 top배열을 따로 생성하였고, 조건을 분기시켰다. top이 k만큼 꽉 차져 있지 않은 경우에는, 마지막 인덱스와 비교하는 것이 아니고, 계속 그냥 append시켜주어야하기 때문이다. 그리고 두번째 조건문엥서는, 만약, 마지막 값이 score[i]의 값보다 작으면 두 값을 바꿔주고, 오름차순으로 정렬하였다. 그리고, 마지막 인덱스 값을 answer에 넣어주었다. 그런데 나의 코드는 분기로인해, 같은 동작들이 여러번 반복되므로, 다른 사람들은 어떻게 효율적으로 코드를 짰을 지 참고하자. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/236729775-d6e2bd28-1c7c-4623-90bb-0ad934422087.png) <br>
-> 여기서 q라는 명에의 전당을 위한 리스트를 만들어주었다. 여러번 분기하지 않고, 그냥 계속 append해서 값을 넣다가, 길이가 더 커지면, 최솟값을 제거시켰다. 그리고 최솟값을 answer 배열에 넣어주었다. 아니 이렇게 간단할 수가......ㅎ<br><br>

## ✔️ What I learned: <br>
-> 뭔가 이런 같은 동작이 반복되는 문제는, 일단 수행해. 그리고 예외조건을 분기로 처리해주자! 그리고, 마지막 인덱스라고 해서 꼭 sort처럼 literally 접근하지 않고, min값을 이용할 수도 있다는 것!! 문제를 문구 자체가 아닌, 다르게 해석하는 방법도 생각해보자!!<br><br>
