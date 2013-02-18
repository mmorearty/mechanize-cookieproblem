require 'mechanize'

agent = Mechanize.new
page = agent.get("http://www.google.com/")
agent.cookie_jar.save_as("cookies.txt", :cookiestxt)
