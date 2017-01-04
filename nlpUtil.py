def tokenize_sentence(sentence):
    return sentence.split(' ')
def tokenize_paragraph(paragraph):
    sentences =  paragraph.split('.')
    if sentences[len(sentences)-1].rstrip() == "":
        setences = sentences[:-1]
    return setences
