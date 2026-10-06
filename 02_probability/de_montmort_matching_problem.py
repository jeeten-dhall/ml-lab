# Given a shuffled deck of cards of numbers,
# what is the probability that the number on the drawn card
# is the same as the card's number in order of the cards drawn.
# I mean, the 16th card drawn turns out to be the number 16

import random
import matplotlib.pyplot as plt

theoretical_probability_value = 0.6321

def plot_probabilities(deck_sizes, probabilities):
    probabilities_percent = [p * 100 for p in probabilities]
    plt.plot(deck_sizes, probabilities_percent, marker='o')
    plt.axhline(y=theoretical_probability_value*100, linestyle='--', label='Theoretical ≈ 63.21%')

    plt.xlabel("Deck size")
    plt.ylabel("Probability")
    plt.title("Success Probability in De Montmort's Matching Problem")

    plt.ylim(0, 100)
    plt.legend()

    plt.show()

deck_of_cards_count = [10, 25, 50, 75, 100, 200, 300, 400, 500]
game_iterations = 100
probabilities = []

for num_cards in deck_of_cards_count:
    wins = 0
    for i in range(0, game_iterations):
        deck_of_cards = list(range(1, num_cards + 1))
        random.shuffle(deck_of_cards)
        for j in range(0, num_cards):
            if deck_of_cards[j] == j+1:
                wins+=1
                break
    probabilities.append(1.0 * wins/game_iterations)

for x, y, in zip(deck_of_cards_count, probabilities):
    print(f"Deck of {x} cards, winning probability = {y:.2f} %. Deviation from 63% is {(abs(0.63-y)*100):.0f}%")

plot_probabilities(deck_of_cards_count, probabilities)