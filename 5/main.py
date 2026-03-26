# #---問題文---
# Ellenは数字のブロックで遊ぼうとしている。
# 数字が書かれているブロックはそれぞれ高さ1で幅はWiである。
# （同じ幅のブロックが複数存在することがある。）

# それらのブロックを高さ1,幅Lの箱の中に入れる。　
# Ellenは大きな箱にどれだけブロックがたくさん入るか気になったが。
# 組み合わせがたくさんあって大変なことに気づいて、すぐに夜になってしまいそうである。
# あなたは、代わりに大きな箱に最大何個のブロックが入るかを求めてください。

#---出力条件---
#求めた数値を返してください。末尾に改行をつけてください。

#箱の幅Lを標準入力する。
L = int(input())
#ブロックの総数Nを標準入力する。
N = int(input())
#Wをリストとして埋め込む。
W = list(map(int, input().split()))

#ソート関数を使用して小さい順に並べる。
W.sort()

#合計の幅をtotal_widthとする。
total_width = 0
#また個数カウンタcountとする。
count = 0

#並び替えた後を1つずつ見ていく
for width in W:
    if total_width + width <= L:
        total_width = total_width + width
        count = count + 1
    else:
        break

print(count)