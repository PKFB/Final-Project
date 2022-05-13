import book_recommender

def test_recommender_build():
    """Test that the Recommender class builds a reommend object correctly."""
    example = book_recommender.Recommender()
    assert(example.books[0].title == "Harry Potter and the Half-Blood Prince (Harry Potter  #6)" and example.books[0].author == "J.K. Rowling/Mary GrandPré"
           and example.books[0].avg_rating == '4.57' and example.books[0].length == "long")
    
    assert(example.books[len(example.books) - 1].title == "Las aventuras de Tom Sawyer")
    """
    recommendation1 = recommender.recommendation("J.K. Rowling", 5, "long")
    assert(recommendation1 != None)
    assert (len(recommendation1) > 0)
    assert(recommendation1[0].title == "Harry Potter and the Half-Blood Prince (Harry Potter #6)")
    """

def test_book_build():
    """Test that the Book class builds a book object correctly."""
    example = book_recommender.Book("Harry Potter and the Half-Blood Prince (Harry Potter #6)", "J.K. Rowling", 4.57, "long")
    #assert(book1.compare("J.K. Rowling", 5, "long") == 3)
    assert(example.title == "Harry Potter and the Half-Blood Prince (Harry Potter #6)" and example.author == "J.K. Rowling"
           and example.avg_rating == 4.57 and example.length == "long")
    
def test_recommend():
    """Test that the recommend function is working correctly."""
    example = book_recommender.Recommender()
    example_author_input = input("Please enter if you have a preference for a certain author: ")
    example_rating_input = input("Please enter if you have a preference for a certain rating range (1-5): ")
    example_length_input = input("Please enter if you have a preference for a certain length: ")
    response = example.recommend(example_author_input, example_rating_input, example_length_input)
    
    expected = list((book_recommender.Book("Harry Potter and the Prisoner of Azkaban (Harry Potter  #3)", "J.K. Rowling/Mary GrandPré", "4.56", "435"), 
                    book_recommender.Book("Harry Potter Boxed Set  Books 1-5 (Harry Potter  #1-5)", "J.K. Rowling/Mary GrandPré", "4.78", "2690"),
                    book_recommender.Book("Harry Potter and the Chamber of Secrets (Harry Potter  #2)", "J.K. Rowling/Mary GrandPré", "4.42", "341"),
                    book_recommender.Book("Harry Potter and the Sorcerer's Stone (Harry Potter  #1)", "J.K. Rowling/Mary GrandPré", "4.47", "424")))
    
    assert(response == expected)

def test_recommend_lower():
    pass
    
def test_recommend_na_author():
    pass
    
