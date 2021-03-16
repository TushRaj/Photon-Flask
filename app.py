from flask import Flask, render_template,request,Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///photon.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Photon(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    

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


@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    return Response(status=200)
    


if __name__ == "__main__":
    app.run(debug=True)