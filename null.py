import missingno
import pandas
import numpy
from sklearn.impute import SimpleImputer, KNNImputer

'''
Frequent_Null = './Oakland Crime Statistics 2011 to 2016 Frequent Null/'
csv_Files = './Oakland Crime Statistics 2011 to 2016 csv Files/'
delete_Null = './Oakland Crime Statistics 2011 to 2016 Delete Null/'
KNN_Null = './Oakland Crime Statistics 2011 to 2016 KNN Null/'
Attribute_Null = './Oakland Crime Statistics 2011 to 2016 Attribute Null/'
'''
Frequent_Null = './Wine Reviews Frequent Null/'
csv_Files = './Wine Reviews csv Files/'
delete_Null = './Wine Reviews Delete Null/'
KNN_Null = './Wine Reviews KNN Null/'
Attribute_Null = './Wine Reviews Attribute Null/'


def Oakland_Crime_Statistics_2011_to_2016_attribute_null(file_name):
    global csv_Files
    global Attribute_Null
    data = pandas.read_csv(csv_Files + file_name, encoding='UTF-8').replace(' ', numpy.NaN)
    new_data = data[['Area Id', 'Priority', 'Beat', 'Incident Type Id', 'Incident Type Description']]
    for i in range(len(new_data)):
        if numpy.isnan(new_data.iloc[i]['Area Id']):
            for j in range(len(new_data)):
                if not numpy.isnan(new_data.iloc[j]['Area Id']) and (new_data.iloc[i][1] == data.iloc[j][1]
                                                                     or new_data.iloc[i][2] == data.iloc[j][2]
                                                                     or new_data.iloc[i][3] == data.iloc[j][3]
                                                                     or new_data.iloc[i][4] == data.iloc[j][4]):
                    new_data.iloc[i]['Area Id'] = data.iloc[j]['Area Id']
                    break
        if numpy.isnan(new_data.iloc[i]['Priority']):
            for j in range(len(new_data)):
                if not numpy.isnan(new_data.iloc[j]['Priority']) and (new_data.iloc[i][0] == data.iloc[j][0]
                                                                      or new_data.iloc[i][2] == data.iloc[j][2]
                                                                      or new_data.iloc[i][3] == data.iloc[j][3]
                                                                      or new_data.iloc[i][4] == data.iloc[j][4]):
                    new_data.iloc[i]['Priority'] = data.iloc[j]['Priority']
                    break
    data['Area Id'] = new_data['Area Id']
    data['Priority'] = new_data['Priority']
    data = pandas.DataFrame(data)
    data.to_csv(path_or_buf=Attribute_Null + file_name.split('.')[0] + '.csv', index=False, encoding='UTF-8')


def Wine_Reviews_attribute_null(file_name):
    global csv_Files
    global Attribute_Null
    data = pandas.read_csv(csv_Files + file_name, encoding='UTF-8').replace(' ', numpy.NaN)
    new_data = data[['points', 'price', 'country', 'province', 'taster_name']]
    for i in range(len(new_data)):
        if numpy.isnan(new_data.iloc[i]['points']):
            for j in range(len(new_data)):
                if not numpy.isnan(new_data.iloc[j]['points']) and (new_data.iloc[i][1] == data.iloc[j][1]
                                                                    or new_data.iloc[i][2] == data.iloc[j][2]
                                                                    or new_data.iloc[i][3] == data.iloc[j][3]
                                                                    or new_data.iloc[i][4] == data.iloc[j][4]):
                    new_data.iloc[i]['points'] = data.iloc[j]['points']
                    break
        if numpy.isnan(new_data.iloc[i]['price']):
            for j in range(len(new_data)):
                if not numpy.isnan(new_data.iloc[j]['price']) and (new_data.iloc[i][0] == data.iloc[j][0]
                                                                   or new_data.iloc[i][2] == data.iloc[j][2]
                                                                   or new_data.iloc[i][3] == data.iloc[j][3]
                                                                   or new_data.iloc[i][4] == data.iloc[j][4]):
                    new_data.iloc[i]['price'] = data.iloc[j]['price']
                    break
    data['points'] = new_data['points']
    data['price'] = new_data['price']
    data = pandas.DataFrame(data)
    data.to_csv(path_or_buf=Attribute_Null + file_name.split('.')[0] + '.csv', index=False, encoding='UTF-8')


def KNN_null(file_name):
    global csv_Files
    global KNN_Null
    data = pandas.read_csv(csv_Files + file_name, encoding='UTF-8')
    fill = KNNImputer(missing_values=numpy.NaN, n_neighbors=3)
    new_data = fill.fit_transform(data[['points', 'price']])
    new_data = pandas.DataFrame(new_data)
    data['points'] = new_data[0]
    data['price'] = new_data[1]
    data = pandas.DataFrame(data)
    data.to_csv(path_or_buf=KNN_Null + file_name.split('.')[0] + '.csv', index=False, encoding='UTF-8')


def frequent_null(file_name):
    global csv_Files
    global Frequent_Null
    data = pandas.read_csv(csv_Files + file_name, encoding='UTF-8')
    head = list(data.columns)
    fill = SimpleImputer(missing_values=numpy.NaN, strategy='most_frequent')
    data = fill.fit_transform(data)
    data = pandas.DataFrame(data)
    data.to_csv(path_or_buf=Frequent_Null + file_name.split('.')[0] + '.csv',
                index=False, header=head, encoding='UTF-8')


def delete_null(file_name):
    global csv_Files
    global delete_Null
    data = pandas.read_csv(csv_Files + file_name, encoding='UTF-8')
    plot = missingno.matrix(data, labels=True).figure
    plot.figure.savefig(delete_Null + file.split('.')[0] + '.png')
    data = data.replace(' ', numpy.NaN).dropna(axis=0)
    data.to_csv(path_or_buf=delete_Null + file_name.split('.')[0] + '.csv',
                index=False, header=True, encoding='UTF-8')


if __name__ == '__main__':
    '''
    files = ['records-for-2011.csv', 'records-for-2012.csv', 'records-for-2013.csv', 'records-for-2014.csv',
             'records-for-2015.csv', 'records-for-2016.csv']
    '''
    files = ['winemag-data-130k-v2.csv']
    for file in files:
        delete_null(file)
        frequent_null(file)
        KNN_null(file)
        Wine_Reviews_attribute_null(file)
        # Oakland_Crime_Statistics_2011_to_2016_attribute_null(file)

