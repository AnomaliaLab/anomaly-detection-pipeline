import csv
import pandas as pd
import numpy as np


def load_data_from_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def load_data_as_pandas_df(file_path):
    data = pd.read_csv(file_path)
    return data

# load streaming data from kafka
def load_data_from_kafka():
    pass

def load_data_from_database():
    pass

def load_data_from_api():
    pass

def load_data_from_s3():
    pass

def load_data_from_hdfs():
    pass

def load_data_from_ftp():
    pass

def load_data_from_http():
    pass


def generate_training_dataset():
    timestamps = np.arange(0, 24 * 3600 * 14, 60)
    num_points = len(timestamps)

    sensor1_values = np.random.rand(num_points)
    dataset1 = np.array([timestamps, sensor1_values])
    dataframe1 = pd.DataFrame(dataset1.T, columns=['timestamp', 'sensor1'])
    dataframe1.set_index('timestamp', inplace=True)

    sensor2_values = np.sin(timestamps)
    dataset2 = np.array([timestamps, sensor2_values])
    dataframe2 = pd.DataFrame(dataset2.T, columns=['timestamp', 'sensor2'])
    dataframe2.set_index('timestamp', inplace=True)

    dataframes_dict = {'dataframe1': dataframe1, 'dataframe2': dataframe2}
    
    return dataframes_dict


def generate_scoring_dataset(np):
    timestamps = np.arange(0, 24 * 3600, 60)
    num_points = len(timestamps)

    sensor1_values = np.random.rand(num_points)
    sensor1_values[0:100] = 2 * np.random.rand(100)  # Introducing some variations for the first 100 points
    dataset1 = np.array([timestamps, sensor1_values])
    dataframe1 = pd.DataFrame(dataset1.T, columns=['timestamp', 'sensor1'])
    dataframe1.set_index('timestamp', inplace=True)

    sensor2_values = np.sin(timestamps)
    dataset2 = np.array([timestamps, sensor2_values])
    dataframe2 = pd.DataFrame(dataset2.T, columns=['timestamp', 'sensor2'])
    dataframe2.set_index('timestamp', inplace=True)

    dataframes_dict = {'dataframe1': dataframe1, 'dataframe2': dataframe2}

    return dataframes_dict

if __name__ == '__main__':
    file_path = 'data/air_quality.csv'
    # data = load_data_from_csv(file_path)
    # print(data)

    data = load_data_as_pandas_df(file_path)
    print(data.head())



