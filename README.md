# Shiritori End With Analysis

This repository contains a Python script that analyzes Japanese nouns to determine which characters are most commonly found at the end of these words. The analysis is based on the data from the Unidic-cwj-3.1.1 lexicon and is intended for use in understanding trends in the Japanese word game Shiritori.

## Overview

Shiritori is a Japanese word game in which players take turns to say a word which begins with the final kana of the previous word. The game ends when a player says a word that ends in the kana 'ん'.  
This script takes a CSV file of Japanese nouns from the Unidic-cwj-3.1.1 lexicon, counts the occurrences of the final character of each noun, and ranks them in descending order to find the most common ending characters.

## Data Source

The dataset used in this analysis is derived from the "UniDic-manyo_1603" lexicon, which is part of the UniDic lexicon series provided by The UniDic Consortium. This lexicon is available for download at [UniDic](https://clrd.ninjal.ac.jp/unidic/).
The "UniDic-manyo_1603" lexicon includes comprehensive lexical data of the Japanese language and is instrumental for linguistics research and language processing tasks.

## Usage

To run the script, ensure that you have Python installed on your machine and the necessary permissions to read from the input file and write to the output file.

1. Place the `lex_3_1.csv` file in the `input_data` directory.
2. Run the `main()` function from the command line or an IDE.
3. The script will generate a CSV file in the `result` directory, named `result.csv`, containing the ranked list of ending characters.

## Results

The `result.csv` file will contain two columns: 'word' and 'count'. 'word' represents the ending character, and 'count' represents the number of times that character appears at the end of a noun in the dataset.

---

**Please note that this analysis is for educational and entertainment purposes and may not represent linguistic patterns with complete accuracy.**
