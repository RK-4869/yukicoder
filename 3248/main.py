#2つの正整数n,xが与えられます。
#異なる2つの正整数a,bが存在するとき、a^x*b = nを満たすかどうか判定してください。
#存在するなら Yes を、存在しないなら No を出力してください。

#まず2つのn,xを標準入力する。
n, x = map(int, input().split())

# print(n)
# print(x) きちんと出力できたことを確認した。

#次に、n,xそれぞれを条件分岐させると
if n > 1 or x == 0:
    print("Yes")
else:
    print("No")