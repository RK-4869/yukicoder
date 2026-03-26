# 1からNまでの合計を求めてください。

#まず与えられた整数Nを標準入力で受け取る。
N = int(input())
#print(N)で出力できた。
#次にどうしたら1からNまでの合計を出せるか考える。
#最初が1と決まっているので、start_Nとおく。
start_N = 1
#合計を0で用意する。
total = 0
#次に、Nまでを繰り返すので
for i in range(1, N+1):
    total += i

print(total)