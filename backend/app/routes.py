from flask import request
from flask_restful import Resource

def initialize_routes(api):
    api.add_resource(Contract, '/contract/<string:address>')

class Contract(Resource):
    def get(self, address):
        # Implement fetching and returning contract data
        return {"market_cap": 123456, "total_holders": 789}
