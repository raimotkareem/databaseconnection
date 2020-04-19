import requests
import bs4
import psycopg2



url = 'https://www.jumia.com.ng/watches-sunglasses/?q=ladies+watch&page=1'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.content,'html.parser')
html = soup.find_all('div',class_='sku -gallery')

con = psycopg2.connect(database = "", user = "postgres", password = "", host = "", port = "")
print ("Opened database successfully")

cur = con.cursor()
cur.execute('''CREATE TABLE TOM
      (LINK          TEXT   NOT NULL,
      NAME           TEXT    NOT NULL,
      PRICE            INT     NULL
      );''')
print("Table created successfully")

cur.execute("INSERT INTO TOM (LINK,NAME,PRICE) VALUES ('www.co.com','tola',6)");

con.commit()
print("Record inserted successfully")
con.close()







