cards = input().split()
shuffles = int(input())

deck_size = len(cards) // 2

for _ in range(shuffles):
    shuffled_deck = []
    for i in range(deck_size):
        shuffled_deck.append(cards[i])
        shuffled_deck.append(cards[i + deck_size])
    cards = shuffled_deck

print(shuffled_deck)
