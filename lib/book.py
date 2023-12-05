class Book:
    def __init__(self, title, page_count):
        if isinstance(page_count, int):
            self._title = title
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def get_title(self):
        return self._title

    def set_title(self, value):
        self._title = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_page_count, set_page_count)
    title = property(get_title, set_title)
