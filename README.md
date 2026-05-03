# Ngram

![Demo](assets/demo.gif)

A character-level ngram text generation model on different languages.

The probability distribution P(char_i | char_i-1, ..., char_i-n) is computed over characters loaded from plain text datasets (Project Gutenberg, etc).

This is exploratory work — the generated output is gibberish but we can evaluate how close it gets to real language patterns depending on N and the dataset.

N is parameterizable:
- N=2 (bigram): each character depends on the previous one
- N=3, 4+: more context, more coherent, but sparser data

The script has two modes:
- **Interactive**: type characters and see the model's top predictions
- **Auto generation**: the model generates text on its own, printed live

## Setup

```bash
chmod +x dataset.sh
./dataset.sh

python -m venv ./venv
source ./venv/bin/activate
pip install matplotlib numpy unidecode

python main.py
```

Change lang and N at the top of `main.py`.

## Bigram probability heatmaps

When N=2, the model saves a heatmap of the probability matrix.

We can see that latin languages share similar adjacency matrix patterns like q followed by u, th in english, etc.

### English
![English bigram heatmap](heatmap/en.png)

### French
![French bigram heatmap](heatmap/fr.png)

### German
![German bigram heatmap](heatmap/de.png)

### Latin
![Latin bigram heatmap](heatmap/lat.png)

## Datasets

All the datasets links in the script may be broken but were functional [2026-05-03].

## Next steps

- have a good dataset pipeline
- try non latin-based alphabet (was unsuccessful for now)
- dynamically change the generative text using current word length to re-evaluate word likeliness to end (realistic word lengths)
- use asian, african text datasets to evaluate matrices differences across language families
- evaluate statistical closeness to real language