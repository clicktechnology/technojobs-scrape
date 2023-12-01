# technojobs-scrape

This is a Scrapy module project which takes in a postcode and radius and scrapes the site for jobs. The output is in .csv and also to MySQL database.

## Quick start

First, pick a directory, say your home directory, and clone the scrape project to that directory.

```bash
git clone https://github.com/clicktechnology/technojobs-scrape.git
```

Now cd into the cloned folder and create a virtual environment.

```bash
cd technojobs-scrape && python -m venv venv
```

Now let's install the requirements for python.

```bash
pip install -r requirements.txt
```

Now run the scrape..

```bash
scrapy crawl jobsjsonld -o output_data.csv
```

The data is in the jobsjson/spiders subdirectory as output_data.csv.

## Add in MySQL access

To add in access to MySQL, you will need to create a database called job_data and the table for the scraped data.

Luckily, all the work is done for you. First, we'll copy the SQL script to your database server thus...

```bash
scp create_db.sql myusername@mydatabaseserver.com:/tmp
```

Now the file is on your database server, simply run it.

```bash
myusername@mydatabaseserver.com ~ $ mysql -uroot -p < /tmp/create_db.sql
```

This creates the database and a user called job_data_user and a password of SECRET_PASSWORD.

Now we just need to modify the pipeline settings so open the settings.py file in technojobs-scrape folder. Go to
line 79 and un-comment the line as shown below.

```bash
    'scrapy_mysql_pipeline.MySQLPipeline': 300,
```

That's it. All finished. Begin scraping!
