# [level 0] 짝수는 싫어요 - 120813 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120813?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code> 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td>[1, 3, 5, 7, 9]</td>
</tr>
<tr>
<td>15</td>
<td>[1, 3, 5, 7, 9, 11, 13, 15]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 #1</p>

<ul>
<li>10 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9]를 return합니다.</li>
</ul>

<p>입출력 #1</p>

<ul>
<li>15 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9, 11, 13, 15]를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/bf890848-8aef-44e8-a97f-2d905ad49d53) <br>
-> 반복문을 돌면서, i는 2씩 더해주어, 바로 push를 해주었다. <br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/02cdd497-dd76-4339-8cc3-37a81cb7a159) <br>
-> n만큼 담긴 배열에서 짝수가 아닌 것만 필터링 해주고 있다.<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/153cf807-3b56-40e2-a6f2-fb142da33343) <br>
-> 처음에 배열은 모두 1로 초기화하고, 인덱스 값과 1을 더한 값이 짝수가 아닌 것만 판별하였다. 인덱스를 이용하였다는 점이 인상적이다.<br><br>

## ✔️ What I learned: <br>
- js 변수 선언: var(함수 레벨 스코프, 중복 선언 가능), const(선언과 동시에 초기화), let(중복 선언 불가, 재할당 가능) 
- js에서 배열 넣기: push 함수
- from: 배열을 초기화할 때 사용 <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/f9cb911d-83f9-48d2-9ba7-4f4fcf94339f) <br>
-> 첫번째 인자로 배열, 두번째 인자로 각각에 적용할 함수 <br>
- js에서 많이 쓰이는 array 함수 3대장
  1. map: 새로운 배열을 만들 때 사용, 모든 배열의 값에 함수를 적 <br>
  ![image](https://github.com/An-jisu/Algorithm/assets/70849122/47a45679-f552-48be-8143-b6cc63c9dfdc) <br>
  2. reduce
  3. filter(요소 값, index, 순회하는 대상 객체): 특정 조건 만족하는 새로운 배열 필요 걸러주는 역할 (참 또는 거짓으로 분류해주는 조건을 만족하는 새로운 배열을 반환)<br>
  ![image](https://github.com/An-jisu/Algorithm/assets/70849122/dd2cd223-afc4-4cca-babd-c1eea7d290df)<br>
  - map과 함께 사용 자주!!!<br>
   ![image](https://github.com/An-jisu/Algorithm/assets/70849122/de016492-fe38-4d3e-a3ca-0ccad99e70b7)<br><br>
### -> 배열과 관련된 문제에서는 map, reduce, filter 함수를 잘 사용한다는 것!!!!!!! 반복문 보다는 그 함수들 이용하는 것 연습하기<br>
### 변수는 const나 let으로 주로 사용하자!!!
