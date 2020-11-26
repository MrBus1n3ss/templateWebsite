from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'  # TODO: Make new key and make it an env variable
csrf = CSRFProtect(app)
Bootstrap(app)

@app.route('/')
@csrf.exempt
def index():
    form = MyForm()
    return render_template('main.html', form=form)

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])