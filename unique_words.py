from enum import unique
from code1 import frequency

def unique_words(movie, number):
    '''Return the unique words that the first num of review have that does not
    present in other reviews'''
    dic = {}
    lst = []
    for i in range(number):
        hist = frequency(movie, i)
        for w,s in hist.items():
            dic[w] = dic.get(w,0) + s
    for w,s in dic.items():
        if s == 1:
            lst.append(w)
    return lst

def main():
    print(unique_words('Hereditary',10))

if __name__ == '__main__':
    main()
