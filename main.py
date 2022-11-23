from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def loadData():
    with open("static/data/index.json", "r") as outfile:
        teamDetails = json.load(outfile)

    nameToPic = {}
    for item in teamDetails:
        item["totalComments"] = len(item["comments"])
        nameToPic[ item["name"] ] = item["picture"]

    return render_template("index.html", token='', teamDetails=teamDetails, nameToPic=nameToPic)

@app.route('/addComment', methods=['GET'])
def updateData():

    empName = request.args.get('empName')
    commentVal = request.args.get('comment')
    userName = request.args.get('name')

    with open("static/data/index.json", "r") as readFile:
        teamDetails = json.load(readFile)
        for item in teamDetails:
            if item["name"] == empName:
                newData = { "name": userName, "value": commentVal }
                item["comments"].append( newData )
                break

    with open('static/data/index.json', 'w') as outfile:
        json.dump(teamDetails, outfile)

    return redirect("/")

if __name__ == '__main__':
    app.run()