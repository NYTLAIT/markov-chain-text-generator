import re

# NOTE: MUST BE USED IN ORDER
# 1. validate_text
# 2. tokenize
# 3. normalize_tokens
# SECOND NOTE: normalized_tokens unused for final_generator and 
# validate text function contains another note about taking in raw string as source

def validate_text(source_text):
    '''
    Checks validation of what can go in the tokenizer

    Args:
        source_text: either a file path or a raw text string.
    Returns:
        raw_text (str): string of the text
    '''
    # Obtain corpus
    try: 
        with open(source_text, 'r') as infile:
            raw_text = infile.read()
    except:
        # NOTE: accepting raw text breaks current CLI syntax but can be used elsewhere otherwise
        # if isinstance(source_text, str):
        #     raw_text = source_text
        # else:
            # print('Invalid text - Accepts only string and txt')
            print('Invalid text - Accepts only txt file path')
            return
    return raw_text
        
def tokenize(raw_text):
    '''
    Tokenizes raw text into a list of tokens

    - Keeps punctuation as separate tokens (.,!?;:)
    - Keeps hyphenated words (on-demand)
    - Keeps apostrophes inside words and trailing (don't, Shackleton's, Iris')

    Args:
        raw_text (str): a string of words

    Returns:
        list[str]: list of tokens
    '''
    # Basic cleaning
    text = raw_text.strip()

    # Tokens include:
    # - words with apostrophes and hyphens
    # - punctuation (markov will deal with that)
    tokens = re.findall(
        r"[a-zA-Z]+(?:[-'][a-zA-Z]+)*|[.,!?;:]",
        text
    )
    return tokens

# UNUSED!
# Clean and normalize token (Ex. Iris' -> iris, relates the words together)    
def normalize_tokens(tokens):
    '''
    Normalizes tokens - to keep related words as one.

    - Removes trailing possessive apostrophes (Iris' -> iris')
    - Normalizes words to lowercase

    Args:
        list[str]: List of cleaned tokens.

    Returns:
        list[str]: List of cleaned tokens.
    '''
    normalized_tokens = []
    for token in tokens:
        # Starts with letter, is a word
        if token[0].isalpha():
            # lowercase
            word = token.lower()
            # "iris'" → "iris"
            word = word.rstrip("'")

            normalized_tokens.append(word)
        else:
            # keep unchanged
            normalized_tokens.append(token)

    return normalized_tokens
