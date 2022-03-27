from code1 import natural_language_processing
from code1 import movies_review

def most_positive_review(movie, num):
    '''return the most postive movie review in the first num of reviews'''
    dic = {}
    for i in range(num):
        score = natural_language_processing(movie,i)
        dic[i] = dic.get(i, 0) + score['pos']
    sort_reviews = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    number = sort_reviews[0][0]
    return movies_review(movie,number)
    
def most_negative_review(movie,num):
    '''return the most postive movie review in the first num of reviews'''
    dic = {}
    for i in range(num):
        score = natural_language_processing(movie,i)
        dic[i] = dic.get(i, 0) + score['neg']
    sort_reviews = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    number = sort_reviews[0][0]
    return movies_review(movie,number)

def main():
    print(most_positive_review('Hereditary',20))
    print(most_negative_review('Hereditary',20))

if __name__ == '__main__':
    main()