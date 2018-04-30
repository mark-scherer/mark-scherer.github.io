# tester.py
# tester file for scraper

# setup
from insta import get_data
from insta import get_url
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import urllib3
import xlsxwriter


# test1 - start with URL
username = 'mark_scherer'
profile_url = get_url(username)
data = get_data(profile_url)
print(data)


"""
# test2 - start with HTML file
from insta import get_basics
filename = "../../dummy.html"
HtmlFile = open(filename, 'r', encoding='utf-8')
html = HtmlFile.read()
profile = BeautifulSoup(html, 'lxml')
basic_info = get_basics(profile)
print(basic_info)
"""