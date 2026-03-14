class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        return self.page.goto(self.url)