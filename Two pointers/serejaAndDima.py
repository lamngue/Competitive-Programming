n = int(input())
cards = list(map(int,input().split()))


def serejaAndDima(n, cards):
    sereja = 0
    dima = 0
    serejaTurn = True
    while len(cards) > 0:
        if (serejaTurn):
            if (len(cards) == 1):
                sereja += cards[0]
            else:
                sereja += max(cards[0], cards[len(cards)-1])
            cards.remove(max(cards[0], cards[len(cards)-1]))
            serejaTurn = False
        else:
            if (len(cards) == 1):
                dima += cards[0]
            else:
                dima += max(cards[0],cards[len(cards)-1])
            cards.remove(max(cards[0], cards[len(cards)-1]))
            serejaTurn = True
    print(sereja, dima)

serejaAndDima(n,cards)
