"""
Authors: Trent Williams, Melissa Kavege, Kai Jung
Assignment: Final Project
Date: 4_15_2022
"""

import csv

""" A class for reading book titles from a csv file into a list of Book objects.
    Returns a list of recommended book titles based on user input.
        Attributes:
           books (list of Book objects): Initially empty when instantiated, a list of Book objects created using data from the csv file.
"""
class Recommender:
    def __init__(self):
        """Initializes the Recommender object"""
        self.books = list()
        with open('books.csv', 'r') as csv_file:
            spreadsheet = csv.reader(csv_file)
        
            """Skips over the first row of the csv file to ignore the headers of each column."""
            next(spreadsheet)
            
            for row in spreadsheet:
                self.books.append(Book(row[1],row[2],row[3], row[7]))
    
    def recommend(self, author_preference, avg_rating_preference, length_preference):
        """Using the user's inputted preferences, the function iterates through the books list and checks 
            for titles with attributes that match. Those titles are then added to a list of the top 5 books to recommend
            to the user.
        
           Args:
               author_preference (string): The user's preferred author.
               avg_rating_preference (float): The user's preffered average rating.
               length_preference (string): The user's preferred length.
               
           Returns:
               list of the first 5 books that mee the user's criteria.             
        """
        criteria = 3 #represents number of available filter criteria
        rankings = []
        for i in range(criteria + 1):
            rankings.append([])
        for book in self.books:
            score = book.compare(author_preference, avg_rating_preference, length_preference)
            if (score > 0): #No need to store
                rankings[score].append(book)
        j = criteria
        recommended_books = []
        while (j > 0):
            if (rankings[j]):
                for k in rankings[j]:
                    if (len(recommended_books) == 5):
                        return recommended_books
                    else:
                        recommended_books.append(k)
            j -= 1
        return recommended_books
        
        """ top_books = list()
        index = 0
        while index < len(self.books) and len(top_books) != 5:
            book = self.books[index]
            if book.author == author_preference and book.avg_rating >= avg_rating_preference and book.length >= length_preference:
                top_books.append(book)
            index += 1
            
        return top_books """
                
class Book:
    """A class to represent a Book object.
    
    Attributes:
        title (string): The title of a book.
        author (string): The author of a book.
        avg_rating (float): The avg_rating for a book based on goodreads reviews.
        length (string): The length of a book either being 'short', 'medium', or 'long' based on page count.
    """
    def __init__(self, title, author, avg_rating, length):
        """Initializes a Book object.
        
           Args:
               title (string): See class documentation.
               author (string): See class documentation.
               avg_rating (float): See class documentation.
               length (string): See class documentation.
        """
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.length = length
        
        #The length is 'short' if the page count is <= 300, 'medium' if page count is > 300 and <= 600, 'long' if page count is larger.
        if self.length <= '300':
            self.length = 'short'
        elif self.length > '300' and self.length <= '600':
                self.length = 'medium'
        else:
            self.length = 'long' 
            
    def compare(self, author, avg_rating, length):
    #Returns a score (integer) of the match of a book to user's preferences
        score = 0
        if (author == self.author):
            score+=1
        if (self.avg_rating >= avg_rating):
            score+=1
        if (self.length == length):
            score+=1
        return score
       
            
if __name__ == "__main__":
    inputted_author = input("Please enter if you have a preference for a certain author: ").title()
    inputted_rating = input("Please enter if you have a preference for a certain rating range (1-5): ")
    inputted_length = input("Please enter if you have a preference for a certain length: ")
    new_Recommender = Recommender()
    recommended_books = new_Recommender.recommend(inputted_author,inputted_rating,inputted_length)
    for book in recommended_books:
        print(book.title)


