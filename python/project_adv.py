def crawl_web(seed, max_pages):
	tocrawl = [seed]
	crawled = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled and len(crawled) < max_pages:
			union(tocrawl, get_all_links(get_page(page)))
			crawled.append(page)
	return crawled

#max depth
def crawl_web(seed,max_depth):    
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled

    