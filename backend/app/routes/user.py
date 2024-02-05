from app import app, bcrypt, db
from flask import jsonify, request, session
from app.models.user import User

# @app.before_request
# def check_user():
# 	print(request.endpoint)
# 	print(request.url)
# 	print(request.path)
# 	print(request.json)

@app.route('/sign-in', methods = ['POST'])
@app.route('/sign-in/', methods = ['POST'])
def sign_in():
	try:
		if len(request.json) < 1:
			return jsonify({ 'message': 'Invalid request.' }), 400

		email = request.json['email']
		password = request.json['password']

		if not email or not password:
			return jsonify({ 'message': 'Invalid request' }), 400

		user = User.query.filter_by(email = email).first()

		if not user:
			return jsonify({ 'message': 'Account not found.' }), 404

		if not bcrypt.check_password_hash(user.password, password):
			return jsonify({ 'message': 'Invalid passwowrd' }), 401

		session['user_id'] = user.id

		return jsonify({ 'message': 'Successfully signed in' }), 200
	except Exception as e:
		err = str(e)

		if 'email' in err or 'password' in err:
			return jsonify({ 'message': 'Invalid request.' }), 400

		return jsonify({ 'message': 'Internal server error' }), 500

@app.route('/sign-up', methods = ['POST'])
@app.route('/sign-up/', methods = ['POST'])
def sign_up():
	try:
		if len(request.json) < 1:
			return jsonify({ 'message': 'Invalid request.' }), 400

		name = request.json['name']
		email = request.json['email']
		password = request.json['password']

		if not name or not email or not password:
			return jsonify({ 'message': 'Invalid request' }), 400

		user = User.query.filter_by(email = email).first()

		if user is not None:
			return jsonify({ 'message': 'Email is already existing' }), 409

		hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

		new_user = User(email, name, hashed_password)

		db.session.add(new_user)
		db.session.commit()

		session['user_id'] = new_user.id

		return jsonify({ 'message': 'Successfully signed up' }), 201
	except Exception as e:
		err = str(e)

		if 'name' in err or 'email' in err or 'password' in err:
			return jsonify({ 'message': 'Invalid request.' }), 400

		return jsonify({ 'message': 'Internal server error' }), 500
