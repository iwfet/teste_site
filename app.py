import os
from flask import *
from flask_cors import CORS

app = Flask(__name__)

Cors =  CORS(app, resource= {r"/*":{"origins":"*"}})

@app.route("/" , methods= ['GET'])
def home():
    return "<h1>ola mundo</h1>"

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    

if __name__ == '__main__':
    main()
    
