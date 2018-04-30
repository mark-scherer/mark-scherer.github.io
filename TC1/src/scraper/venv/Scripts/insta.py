"""
insta.py
Source files for Instagram web scraper.
Given url for instagram profile, returns profile data for analytics suite

Note: currently scrapes using selenium, which opens Chrome browser
    ...only functional way to trick HTML robot tags preventing scraping
"""

# setup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver

# get_data
# main method for accessing instagram profile
# returns dictionary of scrapped info
def get_data(profile_url):
    # load profile
    profile_soup = get_profile(profile_url)
    # build result, return
    data = {'basics': get_basics(profile_soup)}
    return data

# get_url
# given username (without @), returns profile url
def get_url(handle):
    return 'https://www.instagram.com/' + handle + '/?hl=en'

def get_basics(profile_soup):
    basics = {}
    basics['username'] = profile_soup.select_one("._rf3jb").get_text()
    basics['name'] = profile_soup.select_one("._kc4z2").get_text()
    basics['bio'] = profile_soup.select_one("._tb97a > span").get_text()
    basics['profile_picture_src'] = profile_soup.select_one("._rewi8")['src']
    basics['num_posts'] = profile_soup.select("._fd86t")[0].get_text()
    basics['num_followers'] = profile_soup.select("._fd86t")[1].get_text()
    basics['num_following'] = profile_soup.select("._fd86t")[2].get_text()
    basics['public'] = is_public(profile_soup)
    return basics

# is_public
# returns if profile with given soup is public
def is_public(profile_soup):
    if len(profile_soup.select("._q8pf2")) > 0:
        return False
    else:
        return True

# get_profile
# return HTML of profile given URL
def get_profile(profile_url):
    """
    attempt to download site using Requests
    raw_profile = simple_get(profile_url)
    profile_soup = BeautifulSoup(raw_profile, 'lxml')
    """

    # attempt to download site using selenium
    driver = webdriver.Chrome()
    driver.get(profile_url)
    profile_soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit

    return profile_soup

# universal webpage download methods - uses Requests
# following code copied from: https://realpython.com/python-web-scraping-practical-introduction/
def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    # imitates real browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    try:
        with closing(get(url, stream=True, headers=headers)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
# end copied code