# Amazon Spider - Web Crawler
#### Web crawler to take the prices of iPhones on Amazon and save them in an .xlsx spreadsheet.
#### Web crawler para pegar os preços dos iPhones na Amazon e salva-los em uma planilha .xlsx

<a href="https://xlsxwriter.readthedocs.io/"><img src="https://img.shields.io/static/v1?label=&message=xlsxwriter&color=lightgray&style=plastic&logoColor=blue" /></a>
<a href="https://scrapy.org/"><img src="https://img.shields.io/static/v1?label=&message=Scrapy&color=green&style=plastic&logoColor=blue" /></a>
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/static/v1?label=%7C&message=Python3.x&color=blue&style=plastic&logo=python&logoColor=blue" /></a>

## How to use
``` bash
$ python3 -m venv env
$ source env/bin/activate
```

## Install requeriments
``` bash
$ pip install -r requirements.txt
```

## Usage

``` bash
$ scrapy runspider amazon_spider.py
```
