import os
import sys
import random
import subprocess
import requests
from datetime import datetime

from flask import Blueprint, render_template, request, jsonify
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')
    

@bp.route('/checkout')
def checkout():
    url = request.args.get('url')
    vendor_id = request.args.get('vendor_id')
    request_url = url + "/checkout/vendor_name?vendor_id=" + vendor_id
    vendor_name = requests.get(request_url).content.decode('utf-8')
    return render_template('checkout.html', 
        url = url, 
        vendor_id = vendor_id, 
        vendor_name = vendor_name)


@bp.route('/complete_checkout')
def complete_checkout():
    return 'done'

