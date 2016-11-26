import requests

class Lookup:

    url = "https://itunes.apple.com/lookup"

    tag = "iTunesLookup"

    def __init__(self):
        pass

    def _get_page_content(self, page_url):
        r = requests.get(page_url)
        print(r.content)

    def search_by_id(self, id):
        lookup_url = "%s?id=%d" % (self.url, id)
        print("[%s] search_by_id() url: %s" % (self.tag, lookup_url))
        self._get_page_content(lookup_url)


if __name__ == "__main__":
    lookup = Lookup()
    lookup.search_by_id(909253)
