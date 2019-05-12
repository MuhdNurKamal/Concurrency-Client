import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        # print(f"Read {response.content} from {url}")
        pass

def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "http://localhost:5000",
    ] * 100000
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")