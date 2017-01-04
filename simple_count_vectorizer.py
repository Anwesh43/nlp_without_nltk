from nlpUtil import tokenize_sentence
class SimpleCountVectorizer:
    def __init__(self):
        self.token_map = {}
    def __convertToVectors(self,sentences):
        word_matrix = []
        for sentence in sentences:
            dict1 = {}
            for token in self.token_map.keys():
                dict1[token] = 0
            for word in tokenize_sentence(sentence):
                if word in self.token_map.keys():
                    dict1[word] = dict1[word] + 1
            word_matrix.append(dict1)
        return word_matrix
    def fit(self,sentences):
        for sentence in sentences:
            for word in tokenize_sentence(sentence):
                if not(self.token_map.has_key(word)):
                    self.token_map[word] = 1
        return self.__convertToVectors(sentences)

    def transform(self,sentences):
        return self.__convertToVectors(sentences)
