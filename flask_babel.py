#!/usr/bin/env python3

from flask import Flask, render_template, request
from babel import numbers,dates
from datetime import date
from datetime import datetime, time
from flask_babel import Babel, format_date



app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

def get_local():
    return 'zh'
    #request.accept_languages.best_match(['en', 'es', 'de'])
@app.route('/')
def index():
    
    us_num = numbers.format_decimal(12345, locale='en_US')
    se_num = numbers.format_decimal(12345, locale='sv_SE')
    de_num = numbers.format_decimal(12345, locale="de_DE")
    
    my_date = date(1894, 4, 1)
    
    us_date = dates.format_date(my_date, locale='en_US')
    de_date = dates.format_date(my_date, locale='de_DE')
    
    results = {'us_num' : us_num, 'se_num' : se_num, 'de_num' : de_num, 'us_date': us_date, 'de_date' : de_date}
    return render_template('flask_1.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)