#!/bin/bash

set -e

BASE_DIR="./datasets"
mkdir -p $BASE_DIR/{english,french}

echo "=== Downloading LARGE English & French datasets ==="

########################################
# ENGLISH (original English works)
########################################
echo "[EN] Downloading..."

# Shakespeare
wget -q -O $BASE_DIR/english/hamlet.txt https://www.gutenberg.org/cache/epub/1524/pg1524.txt
wget -q -O $BASE_DIR/english/macbeth.txt https://www.gutenberg.org/cache/epub/1533/pg1533.txt
wget -q -O $BASE_DIR/english/othello.txt https://www.gutenberg.org/cache/epub/1531/pg1531.txt
wget -q -O $BASE_DIR/english/king_lear.txt https://www.gutenberg.org/cache/epub/1532/pg1532.txt

# Jane Austen
wget -q -O $BASE_DIR/english/pride_and_prejudice.txt https://www.gutenberg.org/files/1342/1342-0.txt
wget -q -O $BASE_DIR/english/emma.txt https://www.gutenberg.org/files/158/158-0.txt
wget -q -O $BASE_DIR/english/sense_and_sensibility.txt https://www.gutenberg.org/files/161/161-0.txt

# Charles Dickens
wget -q -O $BASE_DIR/english/great_expectations.txt https://www.gutenberg.org/files/1400/1400-0.txt
wget -q -O $BASE_DIR/english/oliver_twist.txt https://www.gutenberg.org/files/730/730-0.txt
wget -q -O $BASE_DIR/english/a_tale_of_two_cities.txt https://www.gutenberg.org/files/98/98-0.txt

# Mark Twain
wget -q -O $BASE_DIR/english/huckleberry_finn.txt https://www.gutenberg.org/files/76/76-0.txt
wget -q -O $BASE_DIR/english/tom_sawyer.txt https://www.gutenberg.org/files/74/74-0.txt

# Arthur Conan Doyle
wget -q -O $BASE_DIR/english/sherlock_holmes.txt https://www.gutenberg.org/files/1661/1661-0.txt

# Mary Shelley
wget -q -O $BASE_DIR/english/frankenstein.txt https://www.gutenberg.org/files/84/84-0.txt

echo "[EN] Done."

########################################
# FRENCH (original French works)
########################################
echo "[FR] Downloading..."

# Victor Hugo
wget -q -O $BASE_DIR/french/les_miserables.txt https://www.gutenberg.org/files/17489/17489-0.txt
wget -q -O $BASE_DIR/french/notre_dame_de_paris.txt https://www.gutenberg.org/files/2610/2610-0.txt

# Gustave Flaubert
wget -q -O $BASE_DIR/french/madame_bovary.txt https://www.gutenberg.org/files/14155/14155-0.txt
wget -q -O $BASE_DIR/french/sentimental_education.txt https://www.gutenberg.org/files/175/175-0.txt

# Jules Verne
wget -q -O $BASE_DIR/french/voyage_centre_terre.txt https://www.gutenberg.org/files/18857/18857-0.txt
wget -q -O $BASE_DIR/french/vingt_mille_lieues.txt https://www.gutenberg.org/files/5097/5097-0.txt
wget -q -O $BASE_DIR/french/le_tour_du_monde.txt https://www.gutenberg.org/files/103/103-0.txt

# Alexandre Dumas
wget -q -O $BASE_DIR/french/les_trois_mousquetaires.txt https://www.gutenberg.org/files/13951/13951-0.txt
wget -q -O $BASE_DIR/french/comte_de_monte_cristo.txt https://www.gutenberg.org/files/17989/17989-0.txt

# Émile Zola
wget -q -O $BASE_DIR/french/germinal.txt https://www.gutenberg.org/files/5711/5711-0.txt

echo "[FR] Done."

########################################
# SUMMARY
########################################
echo ""
echo "=== Dataset summary ==="
echo "English: $(ls $BASE_DIR/english | wc -l) files"
echo "French:  $(ls $BASE_DIR/french | wc -l) files"