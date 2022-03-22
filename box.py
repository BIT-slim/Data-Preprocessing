import numpy
import pandas
import matplotlib.pyplot as plt

'''
csv_Files = './Oakland Crime Statistics 2011 to 2016 csv Files/'
Box = './Oakland Crime Statistics 2011 to 2016 Box/'
'''

csv_Files = './Wine Reviews csv Files/'
Box = './Wine Reviews Box/'


def Wine_Reviews(file_name):
    global csv_Files
    global Box
    dataFrame = pandas.read_csv(csv_Files + file_name, encoding='UTF-8').replace(' ', numpy.NaN)
    nan_points = 0
    list_points = []
    nan_price = 0
    list_price = []
    for i in range(len(dataFrame)):
        item = dataFrame.iloc[i]['points']
        if numpy.isnan(item):
            nan_points = nan_points + 1
        else:
            list_points.append(int(item))

        item = dataFrame.iloc[i]['price']
        if numpy.isnan(item):
            nan_price = nan_price + 1
        else:
            list_price.append(float(item))

    percentile = numpy.percentile(list_points, (25, 50, 75))
    Q1 = percentile[0]
    Q2 = percentile[1]
    Q3 = percentile[2]
    IQR = Q3 - Q1
    top = Q3 + 1.5*IQR
    bottom = Q1 - 1.5*IQR
    if bottom < 0:
        bottom = 0
    sets = [Q1, Q2, Q3, top, bottom, nan_points]
    with open(Box + 'points.txt', 'w') as tf:
        tf.write(str(sets))
        tf.write('\r\n')
    plt.boxplot(list_points, showmeans=True, flierprops={'markerfacecolor': 'red'})
    plt.savefig(Box + 'points.png')

    percentile = numpy.percentile(list_points, (25, 50, 75))
    Q1 = percentile[0]
    Q2 = percentile[1]
    Q3 = percentile[2]
    IQR = Q3 - Q1
    top = Q3 + 1.5 * IQR
    bottom = Q1 - 1.5 * IQR
    if bottom < 0:
        bottom = 0
    sets = [Q1, Q2, Q3, top, bottom, nan_points]
    with open(Box + 'price.txt', 'w') as tf:
        tf.write(str(sets))
        tf.write('\r\n')
    plt.boxplot(list_price, showmeans=True, flierprops={'markerfacecolor': 'red'}, autorange=True)
    plt.savefig(Box + 'price.png')


def Oakland_Crime_Statistics_2011_to_2016(file_name):
    global csv_Files
    global Box
    dataFrame = pandas.read_csv(csv_Files + file_name, encoding='UTF-8').replace(' ', numpy.NaN)
    nan_Area_ID = 0
    list_Area_ID = []
    nan_Priority = 0
    list_Priority = []
    for i in range(len(dataFrame)):
        item = dataFrame.iloc[i]['Area Id']
        if numpy.isnan(item):
            nan_Area_ID = nan_Area_ID + 1
        else:
            list_Area_ID.append(int(item))

        item = dataFrame.iloc[i]['Priority']
        if numpy.isnan(item):
            nan_Priority = nan_Priority + 1
        else:
            list_Priority.append(float(item))

    percentile = numpy.percentile(list_Area_ID, (25, 50, 75))
    Q1 = percentile[0]
    Q2 = percentile[1]
    Q3 = percentile[2]
    IQR = Q3 - Q1
    top = Q3 + 1.5*IQR
    bottom = Q1 - 1.5*IQR
    if bottom < 0:
        bottom = 0
    sets = [Q1, Q2, Q3, top, bottom, nan_Area_ID]
    with open(Box + 'Area Id.txt', 'w') as tf:
        tf.write(str(sets))
        tf.write('\r\n')
    plt.boxplot(list_Area_ID, showmeans=True, flierprops={'markerfacecolor': 'red'})
    plt.savefig(Box + 'Area Id.png')

    percentile = numpy.percentile(list_Area_ID, (25, 50, 75))
    Q1 = percentile[0]
    Q2 = percentile[1]
    Q3 = percentile[2]
    IQR = Q3 - Q1
    top = Q3 + 1.5 * IQR
    bottom = Q1 - 1.5 * IQR
    if bottom < 0:
        bottom = 0
    sets = [Q1, Q2, Q3, top, bottom, nan_Area_ID]
    with open(Box + 'Priority.txt', 'w') as tf:
        tf.write(str(sets))
        tf.write('\r\n')
    plt.boxplot(list_Priority, showmeans=True, flierprops={'markerfacecolor': 'red'}, autorange=True)
    plt.savefig(Box + 'Priority.png')


if __name__ == '__main__':
    '''
    files = ['records-for-2011.csv', 'records-for-2012.csv', 'records-for-2013.csv', 'records-for-2014.csv',
             'records-for-2015.csv', 'records-for-2016.csv']
    '''
    files = ['winemag-data-130k-v2.csv']

    for file in files:
        # Oakland_Crime_Statistics_2011_to_2016(file)
        Wine_Reviews(file)
