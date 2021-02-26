class ClassTest:
    def instance_method(self):
        print(f"Called instance_method if {self}") # <__main__.ClassTest object at 0x10c0b43d0>

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}") # <class '__main__.ClassTest'>

    @staticmethod
    def static_method():
        print("Called static_method.")


# for instance method
# when called will gets instance we created passed as parameter. we don't pass it.
# It will be done by default like ClassTest.instance_method(test)
test = ClassTest()
test.instance_method()
# ClassTest.instance_method(test)

# for class method
# when called will gets class passed as parameter. we don't pass it.
# It will be done by default like that ClassTest.class_method(ClassTest)
ClassTest.class_method()

# static method
# own separate functions lives inside class
ClassTest.static_method()


class Book:
    TYPES = ("hardcover", "paperback") # class properties

    def __init__(self, name, book_type, weight): # parameters
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self): # representation
        return f"<Book {self.name}, {self.book_type}, weighting {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight): # parameters
        # return Book(name, Book.TYPES[0], page_weight + 100)
        return cls(name, cls.TYPES[0], page_weight + 100) # correct way to present

    @classmethod
    def paperback(cls, name, page_weight): # parameters
        # return Book(name, Book.TYPES[1], page_weight)
        return cls(name, cls.TYPES[1], page_weight) # correct way to present





# book = Book("Mother", "hardcover", 1500)
# print(book.name)
# print(Book.TYPES)
# print(book)

# for hardcover method
hardbook = Book.hardcover("Harry Potter", 1500)
lightbook = Book.paperback("Harry Potter", 1500)
print(hardbook)
print(lightbook)