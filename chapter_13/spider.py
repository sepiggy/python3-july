import re
from urllib import request


class Spider():
    url = 'https://www.panda.tv/cate/dota1'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    # 获取数据
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    # 分析数据
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for each in root_html:
            name = re.findall(Spider.name_pattern, each)
            number = re.findall(Spider.number_pattern, each)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    # 精炼数据
    def __refine(self, anchors):
        l = lambda anchor: {'name': anchor['name'][0].strip(),
                            'number': anchor['number'][0]}
        return map(l, anchors)

    # 业务逻辑处理
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    # 排序种子
    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    # 展现数据
    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank ' + str(rank + 1) + ' : ' + anchors[rank]['name'] + '   ' + anchors[rank]['number'])

    # 入口方法
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
