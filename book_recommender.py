"""A template for a python script deliverable for INST326.

Authors: Trent Williams, Melissa Kavege, Kai Jung
Assignment: Final Project
Date: 4_15_2022

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import sys
import argparse
import pandas as pd

class Book:
    """A class to represent a Book object.
    
    Attributes:
        title (string): The title of a book.
        author (string): The author of a book.
        genre (tuple of strings): A tuple containing the different genres of a book.
        avg_rating (float): The avg_rating for a book based on goodreads reviews.
        length (string): The length of a book either being 'short' or 'long' based on page count.
    """
    def __init__(self, title, author, genre, avg_rating, length):
        pass
        """Initializes a Book object.
        
        Args:
            title (string): See class documentation.
            author (string): See class documentation.
            genre (tuple of strings): See class documentation.
            avg_rating (float): See class documentation.
            length (string): See class documentation.
        """
        
    def books():
        #This function is to read the csv file and be added to a list based on selected elements
        books_df = pd.read_csv("books (1).csv")

        print(books_df)
        
    preferences = ["author","genre", "length", "rating"]
   def combine_prefrences(row):
    return row['author']+ " " +row ['genre']+" "+row['length']+ " "row['rating']
    df["combined_features"] = df.apply(combined_features, axis =1)
    print df["combined_features"].head()
        
class Recommender:
    #recommends 5 books to user at a time
    def recommend(books):
        #movie_index 
        movie_list = df[df['title'].strcontains(book)]
        if len(book_list):
            book_idx = book_list.index[0]
            book_list = sorted(list(),reverse=True, key = ()x:x[1]) [1:6]
    
    
    def __init__(self,book, user_author, user_genre,user_rating,user_length):
        #this is supposed to pass in the attribute from the book class to the recommendation class
        rating_scale = 
        self.book = book
        self.user_author = user_author
        self.user_genre = ()
        self.user_length = ()
        self.user_rating =


    def recommendation(self):
        #This is supposed to append the list of books given to the users based on their preferences
        for book in book_list:
            if book.author == user_author:
                recommendation.append(book)
        for book in book_list:
            if book.genre == user_genre:
                recommendation.append(book)
        for book in book_list:
            if book.rating == user_rating:
                recommendation.append(book)
        for book in book_list:
            if book.length == user_length:
                recommendation.append(book)
    """A class for holding responses from the user about their book preferences.
    
        Attributes:
            preferred_author (String): User response to preferred author question
            preferred_genre (String): User response from terminal about their favorite genres
            preferred_rating (float): User response from terminal about their preferred rating (1 - 5)
            preferred_length (String): User response from terminal about preferred length of a book (short or long)
    """

def main(parameter1, parameter2):
    pass

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('required', type=float, help='This is an example of a required argument.')
    parser.add_argument('--optional', '-o', type=int, default=12, help='This is an example of an optional argument')  
    
    args = parser.parse_args(args_list)

    return args

data = pd.read_csv(r"C:books.csv")

descriptions = data['title'] +' '+ data['author'] + ' ' + data['genre'] +' '+ data['ratings'] +' '+ data['pages']
""""""

if __name__ == "__main__":
    
    arguments = parse_args(sys.argv[1:])
    
    main(arguments.required, arguments.optional)


