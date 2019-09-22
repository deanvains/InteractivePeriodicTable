from app import db

class periodicTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(64))

    def __repr__(self):
        return '<id {}, name {}, desc {}>'.format(self.id, self.name, self.description)