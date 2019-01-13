import pandas as pd
from sqlalchemy import create_engine
from config import basedir
import os


def get_engine():
    print(basedir)
    conn = 'sqlite:///' + os.path.join(basedir, 'data', 'anjuke.sqlite')
    return create_engine(conn, echo=False)


def read_sql(sql, log=False):
    if log:
        print("sql > {sql}".format(sql=sql))
    return pd.read_sql(sql, get_engine())
