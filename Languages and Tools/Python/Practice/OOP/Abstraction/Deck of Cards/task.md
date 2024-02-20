# Deck of Cards

A close friend recently contacted you because he knew you can code. His family enjoys playing card games, but their toddler keeps getting into the card drawers and damaging all their playing cards. He asked if you could write a program that would create a deck of playing cards that they could use instead.

## Challenge

Finish the `DeckOfCards` class. The `SUITS` and `RANKS` of each card have been provided for you as class variables. You won't need to modify them, but you will need to use them.

### Constructor

1. Initialize a `private` empty list called `cards`.
2. Fill that empty list by calling the `create_deck` method within the constructor.

### `create_deck(self)`

This method should create a `(Rank, Suit)` _tuple_ for all 52 cards in the deck and append them to the `cards` list.

_Order matters!_ The cards should be appended to the list in the following order: all ranks of hearts, then diamonds, then clubs, and finally spades. Within each suit, the cards should be ordered from lowest rank (Ace) to highest rank (King).

### `shuffle_deck(self)`

This method should use the [random.shuffle()](https://docs.python.org/3/library/random.html#random.shuffle) method (available from the random package) to shuffle the `cards` in the deck.

### `deal_card(self)`

This method should [.pop](https://docs.python.org/3/tutorial/datastructures.html#:~:text=list.pop,Python%20Library%20Reference.) the first card off the top of the deck (top of the deck is the _end_ of the list) and return it. If there are no cards left in the deck the method should instead return `None`.