from flask import Blueprint
from flask_restful import Api

main = Blueprint('main', __name__)

from .views import index, area_ana
from .views.plot.test_plot_view import test_plot_view
from .views.plot import plot_distribution_view

restful = Api(main)

from flaskr.main.api.locate.AProvider import AProvider

restful.add_resource(AProvider, '/api/locate/a')

from flaskr.main.api.locate.BProvider import BProvider

restful.add_resource(BProvider, '/api/locate/b')
