from nlpUtil import tokenize_sentence
def run(sentence):
    for word in tokenize_sentence(sentence):
        print word

run('hello world i am a good kid')
