#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine
# Creating a Magazine
magazine = Magazine("Tech Times", "Technology")
magazine = Magazine("Shibuya Arc", "Anime")
# Creating an Author
author = Author("John Doe")
author = Author("Ivory Marie")

# Adding an Article
article = author.add_article(magazine, "The Future of AI")
article = author.add_article(magazine, "Jujutsu Kaisen")

# Print Article Details
print(f"Article Title: {article.title}")
print(f"Author: {author.name}")
print(f"Magazine: {magazine.name}")



if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
