# Second Order Markov Text Generator
Generate text using a second order markov chain built from a corpus
to better predict the next word when generating and form a structure and theme 
representing the corpus given by way of tokenization

## Features
1. Tokenization: includes punctuations as tokens themselves for a more natural flow
2. Second order markov chain: gain more context to retain structure and theme of given corpus better
3. Modular and documented: files clean, seperated, and reusable

## Files && Functions
Please see docstrings for greater detail
- clean_text.py:
    - validate_text(): validate text (mainly safely check if txt file in this project)
    - tokenize(): turn raw text into list of tokens
    - normalize_tokens(): unused(see features section) - normalize tokens, see doc string for more info
- second_order_marchov.py:
    - make_second_order_markov(): build second order markov chain from list of tokens
    - process_random_walk_second_order_start(): handle flexible starts of random walk when specified to start at specific word or words and handle error
    - random_walk_second_order(): Generate text using a random walk on a second order Markov chain
- random_walk.py:
    - weighted_random_word(): Select word at random given a histogram of {word: frequency} pairs
- generate_text.py:
    - fetch_gutenberg(): fetch a plain text corpus from a Project Gutenberg URL
    - generate_from_cli(): start command line interaction to generate text

## Flow 
1. generate_text -> start the script and get arguments - grabs text from project gutenberg if using as source as well
2. clean_text.py -> validate text source and tokenize into list
3. second_order_markov -> generate second order marchov chain histogram from list
    - generate second order marchov chain histogram from list
    - (callable) random_walk.py -> gets looped through to pick next word
    - continue until given sentence argument satisfied or no other available word and return generated text

## Shapes and Formattings
- command line argument (syntax): python3 generate_text.py (source) [num_sentences] [start words...]
- second order markov chain (shape): {(word1, word2): {next_word: frequency}}

## EXAMPLE COMMAND LINES
- python3 generate_text.py https://www.gutenberg.org/files/5199/5199-0.txt 11
- python3 generate_text.py corpus/Sir_Raymond_Priestley_quote.txt 6 For scientific

## Known Issues and Limitations
- gutenberg.txt has seems to sometimes produce strange text, etc (e.g. got 'b' as a word earlier)
- sentences are counted every period even if just abbreviation
- If adding what word to start on, must include the desired number of sentences
- When inputting desired word to start, it is case sensitive
- Some function names read like isekai anime titles (obnoxiously long)