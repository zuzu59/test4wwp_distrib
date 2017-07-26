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
        names = db.query('SELECT NAME FROM users').list()
        return render.index(names)

class compare:
    def GET(self):
        urls = web.input(url=[]).url
        name = web.input(name = '').name
        if len(urls)==2:
            return render.compare(name, urls[0], urls[1])
        else:
            #Verification de la date d'expiration de seances 'en cours'
            db.update('sites', where='STATUS="BUSY" AND DATE<' + str(time.time()-grace_period), STATUS=None, DATE=None)
			
            urls = db.query('SELECT JAHIA, WORDPRESS FROM sites WHERE STATUS IS NULL').list()
            if not urls:
                return "No more sites to compare"
            else:
                rdm_id = randint(0, len(urls))
                temp = urls[rdm_id]
                if (db.query('SELECT STATUS FROM sites WHERE JAHIA="' + temp.JAHIA + '"')!='DONE'):
                    db.update('sites', where='JAHIA="' + temp.JAHIA + '"', STATUS='BUSY', DATE=time.time())
                raise web.seeother('/compare?name=' + name + '&url=' + temp.JAHIA + '&url=' + temp.WORDPRESS)

    def POST(self):
        name = web.input(select=None).select
        if name != "empty":
            raise web.seeother('/compare?name=' + name)
        else:
            raise web.seeother('/')



class next:
    def POST(self):
        update_status('DONE')

class emptyPage:
    def POST(self):
        update_status('EMPTY')
        
class connectionError:
    def POST(self):
        update_status('ERROR')
 

def update_status(status):
    url = web.input(url=None).url
    name = web.input(name = '').name
    if name:
        db.update('sites', where='JAHIA="' + url + '"', STATUS=status, DATE=time.time())    
        raise web.seeother('/compare?name=' + name)
    else:
        raise web.seeother('/')

		
if __name__ == "__main__":  
    app = web.application(urls, globals())  
    app.run()     
