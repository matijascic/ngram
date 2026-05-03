#!/bin/bash

BASE_DIR="./datasets"
mkdir -p "$BASE_DIR"/{english,french,spanish,german,latin}

echo "=== Downloading multilingual datasets ==="

download() {
  URL="$1"
  OUT="$2"
  wget -q -O "$OUT" "$URL" 2>/dev/null
  if [ $? -ne 0 ] || [ ! -f "$OUT" ]; then
    echo "❌ Failed: $OUT"
    rm -f "$OUT"
    return
  fi
  SIZE=$(wc -c < "$OUT")
  if [ "$SIZE" -lt 1000 ]; then
    echo "⚠️ Too small, removing: $OUT"
    rm -f "$OUT"
  else
    echo "✅ $OUT ($SIZE bytes)"
  fi
}

########################################
# ENGLISH
########################################
echo "[EN]"
download "https://www.gutenberg.org/cache/epub/1524/pg1524.txt" "$BASE_DIR/english/hamlet.txt"
download "https://www.gutenberg.org/cache/epub/1533/pg1533.txt" "$BASE_DIR/english/macbeth.txt"
download "https://www.gutenberg.org/cache/epub/1513/pg1513.txt" "$BASE_DIR/english/romeo_juliet.txt"
download "https://www.gutenberg.org/cache/epub/1342/pg1342.txt" "$BASE_DIR/english/pride_prejudice.txt"
download "https://www.gutenberg.org/cache/epub/84/pg84.txt"     "$BASE_DIR/english/frankenstein.txt"
download "https://www.gutenberg.org/cache/epub/1661/pg1661.txt" "$BASE_DIR/english/sherlock_holmes.txt"

########################################
# FRENCH 
########################################
echo "[FR]"
download "https://www.gutenberg.org/cache/epub/14155/pg14155.txt" "$BASE_DIR/french/madame_bovary.txt"
download "https://www.gutenberg.org/cache/epub/5097/pg5097.txt"   "$BASE_DIR/french/vingt_mille_lieues.txt"
download "https://www.gutenberg.org/cache/epub/800/pg800.txt"     "$BASE_DIR/french/tour_du_monde.txt"

########################################
# SPANISH 
########################################
echo "[ES]"
download "https://www.gutenberg.org/cache/epub/2000/pg2000.txt"   "$BASE_DIR/spanish/don_quijote.txt"

########################################
# GERMAN
########################################
echo "[DE]"
download "https://www.gutenberg.org/cache/epub/22367/pg22367.txt" "$BASE_DIR/german/verwandlung.txt"
download "https://www.gutenberg.org/cache/epub/2407/pg2407.txt"   "$BASE_DIR/german/werther.txt"
download "https://www.gutenberg.org/cache/epub/7205/pg7205.txt"   "$BASE_DIR/german/zarathustra.txt"

echo "[LATIN]"
download "https://raw.githubusercontent.com/mathisve/LatinTextDataset/master/latincorpus.txt" "$BASE_DIR/latin/corpus.txt"

########################################
# SUMMARY
########################################
echo ""
echo "=== Dataset summary ==="
for lang in english french spanish german; do
  COUNT=$(ls "$BASE_DIR/$lang" 2>/dev/null | wc -l)
  echo "$lang: $COUNT files"
done
echo "Done."