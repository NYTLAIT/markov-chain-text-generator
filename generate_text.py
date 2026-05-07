from clean_text import validate_text, tokenize
from second_order_markov import make_second_order_markov, random_walk_second_order

import requests
import sys

# --- GUTENBERG HELPER ---
def fetch_gutenberg(url):
    '''
    Fetches a plain text corpus from a Project Gutenberg URL.

    Args:
        url (str): Direct URL to a Gutenberg .txt file

    Returns:
        str: Raw text of the book, exits out if failure.
    '''
    try:
        response = requests.get(url)
        response.raise_for_status() # if failed (e.g. 404, 500) will stop the script
        return response.text
    except requests.RequestException as e:
        print(f"Failed to fetch corpus: {e}")
        return None

# --- CLI INTERFACE ---
# dont forget: cd Code/final_generator
def generate_from_cli():
    '''
    Generate text using second order markov chain

    Usage:
        python3 generate_text.py <source> [num_sentences] [start words...]

    Args:
        source: txt file path, Gutenberg txt URL
        num_sentences: Optional - default 6, number of sentences to generate
        start words: Optional - default None: random pick, 1 or 2 words to start the walk from 
    '''
    print('------Processing------')

    # Checking if source exists
    if len(sys.argv) < 2:
        print('Please enter in format: python3 generate_text.py <source> [num_sentences] [start words...]; Source must exist: txt file path, Gutenberg txt URL')
        sys.exit(1) # Error exit sys.exit(0) is success

    # Source
    source = sys.argv[1]

    # Number of sentences
    num_sentences = 6
    if len(sys.argv) >= 3:
        try:
            num_sentences = int(sys.argv[2])
        except ValueError:
            print('Number of sentences must be an integer')

    # Start words
    start = None
    if len(sys.argv) >= 4:
        start = sys.argv[3:]
        if len(start) > 2:
            print('Too many start words, using first 2')
            start = start[:2]

    # fetch from Gutenberg if URL, else validate as file
    if source.startswith("http"):
        raw_text = fetch_gutenberg(source)
    else:
        raw_text = validate_text(source)

    if not raw_text:
        print("Failed to load corpus")
        sys.exit(1)

    # build chain and generate
    tokens = tokenize(raw_text)
    chain = make_second_order_markov(tokens)
    result = random_walk_second_order(chain, num_sentences=num_sentences, start=start)

    print ('------ Generated Text ------')
    print("\n" + result + "\n")

if __name__ == "__main__":
    generate_from_cli()