from .. import db

# Secondary table to define many-to-many relationship between users and subscribers 
subscriptions_table = db.Table("subscriptions", db.Column("subscriber_id", db.ForeignKey("subscribers.id")), db.Column("user_id", db.ForeignKey("users.id")))

class Subscriber(db.Model):
    """
    Class for defining blogposts instances and methods. Inherits from db.Model.
    """ 
    __tablename__="subscribers"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    subscriptions = db.relationship("User", secondary=subscriptions_table, back_populates = "subscribers")