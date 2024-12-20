import time
import numpy as np
import matplotlib.pyplot as plt
import connect4

t = time.time()
N = 10  # Nb repetitions
nb_games = [10, 100]
# Array with the percentage of success for player 1 for [10, 100, 1000, 10000] games, N times each
win1 = np.zeros((N, len(nb_games)))
# Array with the percentage of draws for player 1 for [10, 100, 1000, 10000] games, N times each
draw = np.zeros((N, len(nb_games)))

##################################
### START : To do for students ###
##################################

# To do : fill in arrays win1 and draw
# In order to do so, simulate games with the function connect4.run_game()
for i in range(N):
    for j, n in enumerate(nb_games):
        won_games = 0
        draws = 0
        print(time.time() - t)
        for _ in range(n):
            game_result = connect4.run_game()
            if game_result == 1:
                won_games += 1
            if game_result == 0:
                draws += 1
        win1[i][j] = (won_games / n) * 100
        draw[i][j] = (draws / n) * 100
        print("Iteration ", i, "n =", n)


################################
### END : To do for students ###
################################

# Computes and prints the mean for each [10, 100, 1000, 10000]
win1_mean = np.mean(win1, axis=0)
draw_mean = np.mean(draw, axis=0)
print(win1_mean)
print(draw_mean)

# Plot the results in the required format.
# Please do not modify
plt.figure()
for i in range(len(nb_games)):
    plt.scatter(np.full(N, nb_games[i]), win1[:, i], c="blue", s=10)
    plt.scatter(np.full(N, nb_games[i]), draw[:, i], c="red", s=10)
    plt.scatter(nb_games[i], win1_mean[i], c="blue", marker="x", s=50)
    plt.scatter(nb_games[i], draw_mean[i], c="red", marker="x", s=50)
plt.legend(
    ["Victoire joueur 1", "Ex-aequo", "Moyenne victoire joueur 1", "Moyenne ex-aequo"]
)
plt.xlabel("Nombre de parties")
plt.ylabel("Probabilite en %")
plt.xscale("log")
plt.ylim((-10, 100))
# plt.show()

elapsed = time.time() - t
print("Elapsed time: ", elapsed)

plt.savefig("images/MCplot.png", format="png")
