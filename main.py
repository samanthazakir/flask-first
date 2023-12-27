from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class FirstApp(Resource):
    def get(self):
        return "first app"

api.add_resource(FirstApp, '/')

if __name__ == '__main__':
    app.run(debug=True)
    