'''use The bag-of-words model  to calculate the similarity of two texts'''
def similarity_text(textone,texttwo):
    '''
    input: two texts
    output: the similarity of two texts
    '''
    #step1: split the text into words
    def cut_word(text):
        return [word for word in jieba.cut(text) if word not in stopwords]
        




