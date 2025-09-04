class Book:
    def __init__(self, title, author, pages):
        """Initialize a Book object with title, author, pages, and is_read status"""
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = False  # Default to False (not read yet)
    
    def mark_as_read(self):
        """Mark the book as read by setting is_read to True"""
        self.is_read = True
        print(f"'{self.title}' has been marked as read!")
    
    def get_info(self):
        """Return a formatted string with all book details"""
        status = "Read" if self.is_read else "Not Read"
        return f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\nStatus: {status}"
    
    def reading_time(self):
        """Calculate estimated reading time (2 minutes per page)"""
        return self.pages * 2


# Test code
book1 = Book('Harry Potter', 'J.K.Rowling', 309)
print(book1.get_info())
print(f"Reading time: {book1.reading_time()} minutes")
print(f"Reading time in hours: {book1.reading_time()/60:.1f} hours")
book1.mark_as_read()
print("\nAfter marking as read:")
print(book1.get_info())

print("\n" + "="*50)


