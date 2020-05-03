import requests
from bs4 import BeautifulSoup
import re


def categories(cat):
    result = ''
    for i in cat:
        result += f'#{i} '
    return result


def parsing(url):
    page = requests.get(
        url
    )
    page.encoding = 'utf-8'
    base_url = url[:url.find('.site')+5]
    soup = BeautifulSoup(page.text, 'html.parser')



    title = soup.find('div', {
        'class': 'film'
    }).find('h1').text

    

    data = [title]
    if data[3]:
        text = f'''**🎬 [{data[0]} {data[1]}]({base_url+img})**
**🍿Жанр:** {categories(data[2])}
**⭐Рейтинг КиноПоиск:** {data[3]}

🔊{data[4]}

[🎬 Смотреть онлайн]({url})
[👉 Все фильмы](http://f1.ikino.site/filmy/) | [👉 Все сериалы](http://f1.ikino.site/serialy/)'''
    else:
        text = f'''**🎬 [{data[0]} {data[1]}]({base_url+img})**
**🍿Жанр:** {categories(data[2])}

🔊{data[4]}

[🎬 Смотреть онлайн]({url})
[👉 Все фильмы](http://f1.ikino.site/filmy/) | [👉 Все сериалы](http://f1.ikino.site/serialy/)'''
    return text, url
