import web
from datetime import datetime

def getFile(file):
	with open(file, 'r') as f:
		return f.read()

urls = (
	'/', 'index',
	'/results', 'results',
	'/clear', 'clear',
	'/about', 'about'
)

app = web.application(urls, globals())

class index:
	def GET(self):
		return getFile('index.html')
	
	def POST(self):
		datum = web.input()
		with open('results.txt', 'a') as f:
			print >>f, str(datetime.now()) + ' UTC: ' + str(web.ctx['ip']) + ': ' + str(datum.ip)
		return getFile('thanks.html')

class results:
	def GET(self):
		return getFile('results.txt')

class clear:
	def GET(self):
		with open('results.txt', 'w') as f:
			print >>f, 'Results (from ' + str(datetime.now()) + ' UTC)'
		return 'Results cleared.'

class about:
	def GET(self):
		return getFile('about.html')

if __name__ == '__main__':
	app.run()