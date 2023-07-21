# [level 0] 가위 바위 보 - 120839 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120839?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.26 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 <code>rsp</code>가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를  모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>rsp</code>의 길이 ≤ 100</li>
<li> <code>rsp</code>와 길이가 같은 문자열을 return 합니다.</li>
<li> <code>rsp</code>는 숫자 0, 2, 5로 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>rsp</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"2"</td>
<td>"0"</td>
</tr>
<tr>
<td>"205"</td>
<td>"052"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"2"는 가위이므로 바위를 나타내는 "0"을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"205"는 순서대로 가위, 바위, 보이고 이를 모두 이기려면 바위, 보, 가위를 순서대로 내야하므로 “052”를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/6db90b29-64e1-4f6c-8a32-52dcdaafd514) <br>
-> 문자열을 split함수를 통해 분리해주고, Array.from을 통해서 각 요소를 배열에 넣어주었다. 그리고 그 배열의 요소들에 하나씩 접근하면서, 그 값에 따라 answer에 문자열로 넣어주었다. split 함수의 사용, Array 라이브러리의 from 함수의 사용은 스스로 잘한 것 같다<br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/e0228619-a8b8-4d35-a5b9-8baafb931bcb) <br>
-> 여기서는 파이썬의 딕셔너리 같이 세트 배열을 정의해주었다. 배열 객체의 키와 값을 표현하여 가위바위보 대응값을 정하였다. [...rsp]를 통해 rsp를 가져오고, 배열에 각 요소를 넣어주었고, map함수를 통해서 배열객체의 해당하는 값을 매핑해주었는데, 배열형태이기 때문에 최종적으로 join을 해주었다!<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/8b9813c3-f7fd-48e8-88d9-24d0c5f6f324) <br>
-> 각각을 분리해서 삼항 연산자로 분기하는 것은 처음 생각한 풀이방법인데, 코드로 짜는 것의 접근까지는 어려웠다. split함수로 문자 하나하나 분리해주고, map함수를 통해 각 요소에 같은 함수를 수행해주었다. (2인지, 0인지, 5인지에 따라 값 저장). split의 결과는 배열이므로, map한 결과도 배열이고 최종적으로 join을 해준 것이다. <br><br>

## ✔️ What I learned: <br> 
- js에서는 삼항연산자와 map 함수 굉장히 많이 사용한다는 것!! <br>
- js에서 배열객체를 생성해줌 (객체는 키와 값으로 이루어져 있다!)<br>
- 배열을 map한 함수의 결과는 당연히 배열. 문자열로 변환하기 위해서는 join해줘야 함<br>
- split함수의 결과는 배열! 문자열을 split해주어도 배열 형태로 저장됨됨
