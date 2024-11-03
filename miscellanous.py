import requests

resp = requests.get('http://rahulshettyacademy.com', cookies={'visit-month':'May'}, timeout=1)

print(resp.history) #301
print(resp.status_code) # 200

resp2 = requests.get('http://rahulshettyacademy.com', cookies={'visit-month':'June'}, allow_redirects=False, timeout=1)

print(resp2.history) #301
print('redirection :', resp2.status_code) # 200



response = requests.get(
    url='https://httpbin.org/cookies',
    cookies={'token': 'value123'}
)
print(response.status_code)
print(response.text)

se = requests.session()
se.cookies.update({'token': 'value123'})
response1 = se.get(
    url='https://httpbin.org/cookies',
    cookies={'token2': 'value123456'}
)
print(response1.history)
print(response1.text)
response2 = se.get(
    url='https://httpbin.org/cookies'
)
print(response2.history)
print(response2.text)
