# https://guarded-stream-62460.herokuapp.com САЙТ
import sentry_sdk, os
from bottle import Bottle, run, request
from sentry_sdk.integrations.bottle import BottleIntegration
SENTRY_DSN = "https://3e774449b21c49c78d2d5ae9ed82aef2@o528104.ingest.sentry.io/5666696"
sentry_sdk.init(
    dsn=os.environ.get(SENTRY_DSN), 
    integrations=[BottleIntegration()]
)
app = Bottle()
@app.route('/')
def index():
	return "Привет."

@app.route('/fail')  
def index1():  
    raise RuntimeError("There is an error!")  

@app.route('/success')
def index2():
	return "200 OK"
if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)
