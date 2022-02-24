# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# 예제 입력 1 
# 5
# 예제 출력 1 
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


n=int(input())
for i in range(1,n+1):
    print("*"*i+" "*(n*2-i*2)+"*"*i)
for j in range(n-1,0,-1):
    print("*"*j+" "*(n*2-j*2)+"*"*j)