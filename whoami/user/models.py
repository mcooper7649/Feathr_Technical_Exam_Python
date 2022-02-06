from flask import Flask, jsonify, request
import uuid


class User:

    @staticmethod
    def signup():
        print(request.form)

        #Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            'username': request.form.get('username'),
            'password': request.form.get('password')
        }
        return jsonify(user), 200
