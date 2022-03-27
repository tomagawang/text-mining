from code1 import frequency
from code1 import top_10

def top_words(movie,num):
    '''return the top 10 words from the first num of reviews'''
    dic = {}
    for i in range(num):
        hist = frequency(movie,i)
        for w, c in hist.items():
            dic[w] = dic.get(w,0) + c
    return top_10(dic, num=10)

def main():
    top_words('Hereditary',20)

if __name__ == '__main__':
    main()