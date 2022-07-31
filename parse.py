def get_date_from_str(date_str):
    from datetime import datetime
    date_str = date_str.replace(',', '')
    d, m, y = date_str.split()
    m = MONTHS.index(m) + 1
    return datetime.strptime(f'{d} {m} {y}', '%d %m %Y').date()


def parse_news_page(url):
    from bs4 import BeautifulSoup
    import urllib.request

    with urllib.request.urlopen(url) as f:
        content = f.read().decode('utf-8')
    soup = BeautifulSoup(content, features='html.parser')
    _, article, *_ = soup.find_all('article')
    content = article.find('div', {'class': 'entry-content'})
    for gallery in content.find_all('div', {'class': 'gallery'}):
        new_gallery = soup.new_tag('div')
        new_gallery['class'] = 'gallery'
        for a in gallery.find_all('a'):
            link = a.get('href')
            new_img = soup.new_tag('img')
            new_img['src'] = link # !!!!!!
            new_item = soup.new_tag('div')
            new_item['class'] = 'galleryItem'
            new_item.append(new_img)
            new_gallery.append(new_item)
        gallery.replace_with(new_gallery)
    print(content)


if __name__ == '__main__':
    from bs4 import BeautifulSoup
    import urllib.request

    MONTHS = ['Січня', 'Лютого', 'Березня', 'Квітня', 'Травня', 'Червня', 'Липня']

    with urllib.request.urlopen('https://svfoundation.org.ua/novyny/page/3/') as f:
        list_content = f.read().decode('utf-8')

    soup = BeautifulSoup(list_content, features='html.parser')
    articles = soup.find_all('article')
    for article in articles:
        preview_image = article.find('img')
        preview_src = preview_image.get('src')
        print(preview_src)
        header = article.find('h4')
        print(header.text)
        annotation = header.find_next('div')
        print(annotation.text)
        link = annotation.find_next('a')
        print(link.get('href'))
        pub_date = get_date_from_str(link.text.strip())
        print(pub_date)
        _ = parse_news_page(link.get('href'))
        # print(parse_date(link.text.strip(), locale='uk_UA'))

    print(len(articles))
