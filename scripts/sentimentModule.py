from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from databaseModule import MySQL

import nltk.data
import string



class Sentiments:
    def __init__(self):
        self.wordScoresMap = dict()
        self.stemmer = PorterStemmer()

        # Loading external data And setting global variables...
        self.posTagger = nltk.data.load('taggers/maxent_treebank_pos_tagger/english.pickle')
        self.sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')

        self.loadSentiWordnet()

    # This function is called from the constructor and it loads the file
    # contents into data structures
    def loadSentiWordnet(self):
        db = MySQL()
        # db = MySQL("localhost", "root", "admin", "insidetrends")
        words = db.selectAllFrom("words")
        for word in words:  # word[0] -> id, word[1] -> word, word[2] -> score
            self.wordScoresMap[word[1]] = word[2]



            # This function gets passed the score in floating point number

    # and returns a string tag
    def getTag(self, score):
        if score >= 0.75:
            return "strong_positive"

        if score > 0.25 and score < 0.75:
            return "positive"

        if score > 0 and score <= 0.25:
            return "weak_positive"

        if score < 0 and score >= -0.25:
            return "weak_negative"

        if score < -0.25 and score >= -0.75:
            return "negative"

        if score <= -0.75:
            return "strong_negative"

        return "neutral"

    # A list of words is passed into this function and it will return
    # a list of tuples with tagged words [ (word, tag), (word, tag), (word, tag), ... ]
    def posTagWords(self, wordsToTag):
        taggedWords = []

        # tagged = self.posTagger.tag(wordsToTag)
        for tag in wordsToTag:  # tag[0] contains the word and tag[1] contains the tag

            if tag[1].startswith("N"):  # Nouns
                taggedWords.append(tag[0].lower() + "#n")

            if tag[1].startswith("J"):  # Adjective
                taggedWords.append(tag[0].lower() + "#a")

            if tag[1].startswith("R"):  # Adverb
                taggedWords.append(tag[0].lower() + "#r")

            if tag[1].startswith("V"):  # Verb
                taggedWords.append(tag[0].lower() + "#v")

        return taggedWords

    # This function returns tagged tokens
    def posTagTokens(self, tokens):
        return self.posTagger.tag(tokens)

    # This function returns a list of tokens of the string passed here
    def tokenizeString(self, string):
        return word_tokenize(string)

    # This function accepts a list of tuples of tagged words, it looks
    # through the wordScoresMap and finds the scores of the tagged words
    # it then calculates the average of all the scores to get the sentiment
    # values
    def getScore(self, taggedWords):
        score = 0.0
        for taggedWord in taggedWords:

            if taggedWord in self.wordScoresMap:
                score += self.wordScoresMap.get(taggedWord)
            else:
                continue

        score /= len(taggedWords) + 1
        return score

    # This function returns a list of sentences form the string passed here
    def getSentences(self, string):
        return self.sentence_detector.tokenize(string)

    # This function returns a list of tokens from sentence based on punctuation
    def tokenizeStringPunct(self, sentence):
        return word_tokenize(sentence.translate(None, string.punctuation))

    # This function accepts POSTagged tokens as an argument
    # and returns a 'Chunked' set of tokens
    # For further information on this function please visit
    # page 9 of the following URL
    # --> http://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/dongqing-chunking.pdf
    def chunkSentence(self, taggedTokens):
        pattern = "NP: {<JJ>+<NN>+|<NNP>+<NN>+|<NNP>+<CD>*}"
        NPChunker = nltk.RegexpParser(pattern)
        result = NPChunker.parse(taggedTokens)

        return result


def main():
    pass


if __name__ == '__main__': main()
