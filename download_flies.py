from urllib.request import Request
from urllib.request import urlopen
from urllib.request import urlretrieve
import re
import os

# Шаблон для знахолдження файлу розширення .py та .pyw та .pdf
FILEEXT = r'\"(.+(?:\.pyw*|\.pdf))\"'
SITE = r'https?:\/\/.*?(?=\/)'


def download_files(url, folder):
    """ Завантажує усі python-файли та pdf-файли за у директорію folder.
    """
    html = get_html(url)
    # Створюємо каталог для збереження файлів
    if not os.path.exists(folder):
        os.mkdir(folder)

    site = re.search(SITE, url, re.IGNORECASE).group()
    for file in re.findall(FILEEXT, html, re.IGNORECASE):
        fileurl = site + file  # Повне посилання на файл
        filename = os.path.basename(file)  # Визначаємо ім`я файлу
        print(fileurl)
        # Завантажуємо файл і зберігаємо їх у директорії folder
        urlretrieve(fileurl, os.path.join(folder, filename))


def get_html(url):
    """ Повертає розкодавані дані веб-сторінки за заданою адресою."""
    request = Request(url, headers={"User-Agent": "hello!"})
    response = urlopen(request)
    return str(response.read(), encoding="utf-8", errors="ignore")


rootSite = 'http://www.matfiz.univ.kiev.ua/pages/'
rootPath = "D:\\Repo\\project-management\\"

dirs = {
    "57": "",
}

if __name__ == "__main__":
    # webpage = input("webpage: ")
    # dirpath = input("dirpath: ")
    for page, dir in dirs.items():
        webpage = (rootSite + page).strip()
        dirpath = (rootPath + dir).strip()
        print(f"webpage: {webpage}")
        print(f"dirpath: {dirpath}")

        download_files(webpage, dirpath)
