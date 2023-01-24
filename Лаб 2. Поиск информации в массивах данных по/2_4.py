from urllib.parse import urlparse
def url_validation(url):
    try:
        res = urlparse(url)
        return all([res.scheme, res.netloc])
    except:
        return False


url = input('Сайт:\n')
print(url_validation(url))
