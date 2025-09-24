
import sys

sys.path.append("../sys")

from sklearn.ensemble import IsolationForest
from pathlib import Path
import joblib
import logging
# from utils.load_data import load_data_as_pandas_df

from src.utils import load_data
# import utils.load_data as load_data 

# fix the error No module named 'utils'


from data_processing.features import features_selection
import config

logger = logging.getLogger("ml_pipeline")


def model_train_save(train_data, n_estimators, contamination, sample_size, model_path):
    # Train the model
    model = IsolationForest(n_estimators=n_estimators, contamination=contamination, random_state=0, max_samples=sample_size)
    model.fit(train_data)
    logger.info("Model trained successfully")

    # Save the model
    model_path = Path(model_path)
    model_path.mkdir(parents=True, exist_ok=True)
    with open(model_path / "modelname.joblib", "wb") as f:
        joblib.dump(model, f)
    logger.info("Model saved successfully")

    return model


def training_pipeline(n_estimators, contamination, sample_size, model_path, data_file_path):
    data = load_data_as_pandas_df(data_file_path)
    logger.info("Data loaded successfully")
    data.head()
    featurs = features_selection(data)
    model = model_train_save(featurs, n_estimators, contamination, sample_size, model_path)
    logger.info("Model trained and saved successfully")
    return model


if __name__ == "__main__":
    n_estimators = config.n_estimators
    contamination = config.contamination
    sample_size = config.sample_size
    model_path = config.model_path
    data_file_path = config.data_file_path
    model = training_pipeline(n_estimators, contamination, sample_size, model_path, data_file_path)