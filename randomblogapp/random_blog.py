import requests, bs4, random, webbrowser

def random_url_get(page_link, class_info, use_list):
    res = requests.get(page_link)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select(class_info)
    for elem in elems:
        use_list.append('{}'.format(elem.get('href')))

# topiclist = []
# article_list = []

# random_url_get('https://hatenablog.com/topics/journal', '.topic-list-item', topiclist)
# random_url_get(random.choice(topiclist), '.entry-link', article_list)
# webbrowser.open(random.choice(article_list), new=2, autoraise=True)



#res = requests.get('https://hatenablog.com/topics/journal')
#elems = soup.select('.topic-list-item')
