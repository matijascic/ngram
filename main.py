import os
import numpy as np
import matplotlib
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

    # Cleaning data
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

    # Bigram heatmap
    chars = sorted(set(c for key in bigram for c in key.split('|')))
    size = len(chars)
    char_to_idx = {c: i for i, c in enumerate(chars)}

    matrix = np.zeros((size, size))
    for key, count in bigram.items():
        c1, c2 = key.split('|')
        matrix[char_to_idx[c1]][char_to_idx[c2]] = count

    plt.figure(figsize=(12, 10))
    plt.imshow(matrix, cmap='hot')
    plt.xticks(range(size), chars)
    plt.yticks(range(size), chars)
    plt.xlabel('given char')
    plt.ylabel('next char')
    plt.colorbar(label='count')
    plt.title('Bigram Counts')
    plt.tight_layout()
    plt.show()


