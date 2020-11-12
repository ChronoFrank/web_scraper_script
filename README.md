# web_scraper_script
Simple script made in  python 3.8.5 to extract all html tags and top 5 most used from a given url
there is no external libs used.

## Instructions for development:

#### 1. Create virtualenv:
```
mkvirtualenv web_scraper --python=python3
```
#### 2. Link project dir to postactivate:
```
setvirtualenvproject <project_dir>
```
#### 3. Clone the repository:
```
git clone git@github.com:ChronoFrank/web_scraper_script.git 

or 

git clone https://github.com/ChronoFrank/web_scraper_script.git
```
#### 4. run tests:
```
python tests.py
```

#### 5. run script:
```
python url_scraper.py
```
the script will ask you to enter a valid url to scrape
 ```
 enter url to scrape ->
```

after you enter the url, the script will perform a scrape on the web
page and it'll retrieve the total elements (html tags) used on the page and also
the top 5 most frequently used elements

```
enter url to scrape -> https://www.python.org/
url to analise -> https://www.python.org/
total elements in the webpage -> 31
top 5 most frequently used tags -> {'</a>': 209, '</li>': 163, '</span>': 72, '</div>': 49, '</ul>': 28}
```