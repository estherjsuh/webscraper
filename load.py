from sqlalchemy import create_engine
from cleanse import availability
from config import DATABASE_URL, user, passw, receiver
import smtplib, ssl
from email.mime.text import MIMEText
from datetime import date
from config import brand

engine = create_engine(DATABASE_URL)

### Loads product data to postgres DB
def load():
    availability.to_sql('product_data', engine, if_exists='append')

try:
    load()
    print('{} rows of data has been loaded to postgres table: product_data'.format(len(availability.index)))
except:
    print('error: data could not be loaded')

### Creates email content ###
price_point= 100
def create_message(dataframe):
    s = '''\
    {} has {} skus in your size xxs-xs Today, {}.
    Today's average price is ${:.2f}.
    There are {} skus within your ${} price point.\
    '''.format(brand, len(availability.index), date.today().strftime("%m/%d/%y"), availability["price"].mean(), len(availability[availability['price']<=price_point]), price_point)
    return s

### Creates server to send email content ###
TO = receiver
SUBJECT = 'Product Availability'
TEXT = create_message(availability)
sender = user
password = passw

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(sender,password)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')
server.quit()
