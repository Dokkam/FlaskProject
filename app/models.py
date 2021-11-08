from app import db

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cityName = db.Column(db.String(64))
    cityRank = db.Column(db.Integer)
    isVisited = db.Column(db.Boolean, default = False)
    
    def check_city(self, city_name):
        return (self.city_name, city_name)

    def __repr__(self):
        return '<City {}>' .format(self.city_name)

