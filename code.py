import web
from web import form
import time
from random import randint

render = web.template.render('Templates/')

urls = (
	'/', 'index',
	'/compare', 'compare',
	'/next', 'next',
	'/sendko', 'sendko'
)

db = web.database(dbn='sqlite', db='python.db')

button = form.Form(
    form.Button("submit", type="submit", description="Next"),
)
#Changer la valeur en secondes pendant laquelle un page va etre consideree comme en traitement
grace_period = 3600

class index:
    def GET(self):
    	return render.index()
    	
class compare:
	def GET(self):
		i = web.input(url=[])
		if len(i.url)==2:
			return render.compare(i.url[0], i.url[1])
		else:
			#Verification de la date d'expiration de seances 'en cours'
			db.update('sites', where='STATUS="BUSY" AND DATE<' + str(time.time()-grace_period), STATUS=None, DATE=None)
			
			urls = db.query('SELECT JAHIA, WORDPRESS FROM sites WHERE STATUS IS NULL').list()
			if not urls:
				return "No more sites to compare"
			else:
				rdm_id = randint(0, len(urls))
				temp = urls[rdm_id]
				
				if (db.query('SELECT STATUS FROM sites WHERE JAHIA="' + temp.JAHIA + '"')!='TESTED'):
					db.update('sites', where='JAHIA="' + temp.JAHIA + '"', STATUS='BUSY', DATE=time.time())
				raise web.seeother('/compare?url=' + temp.JAHIA + '&url=' + temp.WORDPRESS)
	def POST(self):
		raise web.seeother('/compare')
		

class next:
	def POST(self):
		i = web.input(url=None)
		db.update('sites', where='JAHIA="' + i.url + '"', STATUS='TESTED', DATE=time.time())
		raise web.seeother('/compare')
		
class sendko:
	def POST(self):
		i = web.input(url=None)
		db.update('sites', where='JAHIA="' + i.url + '"', STATUS='ERROR', DATE=time.time())
		raise web.seeother('/compare')
		
if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()     
