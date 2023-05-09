# [unrated] 햄버거 만들기 - 133502 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/133502#qna) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>햄버거 가게에서 일을 하는 상수는 햄버거를 포장하는 일을 합니다. 함께 일을 하는 다른 직원들이 햄버거에 들어갈  재료를 조리해 주면 조리된 순서대로 상수의 앞에 아래서부터 위로 쌓이게 되고, 상수는 순서에 맞게 쌓여서 완성된 햄버거를 따로 옮겨 포장을 하게 됩니다. 상수가 일하는 가게는 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 합니다. 상수는 손이 굉장히 빠르기 때문에 상수가 포장하는 동안 속 재료가 추가적으로 들어오는 일은 없으며,  재료의 높이는 무시하여  재료가 높이 쌓여서 일이 힘들어지는 경우는 없습니다.</p>

<p>예를 들어, 상수의 앞에 쌓이는 재료의 순서가 [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]일 때, 상수는 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 햄버거를 포장하고, 아홉 번째 재료가 쌓였을 때, 두 번째 재료와 일곱 번째 재료부터 아홉 번째 재료를 이용하여 햄버거를 포장합니다. 즉, 2개의 햄버거를 포장하게 됩니다.</p>

<p>상수에게 전해지는 재료의 정보를 나타내는 정수 배열 <code>ingredient</code>가 주어졌을 때, 상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>ingredient</code>의 길이 ≤ 1,000,000</li>
<li><code>ingredient</code>의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>ingredient</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[2, 1, 1, 2, 3, 1, 2, 3, 1]</td>
<td>2</td>
</tr>
<tr>
<td>[1, 3, 2, 1, 2, 1, 3, 1, 2]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li>문제 예시와 같습니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li>상수가 포장할 수 있는 햄버거가 없습니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ❤️ 문제 핵심: <br>
-> 1231의 순서대로 나오는 경우, 햄버거 만듦/ 햄버거 총 개수 세기 <br><br>

## 😀 나의 처음 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/236994057-3ba9b7f8-f4f8-47da-ac70-6e38afef04f8.png) <br>
-> 문자열로 바꾸고, "1231"이 존재하지 않을 때까지 반복하면서, 존재하면 answer 1증가시키고, replace하도록 하였다. 그런데 시간초과!!!!! replace가 전체 문자열을 다 검사해서 시간을 많이 잡아먹는 것 같다. 그래서 pop도 시도해보고 했는데, 계속 오류나는 거.....그래서 이 문제는 쉽지만서도 접근방법이 헷갈려서 블로그 참고하였다.<br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/236994913-357514fe-2441-4db6-ad9b-f0bdd2e1a476.png)  <br>
-> ingredient 요소 하나씩 접근하면서, s배열에 넣었다. (s 배열은 i는 1231제거 후 다시 앞으로 돌아갈 수없다는 사실 때문에 새로 만듦) 1231이면 4번 돌면서 pop해줬다. <br>
![image](https://user-images.githubusercontent.com/70849122/236995149-d8bdc148-b123-4332-bee8-a4a90b17b94a.png) <br>
-> 저기 한 줄만 바꿔주어도 오류가 난다. 리스트를 재할당해야하므로 시간초과가 발생하는 것이다. <br>

## 😀 c언어 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/236997141-f68ed441-8b35-41db-9ddf-83dbbc8c24f1.png) <br>
-> (https://velog.io/@dakyommii/C%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%96%84%EB%B2%84%EA%B1%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0) 참고 <br>

## ✔️ What I learned: <br>
- 문자열에서 특정 문자열 제거: replace  (반환값 저장해줘야하므로 replace = s.replace())이런식으로 나타내줘야한다는 것!!! <br>
- 리스트에서 특정 부분 제거는 del이나 pop 사용하자!!!! replace는 시간 많이 잡아먹음 (pop은 끝부터 제거) <br>
- 리스트 문자열로: 반복문 돌면서 요소 하나씩 접근하면서 ''.join() <br>
- 문자열 리스트로: s = list(s) 이렇게 써주면 됨. <br>
- c++ back(): 벡터의 마지막 요소 반환 <
- c++ pop_back(): 값 넣어줌
