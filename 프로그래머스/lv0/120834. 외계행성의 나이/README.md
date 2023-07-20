 # [level 0] 외계행성의 나이 - 120834 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120834?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.07 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 <code>age</code>가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>age</code>는 자연수입니다.</li>
<li><code>age</code> ≤ 1,000</li>
<li>PROGRAMMERS-962 행성은 알파벳 소문자만 사용합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>age</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>23</td>
<td>"cd"</td>
</tr>
<tr>
<td>51</td>
<td>"fb"</td>
</tr>
<tr>
<td>100</td>
<td>"baa"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>age</code>가 23이므로 "cd"를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>age</code>가 51이므로 "fb"를 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li><code>age</code>가 100이므로 "baa"를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/b0abd9da-3ac7-458a-bfea-965e3de8bce3) <br>
-> a 배열에 알파벳으로 넣어놓고, b의 길이를 구하고, length는 <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/76c3aa27-ec65-40bd-bbc2-5baf126ce86f) <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/288908eb-7fe7-4802-a6a0-66fe221c7246) <br>
-> 위와 같이 문자열 자체도 인덱스로 접근할 수 있다는 것 기억하기!! <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/65ed8992-fee4-467e-b9cb-b0981978fd45) <br>
-> 새로운 배열을 생성하는 메서드이다. 위에서는 split과 같은 역할을 하는 것이다. 문자열로 바꾸고, 각각을 Array.from을 통해 각각 배열에 넣은 것이다.<br><br>


##  ✔️ What I learned: <br>
- join함수 사용법: 파이썬-''.join(answer)/ js-answer.join("")   :  순서가 반대라는 것 기억하기!!!<br>
- 여기선 문자열 자체를 인덱스로 접근할 수 있따는 점 기억하기!! 문자열의 인덱스가 중요하다는 것!!!
