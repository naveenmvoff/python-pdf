# Create a class to represent a book with attributes like title, author, and publication year.
class theBook:
    def __init__(self, title, author, publication):
        self.title = title
        self.author = author
        self.publication = publication
    
    def hello(self):
        return f"'{self.title}' by '{self.author}' published in '{self.publication}'"
    
    
    

result1 = theBook("Atomic Habits", "Robert Kiyosaki", "2018")
print(result1.hello())
