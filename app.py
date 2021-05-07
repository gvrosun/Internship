import os.path

from flask import Flask, render_template, redirect, url_for
from forms import StoredForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
base_dir = os.path.dirname(__file__)

app.config['SECRET_KEY'] = 'my_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


# Models
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    message = db.Column(db.Text)

    def __init__(self, name, message):
        self.name = name
        self.message = message


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/reset')
def reset():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/blog', methods=['GET', 'POST'])
def blog():
    form = StoredForm()
    data = Comments.query.all()
    if form.validate_on_submit():
        name = form.name.data
        message = form.message.data
        new_data = Comments(name, message)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('blog'))

    return render_template('blog.html', form=form, data=data)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
