import logging
import numpy as np

logger = logging.getLogger("ml_pipeline")# Select features


def features_selection(data):
    features = data[['CO(GT)', 'C6H6(GT)', 'NOx(GT)', 'NO2(GT)']]
    # Drop rows with missing values (-200)
    features = features.replace(-200, np.nan)
    features = features.dropna()
    logger.info("Features selected successfully")
    logger.info("Shape of features: {}".format(features.shape))
    return features