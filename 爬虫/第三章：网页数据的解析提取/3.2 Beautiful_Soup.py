from bs4 import BeautifulSoup


#
# with open('..\\资料文件\\lzacg_detail.html','w',encoding='utf-8') as f:
#     f.write(data)



with open('..\\资料文件\\lzacg_detail.html','r',encoding='utf-8') as f:
    data = f.read()
soup = BeautifulSoup(data,'lxml')
# data = soup.prettify()
# print(soup.title)
# print(soup.h4.attrs)
# print(soup.h4.string)
# print(soup.html.body.p.br)
# print(soup.head.contents)
# print(soup.head.children)
# for num,i in enumerate(soup.head.contents):
#     print(num,i)

# print(soup.h4.next_siblings)
# for i in soup.h4.next_siblings:
#     print(i)

# result = soup.find_all_next(name='div',attrs={'class':'theme-box' and 'wp-posts-content'})
# result = soup.find_all(class_='theme-box' and 'wp-posts-content')
# print(result)


# uls = soup.select('ul')
# for ul in uls:
#     print(ul.select('li'))


# ps = soup.find(name='h4').next_siblings
# for p in ps:
#     print(p.get_text())

data = soup.title
print(data)


