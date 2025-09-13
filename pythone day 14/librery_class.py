class Book():
    total_books = 0
    def __init__(self,title,author):
     self.title = title
     self.author = author
     Book.total_books += 1
    def show(self):
       print(f"{self.title} by  {self.author}")
b1 = Book("Song Of Ice and Fire","Goergi R.R. Martin")
b2 = Book("Harry Potter","J.K. Rolling")
b3 = Book("JoJo's Bizzare Adventure", "Hirohiko Araki")

b1.show()
b2.show()
b3.show()
print(f"total books in library:{Book.total_books}")