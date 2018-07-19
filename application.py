from flask import Flask, request, render_template, redirect

try: #for python 3
	from urllib.parse import urlparse
	str_encode = str.encode
except ImportError: #for python 2
	from urlparse import urlparse
	str_encode = str

from encoder_decoder import *
from db import *

application = Flask(__name__, template_folder='templates')

@application.route('/', methods=['GET', 'POST'])
def home():
	if request.method=='POST':
		original = str_encode(request.form.get('url'))
		if not urlparse(original).scheme: #in case the scheme is missed
			original='http://'+original
		id = insert(original)
		shortened_url = toBase62(id)
		return render_template('home.html', short_url=request.base_url+shortened_url)
	return render_template('home.html')
		
@application.route('/<short_url>')
def redirect_to_original(short_url):
	decode_url = toBase10(short_url)
	original=select(decode_url)
	return redirect(original)

if __name__ == '__main__':
	table_check()
	application.run(debug=True)