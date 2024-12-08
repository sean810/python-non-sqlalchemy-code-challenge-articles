class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = name.strip()
        self._articles = []

    @property
    def name(self):
        return self._name  # Name is immutable

    def articles(self):
        """Returns a list of all articles written by the author."""
        return self._articles

    def magazines(self):
        """Returns the unique list of magazines the author has contributed to."""
        if not self._articles:
            return []
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        """Creates and links an article to the author and a magazine."""
        if not isinstance(magazine, Magazine):
            raise ValueError("The magazine must be an instance of the Magazine class")
        if not isinstance(title, str) or not (5 <= len(title.strip()) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        
        article = Article(self, magazine, title.strip())
        return article

    def topic_areas(self):
        """Returns unique categories of magazines the author has contributed to."""
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title.strip()) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class")

        self._title = title.strip()  # Store the title internally
        self.author = author
        self.magazine = magazine

        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title  # Title is immutable, no setter


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name.strip()) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category must be a non-empty string")

        self._name = name.strip()
        self._category = category.strip()
        self._articles = []

    @property
    def name(self):
        return self._name  # Name is immutable

    @name.setter
    def name(self, new_name):
        raise AttributeError("Name is immutable")  # Prevent changes to the name

    @property
    def category(self):
        return self._category  # Category is immutable

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or not new_category.strip():
            raise ValueError("Category must be a non-empty string")
        self._category = new_category.strip()  # Allow updating category but with validation

    def articles(self):
        """Returns a list of all articles in this magazine."""
        return self._articles

    def contributors(self):
        """Returns a unique list of authors who contributed to this magazine."""
        if not self._articles:
            return []
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        """Returns a list of all article titles in this magazine."""
        if not self._articles:
            return []
        return [article.title for article in self._articles]

    def contributing_authors(self):
        """Returns a list of authors who have written more than 2 articles for this magazine."""
        if not self._articles:
            return []
        author_count = {}
        for article in self._articles:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        return [author for author, count in author_count.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        """Returns the magazine with the most articles."""
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine._articles))
