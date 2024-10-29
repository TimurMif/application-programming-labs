from icrawler.builtin import GoogleImageCrawler

def icrawler(keyw: str, path_to_dir: str):
    """Use icrawler to download in file abs path to image in enthernet"""
    google_crawler = GoogleImageCrawler(storage={'root_dir': path_to_dir})
    filters = dict(size = "large")
    google_crawler.crawl(keyword= keyw, filters =filters, max_num=3)