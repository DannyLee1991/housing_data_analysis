from flask_restful import Resource, reqparse
from housing_data_analysis.db.query import get_all_locate_b
from .. import resp

parser = reqparse.RequestParser()
parser.add_argument("locate_a", type=str, help='locate_a')

class BProvider(Resource):
    def get(self):
        args = parser.parse_args()
        locate_a = args['locate_a']
        locate_b_list = get_all_locate_b(locate_a)
        return resp(data=locate_b_list)
