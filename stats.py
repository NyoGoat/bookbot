def get_num_words(text):    
    lc = text
    wordcount = len(lc.split())


    return wordcount
            
def get_let_count(text):    
    lc = text.lower()
    letcount = {}
    for i in lc: 
        if i not in letcount:
            letcount [i] = 1
        else:
            letcount [i] += 1 


    return letcount


def sort_on(text):
    return text["num"]

def make_char_list(text):
    mcl = []
    for char, num in text.items():
        mcl.append ({"char":char,"num":num})
    mcl.sort(reverse=True, key=sort_on)
    return mcl
