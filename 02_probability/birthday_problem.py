# When people enter a room,
# what is the probability of the kth person to share birthday
# with someone already in the room?

import random
import matplotlib.pyplot as plt

def plot_probabilities(cumulative_count, trials):
    x = range(1, len(cumulative_count))
    y = [((i * 100) / trials) for i in cumulative_count[1:]]

    plt.plot(x, y, marker='o')
    plt.xlabel("Number of people entering the room")
    plt.ylabel("Probability of finding a matching birthday")

    plt.ylim(0, 100)

    plt.show()

num_annual_days = 365
same_birthday_k_count = [0 for i in range(num_annual_days + 1)]
trials = 100

for i in range(trials):
    same_birthday_map = {}
    for k in range(1, 366):
        birthday = random.randint(1, num_annual_days)
        if birthday in same_birthday_map:
            same_birthday_k_count[k] += 1
            break
        same_birthday_map[birthday] = 1

print(same_birthday_k_count)

cumulative_count = []
total = 0
for count in same_birthday_k_count:
    total += count
    cumulative_count.append(total)

plot_probabilities(cumulative_count, trials)


