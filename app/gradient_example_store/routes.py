import os
import sys
import random
import subprocess
from datetime import datetime
from flask import Blueprint, render_template
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('checkout.html')


@bp.route('/complete_checkout')
def complete_checkout():
    return 'done'

