# [level 0] 안전지대 - 120866 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120866) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.21 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/124a2c93-da99-4643-96a8-292bb871f553/image.png" title="" alt="image.png"><br>
지뢰는 2차원 배열 <code>board</code>에 1로 표시되어 있고 <code>board</code>에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.<br>
지뢰가 매설된 지역의 지도 <code>board</code>가&nbsp;매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>board</code>는 n * n 배열입니다.</li>
<li>1 ≤ n ≤ 100</li>
<li>지뢰는 1로 표시되어 있습니다.</li>
<li><code>board</code>에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>board</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]</td>
<td>16</td>
</tr>
<tr>
<td>[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]</td>
<td>13</td>
</tr>
<tr>
<td>[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>(3, 2)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선 총 8칸은 위험지역입니다. 따라서 16을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>(3, 2), (3, 3)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선은 위험지역입니다. 따라서 위험지역을 제외한 칸 수 13을 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>모든 지역에 지뢰가 있으므로 안전지역은 없습니다. 따라서 0을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 👑 나의 풀이: <br>
<code>
def solution(board):
    answer = 0
    N = len(board)
    
    #지뢰를 만나면, 그 주변의 값 1로 바꾸기
    for i in range(N):
        for j in range(N):
            if(board[i][j]==1):
                board[i+1][j]==1
                board[i-1][j]==1
                board[i][j-1]==1
                board[i][j+1]==1
                board[i+1][j+1]==1
                board[i+1][j-1]==1
                board[i-1][j+1]==1
                board[i-1][j-1]==1
                
    #1이 아닌 것의 개수 세기
    for i in range(N):
        for k in range(N):
            if(board[i][j]!=1):
                answer+=1

    return answer
</code><br>
-> borad를 돌면서, 1인 경우 주변의 8개의 좌표도 1로 바꿔주고, 마지막에 1이 아닌 경우 count를 하게 해서 코드를 짰다. 하지만, board의 크기를 벗어나는 경우를 생각하지 못했다. 그래서...그 예외를 어떻게 생각하지 고민하다가 코드가 너무 복잡해질 것 같아서, 인터넷 검색을 통해 해결한 문제다... <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/227471731-dd7e7fa8-bb05-499b-aaf3-da0767a0c2ff.png) <br>
-> board의 요소에 하나씩 접근하면서, 1인 경우에는, 사방을 업데이트해서 danger집합에 넣어주었다. danger을 집합으로 처리함으로서, 중복을 제거하였다. 그리고 마지막에는 전체 개수에서 danger 집합의 요소의 갯수를 빼주었다. danger집합에 대해서도 범위를 지정해주어, board를 벗어나는 것에 대한 처리를 해주었다. <br><br>

## ✔ What I learned: <br>
-> enumerate를 통해서, 인덱스와 요소를 동시에 저장하는 것도 계속 써보면서 연습하기!! <br><br>
