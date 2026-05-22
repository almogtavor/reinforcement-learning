P = {
    "B": {"B": 0.1, "K": 0.325, "O": 0.25, "_": 0.325},
    "K": {"B": 0.4, "K": 0, "O": 0.4, "_": 0.2},
    "O": {"B": 0.2, "K": 0.2, "O": 0.2, "_": 0.4},
}
def best_word(K):
    letters = ["B", "K", "O"]
    # V[s] = best probability of completing the word if current letter is s
    V = {s: P[s]["_"] for s in letters}
    best_suffix = {s: s for s in letters}

    for t in range(K - 1, 0, -1):
        new_V = {}
        new_suffix = {}
        for s in letters:
            best_next = max(letters, key=lambda a: P[s][a] * V[a])
            new_V[s] = P[s][best_next] * V[best_next]
            new_suffix[s] = s + best_suffix[best_next]
        V = new_V
        best_suffix = new_suffix
    return best_suffix["B"], V["B"]
word, prob = best_word(5)
print(word, f"{prob:.5f}")
