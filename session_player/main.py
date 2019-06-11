from flask import Flask,jsonify, request,abort,render_template
from flask_sqlalchemy import SQLAlchemy
import json
import os
from datetime import timedelta,datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)

class Player(db.Model):
    event = db.Column(db.String(5))
    country = db.Column(db.String(2))
    player_id = db.Column(db.String(50),primary_key=True)
    session_id = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime)
    session_completed = db.Column(db.BOOLEAN,default=False)

    def __init__(self, event, country, player_id, session_id, timestamp):
        self.event = event
        self.country = country
        self.player_id = player_id
        self.session_id = session_id
        self.timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')


@app.route('/api/players/<player_id>', methods = ['GET', 'POST'])
def get_completed_sessions(player_id):
   
    sessions = Player.query.filter(Player.player_id == player_id and Player.session_completed != True)
    return render_template('render_template_file.html', players=sessions)
    

	
@app.route('/api/hours/<hour>', methods = ['GET', 'POST'])
def get_sessions_start_percountry(hour):
   since = datetime.now() - timedelta(hours=5)
   sessions = Player.query(Player.country,Player.session_id).filter(Player.timestamp > since).group_by(Player.country).all()
   return render_template('render_template_file.html', players=sessions)


@app.route('/api/event_batch',methods = ['GET'])
def create_session():
    """
    API for reciving event batches
    :return:
    """
    if not request.json or not 'event' in request.json \
            or not 'country'  in request.json \
            or not 'player_id' in request.json:
        abort(400)
    print(request.json)
    player = Player(request.json['event'],request.json['country'],
                    request.json['player_id'],request.json['session_id'],request.json['ts'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'Player':player})

if __name__== '__main__':
    app.run(debug=True)