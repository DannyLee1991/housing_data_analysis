from housing_data_analysis.db.query import get_all_data
import seaborn as sns
from . import make_view_response
from ... import main

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn.apionly as snsa


@main.route('/views/view_trans_d', methods=['GET'])
def test_plot_view():
    import importlib
    importlib.reload(mpl)
    importlib.reload(plt)
    importlib.reload(snsa)

    r = get_all_data()
    plot = sns.distplot(r['UNIT_PRICE'])
    fig = plot.get_figure()

    return make_view_response(fig)
