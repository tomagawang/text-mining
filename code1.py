from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

def movies_review(name):
    '''takes movie name and returns the first review of it on IMDB'''
    movie = ia.search_movie(name)[0]
    movie_id = movie.movieID
    movie_reviews = ia.get_movie_reviews(movie_id)
    review = movie_reviews['data']['reviews'][0]['content']
    return review

def frequency(data):
    '''takes a data and returns the freqeuncy of each word in that text'''
    
    pass

def main():
    print(movies_review('Hereditary'))


if __name__ == '__main__':
    main()