"""A template for a python script deliverable for INST326.

Authors: Trent Williams, Melissa Kavege, Kai Jung
Assignment: Final Project
Date: 4_15_2022

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import sys
import argparse
import csv

from numpy import size

""" A class for holding responses from the user about their book preferences.
        Attributes:
            preferred_author (String): User response to preferred author question
            preferred_genre (String): User response from terminal about their favorite genres
            preferred_rating (float): User response from terminal about their preferred rating (1 - 5)
            preferred_length (String): User response from terminal about preferred length of a book (short or long) 
"""
class Recommender:
    def __init__(self):
        self.books = list()
        with open('books.csv', 'r') as csv_file:
            spreadsheet = csv.reader(csv_file)

            next(spreadsheet)
            
            for row in spreadsheet:
                self.books.append(Book(row[1],row[2],row[3],row[7]))
    
    def recommend(self, author, avg_rating, length):
        top_books = list()
        index = 0
        while size(top_books) < 5:
            book = self.books[index]
            if book.author == author and book.avg_rating >= avg_rating and book.length >= length:
                top_books.append(book)
            index += 1
            
        return top_books
                
class Book:
    """A class to represent a Book object.
    
    Attributes:
        title (string): The title of a book.
        author (string): The author of a book.
        genre (tuple of strings): A tuple containing the different genres of a book.
        avg_rating (float): The avg_rating for a book based on goodreads reviews.
        length (string): The length of a book either being 'short' or 'long' based on page count.
    """
    def __init__(self, title, author, avg_rating, length):
        #See class documentation
        self.title = title
        self.author = author
        #self.genre = genre
        self.avg_rating = avg_rating
        self.length = length
            
def main(parameter1, parameter2):
    preferred_author = input("Please enter if you have a preference for a certain author: ")
    preferred_rating = input("Pleaes enter if you have a preference for a certain rating range (1-5): ")
    preferred_length = input("Please enter if you have a preference for a certain length (short, medium, long): ")
    new_Recommender = Recommender()
    recommended_books = new_Recommender.recommend(preferred_author,preferred_rating,preferred_length)
    for book in recommended_books:
        print(book.title)
    
def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--optional', type=float, help='This is an example of a required argument.')
    parser.add_argument('--optional', '-o', type=int, default=12, help='This is an example of an optional argument')  
    
    args = parser.parse_args(args_list)

    return args

if __name__ == "__main__":
    main(None, None)


