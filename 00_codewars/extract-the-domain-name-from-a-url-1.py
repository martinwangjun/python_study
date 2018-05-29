# https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train

# def domain_name(url):
#   url_parts = url.split('//')
#   if len(url_parts) < 2:
#     url = url_parts[0]
#   else:
#     url = url_parts[1]
#   url = url.split('/')[0]
#   url = url.split('.')
#   return url[-2]

# Specialist's solution, GAP!!!
def domain_name(url):
  return url.split("//")[-1].split("www.")[-1].split(".")[0]

print(domain_name('https://www.baidu.com/putian/'))
