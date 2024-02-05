from app import db, ma

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.Text(), nullable = False, unique = True)
	name = db.Column(db.Text(), nullable = False)
	password = db.Column(db.Text(), nullable = False)

	def __init__(self, email, name, password):
		self.email = email
		self.name = name
		self.password = password

class UserSchema(ma.Schema):
	class Meta:
		fields = ('email', 'name', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many = True)
