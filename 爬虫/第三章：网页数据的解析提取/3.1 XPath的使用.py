from lxml import etree
import requests



def save_file(file,data):
    with open(file,'w',encoding='utf-8') as f:
        f.write(data)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'
}

url_bi = 'https://www.bilibili.com/'
url_lz = 'https://lzacg.cc/'
url_bu = 'https://www.baidu.com'
url_mv = 'https://ssr1.scrape.center/'
url_hp_p = 'https://www.httpbin.org/post'
url_hp_g = 'https://www.httpbin.org/get'



# res = requests.get('https://lzacg.cc/10168',headers=headers)
# save_file('..\\资料文件\\lzacg_detail.html',res.text)


# with open('..\\资料文件\\lzacg_detail.html','r',encoding='utf-8') as f:
#     data = f.read()



# HTML = etree.HTML(data)
# result = etree.tostring(HTML,encoding="utf-8",method='html')
# print(result.decode('utf-8'))



# html = etree.parse('..\\资料文件\\lzacg_detail.html',etree.HTMLParser())
# result = etree.tostring(html,encoding="utf-8",method='html')
# print(result.decode('utf-8'))



# html = etree.parse('..\\资料文件\\lzacg_detail.html',etree.HTMLParser())
# result = html.xpath('//div[@data-nav="posts"]/*')

# result2 = [result.index(i) for i in result if 'h4' in str(i)]
# galgame_str = ''
# for i in result[1:result2[1]]:
#     print(etree.tostring(i,encoding='utf-8',method='html').decode('utf-8'))

    # 获取该节点下全部文本，包括br隔断的文字
    # text_list = i.xpath('.//text()')
    # full_text = ''.join(text_list).strip()
    # print(full_text)



# html = etree.parse('..\\资料文件\\lzacg_detail.html',etree.HTMLParser())
# result = html.xpath('//div[@data-nav="posts" and contains(@class,"theme-box")]/*/text()')
# end_index = result.index('游戏截图')
# gal = '\n'.join(result[1:end_index])
# print(gal)



# html = etree.parse('..\\资料文件\\lzacg_detail.html',etree.HTMLParser())
# result = html.xpath('//div[@data-nav="posts"]/p//text()')
# print(result)













































