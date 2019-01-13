from io import BytesIO
import base64
from flask import make_response, render_template
import seaborn.apionly as snsa

# 解决matplotlib字体不显示的问题
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def reload_view():
    import importlib
    importlib.reload(mpl)
    importlib.reload(plt)
    importlib.reload(snsa)


def gen_view_data(fig):
    sio = BytesIO()
    fig.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    return data


def make_view_response(fig):
    '''
    生成可视化图片相应
    :param data:
    :return:
    '''
    data = gen_view_data(fig)
    return make_response(render_template('plot/base.html', data=data))
