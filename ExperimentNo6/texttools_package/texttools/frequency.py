def word_frequency(tokens):
    counts = {}
    for t in tokens:
        t = t.lower()
        counts[t] = counts.get(t, 0) + 1
    return counts
