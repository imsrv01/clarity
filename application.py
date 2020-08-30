#!flask/bin/python
import json, random, string
from flask import Flask, Response, render_template, request, redirect, send_from_directory
import boto3
from botocore.exceptions import ClientError
import os
import random
from datetime import datetime, timezone
#from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def url():
    return render_template("application.html")

@application.route('/application', methods=['POST','GET'])
def applications():
    if request.method == 'POST':
        service = request.form.get('service')
        print("service - ", service)
        project = request.form.get('project')
        print("project - ", project)
        orderid = processvmrequest(service, project)
        return render_template("application.html", orderid=orderid)
    else:
        return render_template("application.html")

def processvmrequest(service, project):
   
    print("hello")
    return "123"

if __name__ == '__main__':
    application.run(
        debug="true",
        host="0.0.0.0",
        port=5000
    )