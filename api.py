from flask import Flask, request
from main import Sandwich

app = Flask(__name__)

# https://e8f7-72-18-104-175.ngrok.io/sandwich?breadPieces=$arg[1]&breadType=$arg[2]&pbType=$arg[3]&presJelJam=$arg[4]&jType=$arg[5]&cutOrNo=$arg[6]&crustOrNo=$arg[7]&cutDirection=$arg[8]
# breadPieces, pbType, jType, breadType, cutOrNo, crustOrNo, presJelJam, cutDirection
# https:// Protocol
# subdomain www, dev, api
# domain google, purplephastrivia
# TLD .com, .org
#:xxxx port number
@app.route("/sandwich")
def hello_world():
    breadPieces = request.args.get("breadPieces")
    breadType = request.args.get("breadType")
    pbType = request.args.get("pbType")
    presJelJam = request.args.get("presJelJam")
    jType = request.args.get("jType")
    crustOrNo = request.args.get("crustOrNo")
    cutOrNo = request.args.get("cutOrNo")
    cutDirection = request.args.get("cutDirection")
    try:
        sandwich = Sandwich(
            breadPieces=breadPieces,
            breadType=breadType,
            pbType=pbType,
            presJelJam=presJelJam,
            jType=jType,
            crustOrNo=crustOrNo,
            cutOrNo=cutOrNo,
            cutDirection=cutDirection
        )
        return sandwich.serve_sandwich()
    except:
        return "Command usage: !servepbj <pieces of bread> <bread type> <pb type> <jelly, jam, preserves> <fruit choice> <crust or no> <cut or no> <cut direction>"
    #return "Still testing"


if __name__ == "__main__":
    app.run(debug=True)
