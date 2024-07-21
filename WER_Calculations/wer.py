import string

def remove_punctuation(text):
    
    # Remove punctuation from the list of words.
    
    return [word.translate(str.maketrans('', '', string.punctuation)) for word in text]

def calculate_wer(reference, hypothesis):

    # Convert both reference and hypothesis to lowercase
    reference = [word.lower() for word in reference]
    hypothesis = [word.lower() for word in hypothesis]

    # Remove punctuation
    reference = remove_punctuation(reference)
    hypothesis = remove_punctuation(hypothesis)

    # Create a matrix to store the distances
    d = [[0] * (len(hypothesis) + 1) for _ in range(len(reference) + 1)]

    # Initialize the matrix
    for i in range(len(reference) + 1):
        d[i][0] = i
    for j in range(len(hypothesis) + 1):
        d[0][j] = j

    for i in range(1, len(reference) + 1):
        for j in range(1, len(hypothesis) + 1):
            if reference[i - 1] == hypothesis[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                substitution = d[i - 1][j - 1] + 1
                insertion = d[i][j - 1] + 1
                deletion = d[i - 1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)

    # The WER is the final value in the matrix divided by the length of the reference
    wer = d[len(reference)][len(hypothesis)] / float(len(reference))
    return wer

# Put the original text into the reference_text
# Put the recognition results into the hypothesis_text
reference_text = "THEN THE JUDGE TO SUM UP THE CASE SPOKE THUS YOU SEE THIS MAN WHO HAS MADE SUCH A STIR IN OUR TOWN".split()
hypothesis_text = "Then the judge, to some of the kings, spoke this.".split()

wer = calculate_wer(reference_text, hypothesis_text)
print(f"Word Error Rate (WER): {wer:.3f}")