import urllib
import urllib2

def read_text():
    quotes = open("/Users/Liujia/Downloads/movie_quotes/movie_quotes.txt")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
    check_profanity(content_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=a"+urllib.quote(text_to_check))
    # connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=")
    # connection = urllib2.urlopen('http://www.baidu.com')
    output = connection.read()
    print(output)
    connection.close()

read_text()