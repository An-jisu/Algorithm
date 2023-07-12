# [level 0] 최빈값 구하기 - 120812 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120812?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 2.42 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 <code>array</code>가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>array</code>의 길이 &lt; 100</li>
<li>0&nbsp;≤&nbsp;<code>array</code>의 원소 &lt; 1000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>array</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 3, 3, 4]</td>
<td>3</td>
</tr>
<tr>
<td>[1, 1, 2, 2]</td>
<td>-1</td>
</tr>
<tr>
<td>[1]</td>
<td>1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[1, 2, 3, 3, 3, 4]에서 1은 1개 2는 1개 3은 3개 4는 1개로 최빈값은 3입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[1, 1, 2, 2]에서 1은 2개 2는 2개로 최빈값이 1, 2입니다. 최빈값이 여러 개이므로 -1을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>[1]에는 1만 있으므로 최빈값은 1입니다.</li>
</ul>

<hr>

<p>※ 공지 - 2022년 10월 17일 제한 사항 및 테스트케이스가 수정되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d1d51370-7f6e-45ca-b919-6ae9cd4f20a9) <br>
-> 배열의 원소로 올 수 있는 값이 0에서 1000사이의 값이라는 사실을 이용하여, 1000개 짜리의 배열을 만들고, for문을 돌면서 각 숫자에 해당할 때 배열 값을 증가시켜주었다. 그리고 그 최댓값을 구하고, 최댓값이 여러 개이면 -1을 return 하게 하였고, 그렇지 않으면, index값을 반환하게 하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/5043418b-e71c-433b-a8dc-e6d295b045d1) <br>
-> map을 이용하여 해당 객체의 요소와 빈도를 매핑한다 .파이썬에서의 딕셔너리와 비슷하다고 생각하면 됨!!<br><br>

## ✔️ What I learned: <br>
- max 함수 {Math.max().apply(this객체, 배열)}: Math.max(), Math.min() 만을 단독으로 사용하면 적용이 안 되는 경우가 있다. <br>
- map 함수: 반복문 대신, 배열의 요소들에 각각 같은 처리를 할 경우! <br>
- indexOf 함수 (O는 대문자!!!): 배열의 인덱스 값에 접근하는 함수<br>
- 배열 선언 방법: <br>
1. ![image](https://github.com/An-jisu/Algorithm/assets/70849122/73d05bb4-1ccf-423b-b08c-12d3154d8a90) <br>
2. ![image](https://github.com/An-jisu/Algorithm/assets/70849122/0a983383-c7f5-496a-b147-77b62bb4d76e) <br>
3. ![image](https://github.com/An-jisu/Algorithm/assets/70849122/aa1d4178-8539-43b3-98bf-c7f7d45c44e1) <br>
4. ![image](https://github.com/An-jisu/Algorithm/assets/70849122/901af48e-0ab6-49a7-8854-ee421b93831b) <br>
-> 4가지 방법 모두 잘 익히기!! 다 알고 있기!!
