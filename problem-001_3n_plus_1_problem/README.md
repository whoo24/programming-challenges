programming-challenges
======================
The 3n+1 problem

PC/UVa 10: 110101/100, 인기도:A, 성공톨: 낯음, 레벨: 1

input)
입력은 일련의 정수썽 i와 j로 구성되며 한 줄에 한 쌍의 수가 입력된다. 모든 정수는 1,000,000보다 작
고 0보다 크다.

output)
각 정수쌍 i와 j에 대해 i와 j를 입력된 순서대로 출력하고 i와 j 사이(i，j 포함)의 최대 사이클 길이를 출
력한다. 이 세 수는 각각 하나씩의 스페이스로 구분되어야 하며 세 수가 모두 한 줄에 출력되어야 하고 입
력된 각 줄마다 한 줄씩 출력해야 한다.


exam)

input:
1 10
100 200
201 210
900 1000

output:
1 10 20
100 200 125
201 210 89
900 1000 174