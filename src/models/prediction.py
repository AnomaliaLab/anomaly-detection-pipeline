import joblib
from pathlib import Path
import utils.load_data as load_data
import data_processing.features as features


def load_model(model_path):
    model_path = Path(model_path)
    with open(model_path / 'modelname.joblib', 'rb') as f:
        model = joblib.load(f)
    return model

def prediction_pipeline(data_file_path, model_path):
    # fetch data
    data = load_data.load_data_as_pandas_df(data_file_path)
    features_data = features.features_selection(data)

    data = data.loc[features_data.index].copy()
    
    # load model
    model = load_model(model_path)
    
    # make prediction
    data['anomaly_score'] = model.decision_function(features_data)
    data['anomaly'] = model.predict(features_data)
    
    return data