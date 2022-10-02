import math

deck = [
    "Lulu", "Lulu", "Lulu",
    "Lili", "Lili", "Lili",
    "Laolao", "Laolao", "Laolao",
    "Jiji", "Jiji", "Jiji",
    "Nyanyan", "Nyanyan",
    "Toutou",
    "Kauwloon", "Kauwloon", "Kauwloon",
    "Qinglong", "Qinglong", "Qinglong",
    "Chuche", "Chuche",
    "Xuanwu",
    "Desires", "Desires",
    "E Tele",
    "Prosperity", "Prosperity", "Prosperity",
    "Gamma", "Gamma", "Gamma",
    "Driver",
    "Nibiru", "Nibiru", "Nibiru",
    "Imperm", "Imperm", "Imperm",
    "Called By",
]
combos = [
    ["Lulu", "Lili"],
    ["Lulu", "Jiji"],
    ["Lulu", "Laolao"],
    ["Lulu", "Nyanyan"],
    ["Lulu", "Toutou"],
    ["Lulu", "Kauwloon"],
    ["Lulu", "Qinglong"],
    ["Lulu", "E Tele"],
    ["Lulu", "Foolish Goods"],
    ["Lili", "Jiji"],
    ["Lili", "Nyanyan"],
    ["Lili", "Toutou"],
    ["Lili", "Kauwloon"],
    ["Lili", "Qinglong"],
    ["Lili", "E Tele"],
    ["Lili", "Foolish Goods"],
    ["Jiji", "Jiji"],
    ["Jiji", "Nyanyan"],
    ["Jiji", "Laolao"],
    ["Jiji", "Toutou"],
    ["Jiji", "Kauwloon"],
    ["Jiji", "E Tele"],
    ["Jiji", "Foolish Goods"],
    ["Laolao", "Nyanyan"],
    ["Laolao", "Toutou"],
    ["Laolao", "Kauwloon"],
    ["Laolao", "E Tele"],
    ["Laolao", "Qinglong", "Gamma"],
    ["Laolao", "Qinglong", "Driver"],
    ["Lulu", "Lulu"],
    ["Laolao", "Foolish Goods"],
    ["E Tele", "Foolish Goods"],
    ["Nyanyan", "Foolish Goods"],
    ["Toutou", "Foolish Goods"],
    ["Toutou", "E Tele", "Qinglong"],
    ["Toutou", "E Tele", "Kauwloon"],
    ["Toutou", "E Tele", "E Tele"],
    ["Toutou", "E Tele", "Gamma"],
    ["Toutou", "E Tele", "Driver"],
    ["Toutou", "E Tele", "Nyanyan"]
]
hand_size = 5
total_tests = math.factorial(len(deck)) / math.factorial(len(deck) - hand_size)
tests = 0
successful_tests = 0


def get_card(hand_size, deck_size, hand=[]):
    if len(hand) == hand_size:
        global tests
        tests += 1
        print(round(tests / total_tests * 100, 2), "%")
        if test(hand):
            global successful_tests
            successful_tests += 1
    else:
        for n in range(len(hand), hand_size):
            for o in range(deck_size):
                if o not in hand:
                    hand.append(o)
                    get_card(hand_size, deck_size, hand)
                    hand.remove(o)
            return


def test(ids):
    for n in range(len(combos)):
        hand = convert(ids)
        if set(combos[n]).issubset(hand):
            return True
    return False


def convert(ids):
    hand = []
    for n in range(len(ids)):
        hand.append(deck[ids[n]])
    return hand


get_card(hand_size, len(deck))
print(tests)
print(successful_tests)
print(successful_tests / tests * 100, "%")
