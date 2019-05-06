from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test","Test Author")
        self.assertEqual("Test", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([],b.posts)
        self.assertEqual(len([]),len(b.posts))
        # self.assertEqual(0,len(b.posts)) #another way to implement

    def test_repr(self):
        b = Blog("Test", "Test Author")
        b2 = Blog("My Day", "Rolf")

        self.assertEqual(b.__repr__(),"Test by Test Author (0 posts)")
        self.assertEqual(b2.__repr__(),"My Day by Rolf (0 posts)")

    def test_repr_multiple_posts(self):
        b = Blog("Test", "Test Author")
        b.posts = ["test1"]
        b2 = Blog("My Day", "Rolf")
        b2.posts = ["test3","test4", "test5"]


        self.assertEqual(b.__repr__(),"Test by Test Author (1 post)")
        self.assertEqual(b2.__repr__(),"My Day by Rolf (3 posts)")

