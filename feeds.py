# feeds.py
# Generate a list of feed urls from OPML file.
# Currently requires python 2.

import opml


def generate_feed_urls(file_name):
    with open(file_name) as f:
        res = opml.parse(f)
        return res

if __name__ == "__main__":

    file_name = 'Feeder.opml'
    res = generate_feed_urls(file_name)
    for i, val in enumerate(res):
        print i, val.text
        print i, val.xmlUrl
        print i, val.type

