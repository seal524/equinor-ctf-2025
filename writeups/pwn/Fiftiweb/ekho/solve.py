import requests
import time
from padding_oracle import encrypt
import base64
from pwn import xor

endpoint = 'https://ekho-9fc3cc1e-fifti.ept.gg/protected'
login_endpoint = 'https://ekho-bf46cfb0-fifti.ept.gg/login.html'

def attempt(payload):
	cookie = f"Era=0&Payload={base64.b64encode(payload).decode()}&AuthHash=%0A"
	res = requests.get(endpoint, cookies={"enterprise_grade_cookie":cookie})
	return "no valid session" not in res.text

def get(payload):
	print(payload)
	cookie = f"Era=0&Payload={base64.b64encode(payload).decode()}&AuthHash=%0A"
	print(cookie)
	res = requests.get(endpoint, cookies={"enterprise_grade_cookie":cookie})
	return res.text

def login():
	now = int(time.time())
	res = requests.post(login_endpoint, data={"username":"user","password":"password"})
	return res, now

ct = encrypt(
	plaintext=b'user=role=admin',
	oracle=attempt,
	num_threads=32,
	block_size=8
)

print(f"payload : {base64.b64encode(ex)}")
print(get(ex)) # should return the flag
