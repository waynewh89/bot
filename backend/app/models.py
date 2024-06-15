from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

class TradeHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contract_address = db.Column(db.String(120))
    trade_type = db.Column(db.String(10))  # buy or sell
    amount = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)
