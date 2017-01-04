from simple_count_vectorizer import SimpleCountVectorizer
from nlpUtil import tokenize_paragraph
def run(sentences_fit,sentences_trans):
    simpleCountVectorizer = SimpleCountVectorizer()
    print "training data"
    print simpleCountVectorizer.fit(sentences_fit)
    print "transformed data"
    print simpleCountVectorizer.transform(sentences_trans)
paragraph_fit = "Everyone you meet here will likely still be here in 10 years. This changes the professional dynamic so that we can all help each other, build relationships, and give real time/effort, without feeling like things have to be transactional. It starts to make sense to invest in activities that pay off in years or decades, not months"
paragraph_trans = "The more years of experience you accumulate in tech, the easier it gets to become negative and closed off to new ideas. It's easy to say No, that's never going to work because experience usually generalizes towards everything failing"
run(tokenize_paragraph(paragraph_fit),tokenize_paragraph(paragraph_trans))
