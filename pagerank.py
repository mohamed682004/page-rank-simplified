import os
import random

# Constants for PageRank calculation
DAMPING = 0.85
SAMPLES = 10000

def main():
    corpus = crawl("corpus")
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")

def crawl(directory):
    pages = {}
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            with open(os.path.join(directory, filename)) as f:
                links = set(f.read().split())
                pages[filename] = links
    return pages

def sample_pagerank(corpus, damping_factor, n):
    page_rank = {page: 0 for page in corpus}
    sample_page = random.choice(list(corpus.keys()))
    for _ in range(n):
        page_rank[sample_page] += 1
        next_pages = corpus[sample_page]
        if len(next_pages) == 0 or random.random() < 1 - damping_factor:
            sample_page = random.choice(list(corpus.keys()))
        else:
            sample_page = random.choice(list(next_pages))

    for page in page_rank:
        page_rank[page] /= n

    return page_rank

if __name__ == "__main__":
    main()
