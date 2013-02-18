# Demo of cookie problem

Create a `cookies.txt` file with some cookies in it, using [Ruby
Mechanize](https://github.com/sparklemotion/mechanize):

    $ ruby cookiewrite.rb

Try to read it with python:

    $ python cookieread.py
    Traceback (most recent call last):
      File "cookieread.py", line 9, in <module>
        jar.load()
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/cookielib.py", line 1763, in load
        self._really_load(f, filename, ignore_discard, ignore_expires)
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_MozillaCookieJar.py", line 55, in _really_load
        filename)
    cookielib.LoadError: 'cookies.txt' does not look like a Netscape format cookies file

Apparently Python requires that the cookie file start with a line that looks
exactly like this, which Mechanize is not writing out:

    # Netscape HTTP Cookie File

(See [this](http://stackoverflow.com/a/11536599/179675) StackOverflow answer.)
