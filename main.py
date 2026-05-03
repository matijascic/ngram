import os
import numpy as np
import matplotlib
import tty
import termios
import sys
import random
import time
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

import dataset as ds

if __name__ == "__main__":

    data = ds.load_dataset("jp")

    N = 4

    # n-gram counts
    ngram = {}
    for name in data.keys():
        content = data[name]["content"]
        for i in range(N - 1, len(content)):
            context = content[i - N + 1:i]
            key = content[i] + "|" + context
            ngram[key] = ngram.get(key, 0) + 1

    print(f"Built {len(ngram)} n-grams")

    # normalize to probabilities
    totals = {}
    for key, count in ngram.items():
        context = key.split('|')[1]
        totals[context] = totals.get(context, 0) + count

    prob = {}
    for key, count in ngram.items():
        context = key.split('|')[1]
        prob[key] = count / totals[context]

    print(f"Loaded {len(prob)} probabilities")

    def get_char():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch

    # interactive next token suggestion
    cols = os.get_terminal_size().columns
    print('\n' * 5)
    prompt = " " * (N - 1)
    while True:
        context = prompt[-(N - 1):]
        candidates = {k: v for k, v in prob.items() if k.split('|')[1] == context}
        top5 = dict(sorted(candidates.items(), key=lambda x: -x[1])[:5])

        top_str = "  ".join(f"{k.split('|')[0]}: {v:.2f}" for k, v in top5.items())
        print('\r' + prompt + "| " + top_str + ' ' * (cols - len(prompt) - len(top_str) - 3), end='', flush=True)

        val = get_char()

        if val == '\x1b':
            break
        elif val == '\x7f' and len(prompt) > N - 1:
            prompt = prompt[:-1]
        elif val.isalpha() or val == ' ':
            prompt += val
        else:
            continue

    # auto generation
    print('\n\n--- Auto generation ---\n')
    start = random.choice(list(totals.keys()))
    text = start
    print(start, end='', flush=True)
    while True:
        context = text[-(N - 1):]
        candidates = {k: v for k, v in prob.items() if k.split('|')[1] == context}
        if not candidates:
            text += ' '
            print(' ', end='', flush=True)
            continue
        keys = list(candidates.keys())
        weights = list(candidates.values())
        chosen = random.choices(keys, weights=weights, k=1)[0]
        char = chosen.split('|')[0]
        text += char
        print(char, end='', flush=True)
        time.sleep(0.05)