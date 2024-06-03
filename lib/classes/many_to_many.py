class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)
        if len(self._title) < 5 or len(self._title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("Author must be of type Author")

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError("Magazine must be of type Magazine")


class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        raise AttributeError("Name is an immutable attribute")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if self.articles():
            return list({article.magazine.category for article in self.articles()})
        return None

    def clear_articles(self):
        """Clear all articles associated with this author"""
        Article.all = [article for article in Article.all if article.author != self]


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else:
                raise ValueError("Name must be between 2 and 16 characters")
        else:
            raise TypeError("Name must be a string")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category) > 0:
                self._category = new_category
            else:
                raise ValueError("Category must be longer than 0 characters")
        else:
            raise TypeError("Category must be a string")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else []

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        contributing_authors = [author for author, count in authors.items() if count >= 2]
        return contributing_authors if contributing_authors else []

    @staticmethod
    def top_publisher():
        if Article.all:
            magazine_article_count = {}
            for article in Article.all:
                magazine = article.magazine
                if magazine in magazine_article_count:
                    magazine_article_count[magazine] += 1
                else:
                    magazine_article_count[magazine] = 1
            return max(magazine_article_count, key=magazine_article_count.get)
        return None


