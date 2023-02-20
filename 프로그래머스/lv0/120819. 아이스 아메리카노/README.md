# [level 0] 아이스 아메리카노 - 120819 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120819) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 <code>money</code>가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return&nbsp;하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>money</code> ≤ 1,000,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>money</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>5,500</td>
<td>[1, 0]</td>
</tr>
<tr>
<td>15,000</td>
<td>[2, 4000]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>5,500원은 아이스 아메리카노 한 잔을 살 수 있고 잔돈은 0원입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>15,000원은 아이스 아메리카노 두 잔을 살 수 있고 잔돈은 4,000원입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges<br><br>

<hr>

## 🎁 나의 풀이: <br>
-> 처음에는 최대 공약수를 생각하다가... money에서 5500을 한 번씩 빼면서, 0보다 작아질 경우 반복문을 빠져나오도록 복잡하게 코딩하였다. <br>
최대 공약수, 최소공배수, 몫과 나머지로 풀 수 있는 문제 유형들을 익히자! 여기서는, money중에서 5500원으로 몇 번 나누어 떨어지느냐의 문제이니까 몫과 나머지!!  <br><br>

## ⭕ 다른 사람의 풀이: <br>
![](https://velog.velcdn.com/images/asj1966/post/1b632912-b342-477c-a0e9-c9a5ac90bf5c/image.png) <br>
-> 단지 5500으로 나눈 몫과 나머지로 처리 해주어도 됨!! 5500원으로 총 몇 번 나누어 떨어지고, 나머지는 뭐니~ 이거니까! <br>
![](https://velog.velcdn.com/images/asj1966/post/e33957aa-f35b-48e9-b817-e891c12c7339/image.png) <br>
-> divmod(나누어 지는 수, 나누는 수) 하면 몫, 나머지 순서대로 반환해줌
