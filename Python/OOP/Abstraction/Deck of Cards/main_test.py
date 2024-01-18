from main import *

run_cases = [
    ("shuffle_deck", 3, [("9", "Hearts"), ("Jack", "Clubs"), ("10", "Spades")]),
    (
        "deal_card",
        4,
        [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades"), ("10", "Spades")],
    ),
    ("deal_card", 3, [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades")]),
]

submit_cases = run_cases + [
    ("shuffle_deck", 3, [("9", "Hearts"), ("Jack", "Clubs"), ("10", "Spades")]),
    (
        "deal_card",
        4,
        [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades"), ("10", "Spades")],
    ),
    ("deal_card", 3, [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades")]),
    ("shuffle_deck", 3, [("9", "Hearts"), ("Jack", "Clubs"), ("10", "Spades")]),
    ("deal_card", 3, [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades")]),
    ("deal_card", 3, [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades")]),
]


def test(action, num_cards, expected):
    print("---------------------------------")
    print(f"Testing action: {action}, dealing {num_cards} cards")
    print(f"Expected Output: {expected}")
    deck = DeckOfCards()
    random.seed(1)
    result = []

    if action == "shuffle_deck":
        print("Shuffling deck...")
        deck.shuffle_deck()
        print(f"dealing {num_cards} cards")
        for _ in range(num_cards):
            result.append(deck.deal_card())

    elif action == "deal_card":
        for _ in range(num_cards):
            result.append(deck.deal_card())

    print(f"Actual Output: {result}")
    if result == expected:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()