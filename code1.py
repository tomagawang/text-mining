from imdb import Cinemagoer
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# create an instance of the Cinemagoer class
ia = Cinemagoer()

def movies_review(name,num):
    '''takes movie name and the # of the review returns the first review of it on IMDB'''
    movie = ia.search_movie(name)[0]
    movie_id = movie.movieID
    movie_reviews = ia.get_movie_reviews(movie_id)
    review = movie_reviews['data']['reviews'][num]['content']
    return review

def frequency(movie,num):
    '''clean the data and takes out punctuations and create a dictionary that contains
    the frequency of the word in the text'''
    hist = {}
    fp = movies_review(movie,num)
    strippables = string.punctuation + string.whitespace
    words = fp.split()
    for word in words:
        word = word.strip(strippables)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1
    return hist

def top_10(hist,num=10):
    '''return the top ten words from the text'''
    lst = []
    for word, freq in hist.items():
        lst.append((freq,word))
    lst.sort(reverse=True)

    for freq, word in lst[0:num]:
        print(word, '\t', freq)

def unique_words(hist1,hist2):
    '''compare two text and find the the words that the other text does not have.'''
    lst = []
    for word in hist1.keys():
        if word not in hist2:
            lst.append(word)
    for word in hist2.keys():
        if word not in hist1:
            lst.append(word)
    return lst

def natural_language_processing(text):


def main():
    hist = frequency('Hereditary',0)
    hist2 = frequency('Hereditary',3)
    #print(movies_review('Hereditary',0))
    #print(hist)
    #top_10(hist, num=10)
    print(unique_words(hist,hist2))


if __name__ == '__main__':
    main()