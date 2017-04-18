from flask import Flask,url_for,request,render_template;
from app import app;
from alchemy import BackData;
#database


#server/
@app.route('/')
def hello():
    """Renders a sample page."""
    createLink="<a href='" + url_for('addAid') +"'>Find A ID</a>";
    return """<html>
                    <head> 
                        <title>Hello,world</title>
                    </head>
                    <body>
                        """+ createLink +"""
                    </body>
                </html>""";


#sever/findAid
@app.route('/addAid', methods=['GET', 'POST'])
def addAid():
    if request.method == 'GET':
        #send user the form
        return render_template('addAid.html');
    elif request.method == 'POST':
        #read data and save it
        id = request.form['id'];
        user=BackData.query.filter_by(id=id).first();
        return render_template('idAdded.html',id = id,situation=user.situation);
    else:
        return "<h2>ERROR</h2>"
