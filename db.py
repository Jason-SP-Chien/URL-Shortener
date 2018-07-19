import sqlite3

def table_check(): #check if the table has already existed
	with sqlite3.connect('urls.db') as conn:
		cur = conn.cursor()
		cur.execute("create table if not exists web_urls(ID INTEGER PRIMARY KEY, URL TEXT NOT NULL)")
		
def insert(url): #insert url and return its id at the same time
	with sqlite3.connect('urls.db') as conn:
		cur = conn.cursor()
		res=cur.execute("INSERT INTO web_urls (URL) VALUES (?) ",[url])
		return res.lastrowid

def select(url): #select url from the table by id
	with sqlite3.connect('urls.db') as conn:
		cur = conn.cursor()
		try:
			res=cur.execute('SELECT url FROM web_urls WHERE id=?', [url])
			original=res.fetchone()
			if original:
				return original[0]
			else:
				return None
		except OverflowError: #avoid overflowerror that makes server crash
			pass