from nlpUtil import tokenize_paragraph
def run(paragraph):
    for sentence in tokenize_paragraph(paragraph):
        print sentence

run('Hello world. Hi i am anwesh. I am a Coder.')
