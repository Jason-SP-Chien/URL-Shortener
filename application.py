from flask import Flask, request, redirect

try: #for python3
	from urllib.parse import urlparse
	str_encode = str.encode
except ImportError: #for python2
	from urlparse import urlparse
	str_encode = str

from encoder_decoder import *
from db import *

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def home():
	if request.method=='POST':
		original = str_encode(request.form.get('url'))
		if not urlparse(original).scheme: #in case the scheme is missed (needed to fix the error on AWS)
			original='http://'+original
		id = insert(original)
		shortened_url = toBase62(id)
		short_url=request.base_url+shortened_url
		return short_url
	return request.base_url
		
@application.route('/<short_url>')
def redirect_to_original(short_url):
	decode_url = toBase10(short_url)
	original=select(decode_url)
	return redirect(original)

if __name__ == '__main__':
	table_check()
	application.run(debug=True)