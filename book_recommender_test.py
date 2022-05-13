import book_recommender

from book_recommender import *

def test_book_build(self):
    Book()
   ''books get put into a list'''
   #happy path
    self.assertBook("Paul Auster",203, 'long') 
     
  #edge case
     self.assertBook("Bill Bryson", 26 ,'short') # page count is 299
     self.assertBook("", ,)
        
    def test_recommender_build(self):
    Recommender
    '''What will be tested author, rating, length
    top books, starting index, length for short medium and long'''
   #happy path
        self.assertRecommender()
     
  #edge case
        
        
        
if __name__ == "__main__":
    test_book_build()
    test_recommender_build()
