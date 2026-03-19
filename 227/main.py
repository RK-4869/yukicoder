# `5枚のカードが配られます。それぞれのカードには、1以上13以下のいずれかの整数が書かれています。カードに書かれている整数の組み合わせによって役が決まります。
# 配られた5枚のカードが、以下のいずれの役に該当するかを調べてください。複数の役に該当する場合は、以下で先に記述した方の役に該当するものとします。
# FULL HOUSE
# ある数をちょうど3つと、別の数をちょうど2つ含む。
# THREE CARD
# ある数をちょうど3つ含む。
# TWO PAIR
# ある数をちょうど2つと、別の数をちょうど2つ含む。
# ONE PAIR
# ある数をちょうど2つ含む。`

#標準入力を受け取る。
cards = map(int, input().split())

#
counts = [0]*13
for num in cards:
    counts[num] += 1

#フルハウスならスリーペアとツーペアなので、同じカードが3枚、2枚組がいくつあるかの組み合わせを数える。
three_count = 0
two_count = 0

for c in counts:
    if c == 3:
        three_count += 1
    elif c == 2:
        two_count += 1

#それぞれの組み合わせで役を作成してみる。
if three_count==1 and two_count == 1:
    print("FULL HOUSE")
elif three_count==1:
    print("THREE CARD")
elif two_count==2:
    print("TWO PAIR")
elif two_count==1:
    print("ONE PAIR")
else:
    print("NO HAND")
    