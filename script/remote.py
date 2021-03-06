#!/usr/bin/env python

import getpass
import os
import sys

## Application specific
SDK_DIR = '/usr/local/google_appengine'
APP_DIR = os.path.expanduser('~/src/bloggart')
APP_ID = 'bloggart-demo'
EMAIL = 'my.email@host.dom'

REMOTE_API_PATH = '/remote_api'

## Extra paths to be inserted into sys.path,
## including the SDK, it's libraries, your APPDIR, and APPDIR/lib

_SDK_LIB_DIR = os.path.join(SDK_DIR, 'lib')
_SDK_LIB_SUBDIRS = [ os.path.join(_SDK_LIB_DIR, name) for name in os.listdir(_SDK_LIB_DIR) if os.path.isdir(os.path.join(_SDK_LIB_DIR, name))]

EXTRA_PATHS = [
	SDK_DIR,
] + _SDK_LIB_SUBDIRS + [
	os.path.join(SDK_DIR, 'lib', 'yaml', 'lib'),
	APP_DIR,
	os.path.join(APP_DIR, 'lib'),
]
sys.path = EXTRA_PATHS + sys.path

from google.appengine.ext.remote_api import remote_api_stub

def attach(host=None):
	def auth_func():
		if host and host.startswith('localhost'):
			return ('foo', 'bar')
		else:
			return (EMAIL, getpass.getpass())
	app_id = APP_ID
	if host and host.startswith('localhost'):
		app_id = 'dev~'+APP_ID
	remote_api_stub.ConfigureRemoteApi(app_id=app_id, path=REMOTE_API_PATH, auth_func=auth_func, servername=host)
	remote_api_stub.MaybeInvokeAuthentication()
	os.environ['SERVER_SOFTWARE'] = 'Development (remote_api)/1.0'


if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1] == '-l':
		host = 'localhost:8080'
	else: 
		host = None

	attach(host)

	from google.appengine.ext import db
	from google.appengine.api import memcache

	BANNER = "App Engine remote_api shell\n" + \
	"Python %s\n" % sys.version + \
	"The db, and memcache modules are imported."

	## Use readline for completion/history if available
	try:
		import readline
	except ImportError:
		pass
	else:
		HISTORY_PATH = os.path.expanduser('~/.remote_api_shell_history')
		readline.parse_and_bind('tab: complete')
		if os.path.exists(HISTORY_PATH):
			readline.read_history_file(HISTORY_PATH)
		import atexit
		atexit.register(lambda: readline.write_history_file(HISTORY_PATH))

	sys.ps1 = '%s <-- ' % (host or APP_ID)

	import code
	code.interact(banner=BANNER, local=globals())
