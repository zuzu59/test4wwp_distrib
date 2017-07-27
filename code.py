import web
from web import form
import time
from random import randint

render = web.template.render('Templates/')

urls = (
	'/', 'index',
	'/sites', 'sites',
	'/compare', 'compare',
	'/next', 'next',
	'/connectionError', 'connectionError',
	'/emptyPage', 'emptyPage'
)


db = web.database(dbn='sqlite', db='python.db')
names = db.query('SELECT ID, NAME FROM users').list()
status = ['DONE', 'BUSY', 'EMPTY', None]

button = form.Form(
    form.Button("submit", type="submit", description="Next"),
)

class index:
    def GET(self):
        return render.index(names)

class sites:
	def GET(self):
		sites = db.query("SELECT * FROM sites;").list()
		return render.sites(sites, names, status)

class compare:
    def GET(self):
        urls = web.input(url=[]).url
        user_id = web.input(user_id = 0).user_id
        if (int(user_id) <= 0) or (int(user_id) > len(names)):
            raise web.seeother('/')
        if len(urls)==2:
            return render.compare(user_id, urls[0], urls[1])
        else:
            urls = db.query('SELECT JAHIA, WORDPRESS FROM sites WHERE STATUS="BUSY" AND USER_ID="' + user_id + '";').list()
     	    if not urls:
		        urls = db.query('SELECT JAHIA, WORDPRESS FROM sites WHERE STATUS IS NULL;').list()
        if not urls:
            return "No more sites to compare"
        rdm_id = randint(0, len(urls)-1)
        temp = urls[rdm_id]
        if (db.query('SELECT STATUS FROM sites WHERE JAHIA="' + temp.JAHIA + '"')!='DONE'):
            db.update('sites', where='JAHIA="' + temp.JAHIA + '"', STATUS='BUSY', USER_ID=user_id, DATE=time.time())
        raise web.seeother('/compare?user_id=' + user_id + '&url=' + temp.JAHIA + '&url=' + temp.WORDPRESS)

    def POST(self):
        user_id = web.input(select=None).select
        if user_id != "empty":
            raise web.seeother('/compare?user_id=' + user_id)
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
    user_id = web.input(user_id=0).user_id
    if user_id != '0':
        db.update('sites', where='JAHIA="' + url + '"', STATUS=status, DATE=time.time())
        raise web.seeother('/compare?user_id=' + user_id)
    else:
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
