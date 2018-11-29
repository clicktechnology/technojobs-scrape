# technojobs-scrape
This is a Scrapy module project which takes in a postcode and radius and scrapes the site for jobs.  The output is in .csv and also to MySQL database.

## How to..

First, pick a directory, say your home directory, and clone the scrape project to that directory.

```
user@host ~ $ git clone https://github.com/clicktechnology/technojobs-scrape.git
```
Now cd into the folder cloned folder thus..
```
user@host ~ $ cd technojobs-scrape
```
Now let's install the requirements for python.

```
user@host ~/technojobs-scrape $ sudo pip install requirements.txt
```
Now run the scrape..
```
user@host ~/technojobs-scrape $ scrapy crawl jobsjsonld -o output_data.csv
```
The data is in the jobsjson/spiders subdirectory as output_data.csv.
