# [level 0] 영어가 싫어요 - 120894 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120894?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.05 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 <code>numbers</code>가 매개변수로 주어질 때, <code>numbers</code>를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>numbers</code>는 소문자로만 구성되어 있습니다.</li>
<li><code>numbers</code>는 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" 들이 공백 없이 조합되어 있습니다.</li>
<li>1 ≤ <code>numbers</code>의 길이 ≤ 50</li>
<li>"zero"는 <code>numbers</code>의 맨 앞에 올 수 없습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"onetwothreefourfivesixseveneightnine"</td>
<td>123456789</td>
</tr>
<tr>
<td>"onefourzerosixseven"</td>
<td>14067</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"onetwothreefourfivesixseveneightnine"를 숫자로 바꾼 123456789를 return합니다.</li>
</ul>

<p>입출력 예 #1</p>

<ul>
<li>"onefourzerosixseven"를 숫자로 바꾼 14067를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/5340f045-57b4-4304-8103-e270455df6e6) <br>
-> 처음엔 numbers에 arr 값이 존재하는 지 검사하려고 했는데, 각 문자열을 어떻게 분리해야할 지에 대한 해결책이 생각나지 않았다. 따라서 arr을 하나씩 접근하며 numbers에 그 값이 존재하는 지 검사하였다. 존재하면 replaceAll 함수를 통해서 모두 그 값에 해당하는 arr의 인덱스 값으로 바꿔주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/c90a6938-98ab-4f2c-b456-885ad8bc4b94) <br>
-> replace 콜백으로 처리하였다. 정규식 표현 부분은 문자열에서 해당하는 문자열이 있으면 해당하는 숫자로 바꿔주는 역할이다. g플래그는 전역 검색으로 해당하는 모든 문자열을 찾는다. 여기서는 정규식에 포함된 문자열을 발견하면 obj[v]를 반환하는 역할이다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/5865469f-5b3f-40cc-b0c9-46a13343a958) <br>
-> number를 하나씩 검사하면서, numbers를 그 문자열들을 기준으로 split한다. 구분자는 포함되지 않기 때문에, 분리 후 다시 그에 해당하는 숫자값으로 join해주었다.<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/6782f780-eef5-4eee-bfe5-93556e5fc5be)
-> 여기서는 reduce함수를 활용해서 특정 문자값을 숫자로 바꾸는 동작을 반복하였다. 여기서는 n에 대해서 배열의 값을 인덱스값으로 변환하게끔 하였다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/e48973b0-6c0a-4b91-981c-8d240e59e388) <br>
-> 나는 for문으로 했는데, 이렇게 forEach문으로도 할 수 있음. 값이랑 인덱스에 동시에 접근 가능하다. <br><br>

## ✔️ What I learned: <br>
- 콜백: 함수의 인자로 함수를 전달하여, 어떤 이벤트가 발생하였거나 특정 작업이 완료되었을 때, 호출되도록 하는 프로그래밍 패턴이다. <br>
- '+'는 js에서 숫자로 변환하는 연산자이다. <br>
- js split(): 구분자로 지정된 문자열은 결과 배열에 포함되지 않는다!!!
