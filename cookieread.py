# import http.cookie

try:
    import http.cookiejar as c
except ImportError: # Python 2
    import cookielib as c

jar = c.MozillaCookieJar("cookies.txt")
jar.load()
