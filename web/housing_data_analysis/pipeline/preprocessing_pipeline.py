from housing_data_analysis.db.query import get_all_data


class PreProcessingPipeline():

    def run(self):
        all_data = get_all_data()
        for i in range(len(all_data)):
            s = all_data.ix[i]
            print(s)
            break
        pass


if __name__ == '__main__':
    p = PreProcessingPipeline()
    p.run()
