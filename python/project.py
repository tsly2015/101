page = ...contents of some web page...
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote =  page.find('"', start_quote+1)
url = page[start_quote+1: end_quote]
print url
page = page[end_quote:]

def get_next_target(s):
	start_link = s.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = s.find('"', start_link)
	end_quote =  s.find('"', start_quote+1)
	url = s[start_quote+1: end_quote]
	return url, end_quote

url, endpos = get_next_target(page)

def print_all_links(page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break

print get_page('http://www.sina.com.cn')

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links


#depth-first search
def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			union(tocrawl, get_all_links(get_page(page)))
			crawled.append(page)
	return crawled

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html></html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html></html>')
    except:
        return ""
    return ""

#index = [['udacity', ['http://udacity.com', 'http://npr.org']],
#         ['computing', ['http://acm.org']]]

def add_to_index(index, keyword, url):
	for entry in index:
		if entry[0] == keyword:
			if not url in entry[1]:
				entry[1].append(url)
			return
	index.append([keyword, [url]])

def lookup(index, keyword):
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return []

def add_page_to_index(index, url, content):
	words = content.split()
	for word in words:
		add_to_index(index, word, url)


def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index, page, content)
			union(tocrawl, get_all_links(content))
			crawled.append(page)
	return index

def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""

def split_string(source,splitlist):
	output = []
	atsplit = True
	for char in source:
		if char in splitlist:
			atsplit = True
		else:
			if atsplit:
				output.append(char)
				atsplit = False
			else:
				output[-1] = output[-1] + char
	return output

def record_user_click(index, keyword, url):
	urls = lookup(index, keyword)
	if urls:
		for entry in urls:
			if entry[0] == url:
				entry[1] = entry[1] + 1
	
def add_to_index(index, keyword, url):
	#index: [[keyword, [[url, count], [url, count], ...]], ...]
	for entry in index:
		if entry[0] == keyword:
			for element in entry[1]:
				if element[0] == url:
					return
			entry[1].append([url, 0])
			return
	index.append([keyword, [[url, 0]]])

wang ~ $ traceroute www.colorado.edu