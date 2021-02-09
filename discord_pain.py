def split_words(sentence):
    """Takes a string and converts it into a list of single characters."""

    broken_word = []
    for letter in sentence:
        broken_word += letter
    return broken_word


def recombine_words(broken_sentence):
    """Takes a list and returns a string with two vertical bars before and after each item in the list.
     Intended to be used with the output of the split_words() function."""

    finished_sentence = f"||"
    for number in range(len(broken_sentence)):
        if number == len(broken_sentence) - 1:
            finished_sentence += f"{broken_sentence[number]}||"
            break
        finished_sentence += f"{broken_sentence[number]}||||"
    return finished_sentence


def main(sentence):
    """The main function of the discord pain application. Takes a string as a sentence input."""
    broken_sentence = split_words(sentence=sentence)
    return recombine_words(broken_sentence=broken_sentence)
