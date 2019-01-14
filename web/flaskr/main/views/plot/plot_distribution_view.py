from housing_data_analysis.db.query import get_all_data
import seaborn as sns
from flask import request
from . import make_view_response, reload_view
from ... import main


@main.route('/views/plot_distribution', methods=['POST'])
def plot_distribution_view():
    reload_view()

    if request.method == 'POST':
        locate_a = request.form['locate_a']
        locate_b = request.form['locate_b']
        start = request.form['start']
        end = request.form['end']
        what = request.form['what']

        r = get_all_data()
        if locate_a:
            r = r[r.LOCATE_A == locate_a]
        if locate_b:
            r = r[r.LOCATE_B == locate_b]

        # 数据过滤
        r = r[r.BUILD_TIME_INFO != ""]
        r = r[r[what] > r[what].quantile(0.01)]
        r = r[r[what] < r[what].quantile(0.99)]

        col = r[what].astype('float64')

        plot = sns.distplot(col)
        fig = plot.get_figure()

        # print("plot {what}".format(what=what))

        return make_view_response(fig)
