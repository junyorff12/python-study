import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

res = requests.get(url)
print("status code", res.status_code)

account_balance = '12'

# res = account_balance / 2

print(isinstance(account_balance, int))
