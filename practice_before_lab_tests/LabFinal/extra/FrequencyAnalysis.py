import matplotlib.pylab as plt

# these are the letters we are interested in when dealing with frequency-analysis
# WHITE SPACE IS THE MOST FREQUENT 'LETTER' IN THE ENGLISH ALPHABET !!!
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# the method to do frequency analysis: we just count the occurrences
# of the given characters
def frequency_analysis(text):
    # the text we analyse
    text = text.upper()

    # we use a dictionary to store the letter-frequency pair
    letter_frequencies = {}

    # initialize the dictionary (of course with 0 frequencies)
    for letter in LETTERS:
        letter_frequencies[letter] = 0

    # let's consider the text we want to analyse
    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1

    return letter_frequencies


def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


if __name__ == '__main__':

    plain_text = "Shannon defined the quantity of information produced by a source for example, the quantity in a message by a formula similar to the equation that defines thermodynamic entropy in physics. In its most basic terms, Shannon's informational entropy is the number of binary digits required to encode a message. Today that sounds like a simple, even obvious way to define how much information is in a message. In 1948, at the very dawn of the information age, this digitizing of information of any sort was a revolutionary step. His paper may have been the first to use the word bit, short for binary digit. As well as defining information, Shannon analyzed the ability to send information through a communications channel. He found that a channel had a certain maximum transmission rate that could not be exceeded. Today we call that the bandwidth of the channel. Shannon demonstrated mathematically that even in a noisy channel with a low bandwidth, essentially perfect, error-free communication could be achieved by keeping the transmission rate within the channel's bandwidth and by using error-correcting schemes: the transmission of additional bits that would enable the data to be extracted from the noise-ridden signal. Today everything from modems to music CDs rely on error-correction to function. A major accomplishment of quantum-information scientists has been the development of techniques to correct errors introduced in quantum information and to determine just how much can be done with a noisy quantum communications channel or with entangled quantum bits (qubits) whose entanglement has been partially degraded by noise"
    freq = frequency_analysis(plain_text)
    plot_distribution(freq)
