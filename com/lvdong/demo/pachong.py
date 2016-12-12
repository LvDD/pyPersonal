import requests  ## 导入requests
from bs4 import BeautifulSoup
import os


class qutuw:
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 "
                      "Mobile Safari/537.36"}
    index_url = 'http://www.qutuw.com'

    index_html = requests.get(index_url, headers=headers)
    index_soup = BeautifulSoup(index_html.text, 'lxml')
    sort_list = index_soup.find('nav').find_all('a')

    def main(self):
        for sort in self.sort_list:
            sort_href_ = sort['href']
            sort_title_ = sort['title']
            if sort_title_ != '性感图片':
                continue
            path = str(sort_title_).strip()
            fullpath = "F:/qutuw/" + path
            isExists = os.path.exists(fullpath)
            if not isExists:
                os.makedirs(fullpath)
            os.chdir(fullpath)
            print(sort_title_, sort_href_)
            sort_html = requests.get(self.index_url + sort_href_, headers=self.headers)
            sort_soup = BeautifulSoup(sort_html.text, 'lxml')

            self.find_sort_next(sort_soup)

            # find_sort_next(sort_soup)
            print(sort_title_, "over")
            print('/n')

    def find_sort_next(self, sort_soup):
        self.findSortSoup(sort_soup)
        sort_soup_next = sort_soup.find('div', class_='wf-loading').find('a', title='下一页')
        if sort_soup_next is not None:
            sort_soup_next_href = sort_soup_next['href']
            print(sort_soup_next_href)
            next_soup = self.doRequest(sort_soup_next_href)
            self.find_sort_next(next_soup)

    def findSortSoup(self, sort_soup):
        for section in sort_soup.find_all('section'):
            view = section.find('a')
            if view is not None:
                title_ = section.find('article').find('h2').find('div').getText()
                print(title_)
                view_href_ = view['href']
                requests_view = requests.get(self.index_url + view_href_, headers=self.headers)
                view_soup = BeautifulSoup(requests_view.text, 'lxml')
                page_a = view_soup.find('div', class_="article-pages").find_all('a')[-3]
                max_page_num = page_a.text
                if max_page_num == '1':
                    print(view_href_)
                else:
                    page_view_href = page_a['href']
                    page_view_href_split = page_view_href.split('_')
                    split_prefix = page_view_href_split[0]
                    split_suffix = page_view_href_split[1].split('.')[1]
                    split_num = int(max_page_num)
                    while split_num >= 1:
                        value = split_prefix + '_' + str(split_num) + '.' + split_suffix
                        split_num -= 1
                        # print(value)
                        value_soup = self.doRequest(value)
                        try:
                            src_ = value_soup.find('article').find('img')['src']
                            imgName = src_.split('/')[-1]
                            imgSrc = self.index_url + src_
                            img = requests.get(imgSrc, headers=self.headers)
                            f = open(imgName, 'ab')  ##写入多媒体文件必须要 b 这个参数！！必须要！！
                            f.write(img.content)  ##多媒体文件要是用conctent哦！
                            f.close()
                        except Exception:
                            print("###页面爬取异常：" + value)
                            continue

    def doRequest(self, url):
        html = requests.get(self.index_url + url, headers=self.headers)
        soup = BeautifulSoup(html.text, 'lxml')
        return soup


qutuw = qutuw()
qutuw.main()
