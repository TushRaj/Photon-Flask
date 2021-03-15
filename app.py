from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///photon.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        photon = Photon(title=title, desc=desc)
        db.session.add(photon)
        db.session.commit()
        
    allFiles = Photon.query.all() 
    return render_template('index.html', allFiles=allFiles) 


@app.route('/delete')
def delete(num):
    photon = Photon.query.filter_by(num=num).first()
    db.session.delete(photon)
    db.session.commit()
    return redirect("/")


@app.route('/show')
def files():
    allFiles = Photon.query.all()
    print(allFiles)
    


if __name__ == "__main__":
    app.run(debug=True)