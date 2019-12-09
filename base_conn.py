# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_utils import database_exists

# db = SQLAlchemy(app)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(120), nullable=False, default="default.gpg")
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship("Post", backref="author", lazy=True)
#
#     def __repr__(self):
#         return f"username'{self.username}', email'{self.email}'"
#
# class Post(db.Model):
#     from datetime import datetime
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
#
#     def __repr__(self):
#         return f"title'{self.title}', date_posted'{self.date_posted}', content'{self.content}'"
#
# if not database_exists("sqlite:///site.db"):
#     db.create_all()

# t = User(username="Corey", email="sdf@mail.ru", password="234dsfsdaf23")
# print(t)
# db.session().add(t)
# db.session().commit()
# print(User.query.all())
