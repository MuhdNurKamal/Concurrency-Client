import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()


def get_session():
    if not getattr(thread_local, "session", None):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        # print(f"Read {len(response.content)} from {url}")
        pass

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "http://localhost:5000",
    ] * 100000
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
