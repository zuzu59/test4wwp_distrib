import web
from web import form

render = web.template.render('Templates/')

urls = (
	'/', 'index',
	'/compare', 'compare',
	'/sendok/', 'sendok',
	'/sendko/', 'sendko'
)

db = web.database(dbn='sqlite', db='python.db')

button = form.Form(
    form.Button("submit", type="submit", description="Next"),
)

class index:
    def GET(self):
    	return render.index()
    	
class compare:
	def GET(self):
		i = web.input(url=[])
		if len(i.url)!=0:
			return render.compare(i.url[0], i.url[1])
		else:
			url = db.query('SELECT JAHYA, WORDPRESS FROM sites WHERE STATUS IS NULL LIMIT 1').list()
			if not url:
				return "No more sites to compare"
			else:
				temp = url[0]
				raise web.seeother('/compare?url=' + temp.JAHYA + '&url=' + temp.WORDPRESS)
	def POST(self):
		raise web.seeother('/compare')
		

class sendok:
	def POST(self):
		i = web.input(url=None)
		db.update('sites', where='JAHYA="' + i.url + '"', STATUS='OK')
		raise web.seeother('/compare')
		
class sendko:
	def POST(self):
		i = web.input(url=None)
		db.update('sites', where='JAHYA="' + i.url + '"', STATUS='KO')
		raise web.seeother('/compare')

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()     