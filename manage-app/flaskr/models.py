from flaskr import db

class AutoScalingConfig(db.Model):
    __tablename__ = 'autoscalingconfig'
    ascid = db.Column(db.Integer, primary_key=True)
    cpu_grow = db.Column(db.Integer)
    cpu_shrink = db.Column(db.Integer)
    ratio_expand = db.Column(db.Float)
    ratio_shrink = db.Column(db.Float)
    timestamp = db.Column(db.DateTime) # A type for datetime.datetime() objects.
    def __repr__(self): # how to print User
        return '<AutoScalingConfig {}>'.format(self.timestamp)



