'''
usage: 
http://server IP:port/message_url/?Number=1415xxxxxx

'''

import plivoxml
import os
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/message_url/', methods=['GET', 'POST'])
def message():
    r = plivoxml.Response()
    if request.method == 'GET':
        message_content = request.args.items()
        From = request.args['From']
        To = request.args['To']
        Text = request.args['Text']
        Number = request.args['Number']
    elif request.method == 'POST': 
        message_content = request.form.items()
        From = request.form['From']
        To = request.form['To']
        Text = request.form['Text']
        Number = request.form['Number']

    body = str(From) + ': ' + Text
    params = {
        'src' : str(To),
        'dst' : str(Number),
        'type' : "sms",
        }
    r.addMessage(body, **params)
    response = make_response(r.to_xml())
    response.headers["Content-type"] = "text/xml"
#    print r.to_xml
    return response

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host = "0.0.0.0", port = port, debug = True)
