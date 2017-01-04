def tokenize_sentence(sentence):
    return sentence.split(' ')
def tokenize_paragraph(paragraph):
    def replace_dot(sentence):
        return sentence.replace('.','')
    return map(replace_dot,paragraph.split('. '))
