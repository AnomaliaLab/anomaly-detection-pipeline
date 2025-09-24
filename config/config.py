# model Parameters
n_estimators = 100  # Number of trees
contamination = 0.005  # Expected proportion of anomalies
sample_size = 256  # Number of samples used to train each tree
# Path to save the model
model_path = '../artifacts/models'
# path to load raw data
data_file_path = '../data/raw/air_quality.csv'