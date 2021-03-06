# technojobs-scrape
This is a Scrapy module project which takes in a postcode and radius and scrapes the site for jobs.  The output is in .csv and also to MySQL database.

## Quick start

First, pick a directory, say your home directory, and clone the scrape project to that directory.

```
user@host ~ $ git clone https://github.com/clicktechnology/technojobs-scrape.git
```
Now cd into the cloned folder thus..
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

## Add in MySQL access

To add in access to MySQL, you will need to create a database called job_data and the table for the scraped data.

Luckily, all the work is done for you.  First, we'll copy the SQL script to your database server thus...
```
user@host ~/technojobs-scrape $ scp create_db.sql myusername@mydatabaseserver.com:/tmp
```
Now the file is on your database server, simply run it.
```
myusername@mydatabaseserver.com ~ $ mysql -uroot -p < /tmp/create_db.sql
```
 This creates the database and a user called job_data_user and a password of SECRET_PASSWORD.
 
 Now we just need to modify the pipeline settings so open the settings.py file in technojobs-scrape folder.  Go to 
 line 79 and un-comment the line as shown below. 
 ```
     'scrapy_mysql_pipeline.MySQLPipeline': 300, 
 ```
 
 That's it.  All finished.  Begin scraping!
 
 ## Post script
 
 If you decided to use the database option, a query that would get you all the most relevant latest editions of each job in a nice long list would look like this..
 
 ```
SELECT id, job_id, date_posted, date_scraped, job_title, job_type, location, url, job_description, job_skills 
FROM job_data.jobs_listings_json
WHERE id IN (
    SELECT MAX(id)
    FROM job_data.jobs_listings_json
    GROUP BY job_id
)
ORDER BY date_posted DESC;
 ```
