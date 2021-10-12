# https://www.hackerrank.com/challenges/30-abstract-classes/problem

class MyBook():
    def __init__(self, title, author, price):
        self.price = price
        self.author = author
        self.title = title

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")


b_title = input()
b_author = input()
b_price = int(input())
new_novel = MyBook(b_title, b_author, b_price)
new_novel.display()
