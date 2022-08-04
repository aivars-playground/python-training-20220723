def fetch(url):
    """make request, return result"""
    pass


def worker(name, queue, results):
    """take requests from queue, do the work, put result"""
    pass


def distribute_work(url, requests, concurrency, results):
    """divide work in batches, collect results"""
    pass


def assault(url, requests, concurrency):
    """entry point to make requests"""
    pass
