from flask import render_template, make_response, request
from .. import main


@main.route('/area_ana', methods=['GET'])
def area_ana():
    locate_a = request.args.get("locate_a", "全部")
    locate_b = request.args.get("locate_b", "全部")
    print("/area_ana get locate_a:{locate_a} locate_b:{locate_b}".format(locate_a=locate_a, locate_b=locate_b))
    return make_response(render_template('area_ana.html', locate_a=locate_a, locate_b=locate_b))
