import string

try: #python 2
    from string import ascii_lowercase
    from string import ascii_uppercase
except ImportError: #python3
    from string import lowercase as ascii_lowercase
    from string import uppercase as ascii_uppercase

def toBase62(id_n, b=62): #decimal to base62
	base62=ascii_uppercase+ascii_lowercase+string.digits #concatenate to base62
	enc_id_n=''
	while id_n:
		r=id_n%b
		id_n//=b
		enc_id_n+=base62[r]
	return enc_id_n
	
def toBase10(enc_id_n, b=62): #base62 to decimal
	base62=ascii_uppercase+ascii_lowercase+string.digits
	dec_id_n=0
	for c in range(len(enc_id_n)):
		dec_id_n = b*dec_id_n+base62.find(enc_id_n[c])
	return dec_id_n