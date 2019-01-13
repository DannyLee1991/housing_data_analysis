from housing_data_analysis.db.query import get_all_data
import seaborn as sns
import matplotlib.pyplot as plt



if __name__ == '__main__':
    r = get_all_data()
    # sns.distplot(r['UNIT_PRICE'])

    corrmat = r.corr()
    f, ax = plt.subplots(figsize=(12, 9))
    sns.heatmap(corrmat, vmax=.8, square=True);
    plt.show()