import requests

def test_proxy():
	url = "https://www.12306.cn"
	free_proxy={
		"http":"175.101.109.208:8080"
	}
	headers = {
		"User_Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)"
	}

	response = requests.get(url,headers=headers,proxies=free_proxy)
	print(response.status_code)
	print(response.content)

def cookies():
	url = "https://www.yaozh.com/member/"
	cookie = "acw_tc=2f624a5b15814730164346297e778b2093e8495f45ca2f06ba8f4d0540184d; _ga=GA1.1.907251641.1581473181; PHPSESSID=saija0l590i00u130n3r09lav0; _gid=GA1.2.1016647929.1581583881; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1581583884; yaozh_logintime=1581583822; yaozh_user=878009%09Hyjj92; yaozh_userId=878009; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaZbp1llZ2HnKZxanJT1qeSoMZYoNdzbZtaetzPzJqWhpyqn26fhtHCpquUrJrOnlNu1HCWlHNZkm1qlJm3Ca057eF935Bda30ed1c03dCE0334260ZmJeak1mgqJ%2BYn4OnoKKdU5ysa2SUcIeVbm%2BSbWqWnZSUmpeUWaCyaccfadb6dea64f248af054afaabd651c; db_w_auth=749207%09Hyjj92; UtzD_f52b_saltkey=egzisqt6; UtzD_f52b_lastvisit=1581580223; UtzD_f52b_lastact=1581583823%09uc.php%09; UtzD_f52b_auth=4595L%2BLCPd%2BATHafspGXxAR4Id%2BNxfSbGfTiPWNrLdIrhPgzq7hGKMhL96lHWVcrWg3nkC4EIgYp%2FiletUHjBWK2ONA; yaozh_uidhas=1; yaozh_mylogin=1581583825; acw_tc=2f624a5b15814730164346297e778b2093e8495f45ca2f06ba8f4d0540184d; _ga=GA1.1.907251641.1581473181; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1581473080%2C1581583881"
	
	#需要的时 字典类型   可以不将抓包抓到的cookie按字段拆分
	cookies_dict = {
		'cookie':'acw_tc=2f624a5b15814730164346297e778b2093e8495f45ca2f06ba8f4d0540184d; _ga=GA1.1.907251641.1581473181; PHPSESSID=saija0l590i00u130n3r09lav0; _gid=GA1.2.1016647929.1581583881; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1581583884; yaozh_logintime=1581583822; yaozh_user=878009%09Hyjj92; yaozh_userId=878009; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaZbp1llZ2HnKZxanJT1qeSoMZYoNdzbZtaetzPzJqWhpyqn26fhtHCpquUrJrOnlNu1HCWlHNZkm1qlJm3Ca057eF935Bda30ed1c03dCE0334260ZmJeak1mgqJ%2BYn4OnoKKdU5ysa2SUcIeVbm%2BSbWqWnZSUmpeUWaCyaccfadb6dea64f248af054afaabd651c; db_w_auth=749207%09Hyjj92; UtzD_f52b_saltkey=egzisqt6; UtzD_f52b_lastvisit=1581580223; UtzD_f52b_lastact=1581583823%09uc.php%09; UtzD_f52b_auth=4595L%2BLCPd%2BATHafspGXxAR4Id%2BNxfSbGfTiPWNrLdIrhPgzq7hGKMhL96lHWVcrWg3nkC4EIgYp%2FiletUHjBWK2ONA; yaozh_uidhas=1; yaozh_mylogin=1581583825; acw_tc=2f624a5b15814730164346297e778b2093e8495f45ca2f06ba8f4d0540184d; _ga=GA1.1.907251641.1581473181; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1581473080%2C1581583881'
}
	response = requests.get(url,cookies=cookies_dict)
	data = response.content.decode('utf-8')
	with open("rspcookies.html",'w',encoding='utf-8')as f:
		f.write(data)


# session 类 可以自动保存cookies == cookieJar
def cookies02():
	# 代码登录  
	session = requests.session()

	login_url = "https://www.yaozh.com/login/"
	login_form_data = {
		"username":"Hyjj92",
		"pwd":"Wo15951000937",
		"formhash":"3B3AB8F5CA",
		"backurl":"https%3A%2F%2Fwww.yaozh.com%2F"
		}
	headers = {
		"User_Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)"
	}
	login_response = session.post(login_url,data=login_form_data,headers=headers)
#	登陆后带着cookie 访问个人中心
	url = "https://www.yaozh.com/member/"
	data = session.get(url,headers= headers).content.decode('utf-8')
	with open("rescookies2.html",'w',encoding='utf-8')as f:
		f.write(data)

def main():
	#test_proxy()
	#cookies()
	cookies02()
if __name__ == '__main__':
    main()

