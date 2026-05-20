# Custom Code for Sequence Tokenization
# Sample text
text = "Natural language processing is a fascinating field of study. It involves the analysis of textual data and draws insights from linguistics."


# Custom function for sequence tokenization
def sequence_tokenize(text, delimiter="."):
    sequences = text.split(delimiter)
    sequences = [sequence.strip() for sequence in sequences if sequence.strip()]
    return sequences


# Tokenize into sequences
sequences = sequence_tokenize(text)

# Output: Sequence Tokenization
print("Sequence Tokenization:")
print(sequences)
