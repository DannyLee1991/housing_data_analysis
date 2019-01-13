from flask_restful import Resource
from .. import resp
from housing_data_analysis.db.query import get_all_locate_a


class AProvider(Resource):
    def get(self):
        return resp(data=get_all_locate_a())
