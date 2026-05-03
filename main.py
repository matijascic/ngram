import os
import numpy as np
import matplotlib
import tty
import termios
import sys
matplotlib.use("Qt5Agg") 
import matplotlib.pyplot as plt

if __name__ == "__main__":

    DIR="./shakespeare-dataset/"

    dataset={}

    for name in os.listdir(DIR):
        dataset[name]={}
        dataset[name]["title"]=name
        dataset[name]["path"]=DIR+name
        print(dataset[name])
        f=open(dataset[name]["path"], 'r')
        dataset[name]["content"]=f.read()
        f.close()

    for data in dataset.keys():
        content = dataset[data]["content"]
        content = content.replace('\n', ' ')
        content = ''.join(c for c in content if c.isalpha() or c == ' ')
        content = content.lower()
        dataset[data]["content"] = " " + content + " "

    bigram={}
    for data in dataset.keys():
        content=dataset[data]["content"]
        # p(char | char-1) distrib accum
        for i in range(1, len(content)):
            key = content[i] + "|" + content[i-1]
            bigram[key] = bigram.get(key, 0) + 1

    print(bigram)

    # bigram heatmap
    chars = sorted(set(c for key in bigram for c in key.split('|')))
    size = len(chars)
    char_to_idx = {c: i for i, c in enumerate(chars)}

    # adj matrix
    matrix = np.zeros((size, size))
    for key, count in bigram.items():
        c1, c2 = key.split('|')
        matrix[char_to_idx[c1]][char_to_idx[c2]] = count

    # prob/distrib build
    row_sums = matrix.sum(axis=0, keepdims=True) # acc(char) over total dataset
    pmatrix = np.divide(matrix, row_sums, where=row_sums != 0, out=np.zeros_like(matrix)) # actual p(char_(i+1) given char_i)

    # plt.figure(figsize=(12, 10))
    # plt.imshow(pmatrix, cmap='hot')
    # plt.xticks(range(size), chars)
    # plt.yticks(range(size), chars)
    # plt.xlabel('given char')
    # plt.ylabel('next char')
    # plt.colorbar(label='count')
    # plt.title('Shakespear bigram charset distribution')
    # plt.tight_layout()
    # plt.show()

    prob = {}
    for i, c1 in enumerate(chars):
        for j, c2 in enumerate(chars):
            if pmatrix[i][j] > 0:
                prob[c1 + "|" + c2] = pmatrix[i][j]

    print(prob)

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
    prompt = " "
    while True:
        candidates = {key: prob[key] for key in prob if key.endswith('|' + prompt[-1])}
        top5 = dict(sorted(candidates.items(), key=lambda x: -x[1])[:5])

        top_str = "  ".join(f"{k.split('|')[0]}: {v:.2f}" for k, v in top5.items())
        print('\r' + prompt + "| " + top_str + ' ' * (cols - len(prompt) - len(top_str) - 3), end='', flush=True)

        val = get_char()

        if val == '\x1b':
            break
        elif val == '\x7f' and len(prompt) > 1:
            prompt = prompt[:-1]
        elif val.isalpha() or val == ' ':
            prompt += val
        else:
            continue
        
    # auto generation gibber
    import random
    text = " "
    import time
    while True:
        prev = text[-1]
        candidates = {k: v for k, v in prob.items() if k.endswith('|' + prev)}
        if not candidates:
            break
        keys = list(candidates.keys())
        weights = list(candidates.values())
        chosen = random.choices(keys, weights=weights, k=1)[0]
        char = chosen.split('|')[0]
        text += char
        print(char, end='', flush=True)
        time.sleep(0.05)