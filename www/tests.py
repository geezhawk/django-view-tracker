from django.test import TestCase

from www.models import Article, Byline
from www.parsers import kt

class ParserTestCase(TestCase):
    def test_parser(self):
        url = 'http://www.khmertimeskh.com/news/21549/minister-of-interior-addresses----gaps----in-democracy/'
        parsed_article = self.load_article(url)
        if parsed_article is not None:
            a = Article.objects.get_or_create(url=parsed_article.url)[0]
            if a.views == parsed_article.views and a.boring(): 
                a.boring = True
            else:
                a.title = parsed_article.title
                a.views = parsed_article.views
                a.pub_date = parsed_article.pub_date
                for name in parsed_article.bylines:
                    byline = Byline.objects.get_or_create(name=name)
                    a.bylines.add(byline[0])
                    

    def load_article(self, url):
        try:
            parser = kt.KTParser
        except KeyError:
            return
        parsed_article = parser(url)
        if not parsed_article.real_article:
            return
        return parsed_article

#class BoringTest(TestCase):
#    def test_boring(self):
#        boring_article = Article(title='test') #some time in the past
