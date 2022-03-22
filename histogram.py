import pandas
from pyecharts.charts import Bar

'''
csv_Files = './Oakland Crime Statistics 2011 to 2016 KNN Null/'
Histogram = './Oakland Crime Statistics 2011 to 2016 KNN Null/'
'''
csv_Files = './Wine Reviews KNN Null/'
Histogram = './Wine Reviews KNN Null/'


def get_data_csv(file_name):
    global csv_Files
    dataFrame = pandas.read_csv(csv_Files + file_name, encoding='UTF-8')
    head = list(dataFrame.columns)
    frequent_list = {}
    h = 0
    for j in range(len(head)):
        f_dictionary = {}
        for i in range(len(dataFrame)):
            item = dataFrame.iloc[i][head[h]]
            if item not in f_dictionary:
                f_dictionary[item] = 1
            else:
                f_dictionary[item] = f_dictionary[item] + 1
        frequent_list[head[h]] = f_dictionary
        h = h + 1
    return frequent_list


def record(topic, frequent_list):
    global csv_Files
    heads = list(frequent_list.keys())
    h = 0
    with open(csv_Files + topic.split('.')[0] + '.txt', 'w') as tf:
        for f_dictionary in frequent_list.values():
            tf.write(heads[h])
            tf.write('\r\n')
            tf.write(str(f_dictionary))
            tf.write('\r\n')
            h = h + 1


def histogram_plot(topic, frequent_list):
    global Histogram
    heads = list(frequent_list.keys())
    h = 0
    for f_dictionary in frequent_list.values():
        x = list(f_dictionary.keys())
        y = []
        for item in x:
            y.append(f_dictionary[item])
        bar = (Bar().add_xaxis(x).add_yaxis(topic + heads[h], y))
        bar.render(Histogram + topic + '@' + heads[h] + 'bar.html')
        h = h + 1


if __name__ == '__main__':
    '''
        files = ['records-for-2011.csv', 'records-for-2012.csv', 'records-for-2013.csv', 'records-for-2014.csv',
                 'records-for-2015.csv', 'records-for-2016.csv']
    '''
    # files = ['winemag-data-130k-v2.csv']
    files = ['test.csv']

    for file in files:
        frequent = get_data_csv(file)
        # record(file, frequent)
        histogram_plot(file, frequent)
