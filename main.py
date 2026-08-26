import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

res = requests.get(url)


if __name__ == "__main__":
  print("status code", res.status_code)
