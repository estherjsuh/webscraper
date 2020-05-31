![alt text](https://github.com/estherjsuh/webscraper/blob/master/static/tech.png)


# Product Availability Webscraper

## Created by Esther Suh

## Description
Web scraper scraps price and availability data from one of my favorite ecommerce website, cleanses the data, loads the data to Postgres and sends me an email (scheduled daily at 11AM through Cron).

URL has been deliberately hidden for privacy reasons.

## How It's Made

- beautifulsoup - HTML parser
- pandas - data manipulation and analysis
- SQLAlchemy - ORM
- smtplib - defines SMTP client session to send emails

The program is written with Python 3.6. The database is PostgreSQL.

## Cronjobs

Scheduling cron jobs with macOS Catalina.

1. Create bash script to run the program in virtual environment

```
#!/bin/sh
source /Users/esther/Desktop/webscraper/venv/bin/activate

python /Users/esther/Desktop/webscraper/load.py
```

2. Add cronjob:

- Type following command in your terminal

```
cronjob -e
```

- Insert following command to vim; the command below will run the bash script everyday at 11am

```
0 11 * * * /bin/bash  /Users/esther/availproj_load_email.sh
```
