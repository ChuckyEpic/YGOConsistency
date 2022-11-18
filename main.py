import math, time, itertools

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


def generate_hands(deck, hand_size):
    result_list = list(itertools.combinations(deck, hand_size))
    for item in result_list:
        global tests
        tests += 1
        if test(item):
            global successful_tests
            successful_tests += 1


def test(hand):
    for n in range(len(combos)):
        if set(combos[n]).issubset(hand):
            return True
    return False


t0 = time.time()
generate_hands(deck, hand_size)
t1 = time.time()
print(successful_tests / tests * 100, "%")
print(t1 - t0)
