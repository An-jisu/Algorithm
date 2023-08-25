# [level 0] 이진수 더하기 - 120885 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120885?language=javascript#) 

### 성능 요약

메모리: 33.5 MB, 시간: 2.33 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>이진수를 의미하는 두 개의 문자열 <code>bin1</code>과 <code>bin2</code>가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>return 값은 이진수를 의미하는 문자열입니다.</li>
<li>1 ≤ <code>bin1</code>, <code>bin2</code>의 길이 ≤ 10</li>
<li><code>bin1</code>과 <code>bin2</code>는 0과 1로만 이루어져 있습니다.</li>
<li><code>bin1</code>과 <code>bin2</code>는 "0"을 제외하고 0으로 시작하지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>bin1</th>
<th>bin2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"10"</td>
<td>"11"</td>
<td>"101"</td>
</tr>
<tr>
<td>"1001"</td>
<td>"1111"</td>
<td>"11000"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>10 + 11 = 101 이므로 "101" 을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>1001 + 1111 = 11000 이므로 "11000"을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>


<hr>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/662e1c61-2264-4894-993f-3b93191bee2b) <br>
-> 나는 10진수로 각각 변환해서 더한 후 다시 2진수로 바꿔주었다. 조금 복잡한 과정이될 수 있고, 둘 다 0인 경우에 대한 처리를 따로 빼 주어 조금 복잡한 코드가 되었다. 각 자리수를 가각 더해 반올림해주는 방식도 생각해보자. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/b53b999e-a8c8-4e11-99ac-c5c1986ee0e1) <br>
-> 여기서도 나와 같은 방식의 풀이이지만, 라이브러리 함수들을 이용한 풀이이다. 이 방법도 알아야하고, 직접 이진수를 구하는 코드도 짤 수 있어야 한다!! toString의 인수로 2 를 넘겨서, 2진수의 문자열로 바꿔준다는 뜻이다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/781085f5-7409-432d-a667-9723cf5ddc91) <br>
-> 여기서는 각 자리의 숫자들을 더하고, 0과 1을 넘는 2인 경우에 대한 처리를 해주었다. temp에는 1001+1=1002와 같이 각 자리의 숫자들을 더해준다. 각 자리 숫자를 분리하기 위하여, 문자로 바꾼 것을 배열에 담은 후, 거꾸로 뒤집고 .map((v) => +v)를 처리하였다. 이를 통해 각 자리숫자를 분리하여 배열에 거꾸로 저장하게 된 것이다. 거꾸로 뒤집는 이유는 반올림 처리를 조금 더 편리하게 하기 위한 것이다. 안채워진 부분은 0으로 채우고, 2인 경우는 0으로 바꾸고 다음 것에 1 더해고, 3인 경우에는 1로 바꾸고 다음 것에 2 더해준다. 'Number(temp.reverse().join(""))'를 통해서, '00000000012'이런식으로 되어있을 때, Number를 취해주면, 앞의 0은 무시해준다는 것!!!! 따라서서 앞을 0으로 얼마나 채워도 상관 없다는 것.<br><br>

## ✔️ What I learned: <br>
- js에서는 배열에 요소를 넣는 함수가 push라는 것!! append 아님!!!! <br>
- Number, parseInt, .map((v) => +v): 문자를 숫자로/ toString(): 숫자를 문자로 
