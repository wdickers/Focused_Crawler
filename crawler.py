from bs4 import BeautifulSoup
from webpage import Webpage

class Crawler:
    def __init__(self,priorityQueue,scorer,pagesLimit, thresh):
        self.visited = []        
        #self.relevantPages=[]
        self.relevantPagesCount = 0
        self.totalPagesCount = len(priorityQueue.queue)
        self.pagesCount = 0
        self.priorityQueue = priorityQueue
        self.scorer = scorer
        self.pagesLimit = pagesLimit
        self.threshold = thresh
    
    def crawl(self):
        #start crawling
        while self.pagesCount <  self.pagesLimit and not self.priorityQueue.isempty():
            work_url = self.priorityQueue.pop()
            self.visited.append(work_url)
            page = Webpage(work_url[1])
            page_score = self.scorer.calculate_score(page.text)
            if (page_score > self.threshold):
                self.relevantPagesCount += 1
                print ("%s, %s") % (-1 * work_url[0], work_url[1])
            self.pagesCount += 1
            for link in page.outgoingUrls:
                url = link.address
                if url != None and url != '':
                    if url.find('?')!= -1:
                        url = url.split('?')[0]
                    if not self.exists(url,self.visited):
                        if url.startswith('http:') and url.find('#') == -1 and not self.exists(url,self.priorityQueue.queue):                            
                            url_score = self.scorer.calculate_score(link.getAllText())
                            self.totalPagesCount +=1
                            tot_score = (page_score + url_score)/2.0
                            if tot_score > threshold:
                                self.priorityQueue.push(((-1 * tot_score),url))

                
    def exists(self,url,alist):
        urlList = [v for p,v in alist]
        return url in urlList
