# [level 1] 숫자 짝꿍 - 131128 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131128#qna) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.05 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>두 정수 <code>X</code>, <code>Y</code>의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). <code>X</code>, <code>Y</code>의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. <code>X</code>, <code>Y</code>의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.</p>

<p>예를 들어, <code>X</code> = 3403이고 <code>Y</code> = 13203이라면, <code>X</code>와 <code>Y</code>의 짝꿍은 <code>X</code>와 <code>Y</code>에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 <code>X</code> = 5525이고 <code>Y</code> = 1255이면 <code>X</code>와 <code>Y</code>의 짝꿍은 <code>X</code>와 <code>Y</code>에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(<code>X</code>에는 5가 3개, <code>Y</code>에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)<br>
두 정수 <code>X</code>, <code>Y</code>가 주어졌을 때, <code>X</code>, <code>Y</code>의 짝꿍을 return하는 solution 함수를 완성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>X</code>, <code>Y</code>의 길이(자릿수) ≤ 3,000,000입니다.</li>
<li><code>X</code>, <code>Y</code>는 0으로 시작하지 않습니다.</li>
<li><code>X</code>, <code>Y</code>의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>X</th>
<th>Y</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"100"</td>
<td>"2345"</td>
<td>"-1"</td>
</tr>
<tr>
<td>"100"</td>
<td>"203045"</td>
<td>"0"</td>
</tr>
<tr>
<td>"100"</td>
<td>"123450"</td>
<td>"10"</td>
</tr>
<tr>
<td>"12321"</td>
<td>"42531"</td>
<td>"321"</td>
</tr>
<tr>
<td>"5525"</td>
<td>"1255"</td>
<td>"552"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li><code>X</code>, <code>Y</code>의 짝꿍은 존재하지 않습니다. 따라서 "-1"을 return합니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li><code>X</code>, <code>Y</code>의 공통된 숫자는 0으로만 구성되어 있기 때문에, 두 수의 짝꿍은 정수 0입니다. 따라서 "0"을 return합니다.</li>
</ul>

<p><strong>입출력 예 #3</strong></p>

<ul>
<li><code>X</code>, <code>Y</code>의 짝꿍은 10이므로, "10"을 return합니다.</li>
</ul>

<p><strong>입출력 예 #4</strong></p>

<ul>
<li><code>X</code>, <code>Y</code>의 짝꿍은 321입니다. 따라서 "321"을 return합니다.</li>
</ul>

<p><strong>입출력 예 #5</strong></p>

<ul>
<li>지문에 설명된 예시와 같습니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ❤️ 문제 요구 분석과 설계: <br>
-> x와 y의 공통되는 숫자들로 가장 큰 숫자를 만들어 return 하는 것.<br>
-> x와 y의 공통된 숫자를 리스트에 넣고, y에서 삭제하도록 처리해주었다. 그런데 런타임 오류가 나는 것이다. <br>

## 😀 나의 처음 풀이: <br>
```
def solution(X, Y):
    answer = ''
    lis = []
    #공통된 숫자 찾기 (x요소 하나씩 접근하면서 y에 있으면 리스트에 넣고 y에서 replace)
    for i in X:
        if i in Y:
            lis.append(i)
            Y = Y.index(i)
    lis.sort(reverse=True)
    #짝꿍 return 하기(len이 0 인 경우, 0으로만 이루어진 경우 처리)
    if len(lis)==0:
        return '-1'
    elif lis[0]=='0':
        return '0'
    else:
        return ''.join(lis)
```
-> 위와 같은 설계로 풀었는데, 뒤에서 몇 개의 테스트케이스에서 런타임 오류가 나는 것이다. 반복문 안에서 y에 있는지 검사할 때 시간이 너무 오래걸리는 것이다. 처음엔 replace가 문제인다고 생각했다. <br><br>

## 😀 최종 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/ada4e4ef-2867-4d8c-9dd6-66f66d7fa5af) <br>
-> x와 y를 각각 돌면서, 0부9까지 숫자의 개수를 저장해준다. 그리고 9부터 내려오면서, x와 y의 최솟값만큼 answer에 넣어준다. 그리고 예외도 처리해주었다. 각 자리 수는 0~9 사이의 숫자로 이루어져 있다는 사실을 이용한 것이다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/ff7e791f-e692-4802-b018-97bdcba48995) <br>
-> 여기서도 마찬가지!! for문으로 9부터 검사하면서, 개수만큼 answer에 더해주었다. 따로 다시 정렬할 필요가 없음!<br><br>

## ✔️ What I learned: <br>
-> replace는 시간복잡도 클 수 있다는 것/ 비교 횟수를 줄이는 게 중요하다! (딕셔너리 굳)<br><br>
