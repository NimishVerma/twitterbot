from django.shortcuts import render
import requests
import base64
import hmac
import hashlib
# Create your views here.

def sethook(request):

	if request == 'GET':
		crc_token = request.GET['crc_token	']

		sha256_hash_digest = hmac.new('zQC1HaCQQ0TCX5SIkCV1YkARxwFDxtIuPvCpjupigj5y4HAb2U', msg=crc_token, digestmod=hashlib.sha256).digest()

		response = {
		  'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest)
		}			

	if request == 'POST':
		print request