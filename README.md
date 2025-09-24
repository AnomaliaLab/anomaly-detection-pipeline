# anomaly-detection
Basic learning of anomaly detection

This project provides a modular pipeline for anomaly detection using machine learning techniques. It is designed for flexibility and extensibility, supporting various data sources and logging configurations.

## Features

- **Data Loading**: Utilities to load data from CSV, databases, APIs, S3, HDFS, FTP, HTTP, and Kafka streams (src/utils/load_data.py).
- **Synthetic Data Generation**: Functions to generate synthetic training and scoring datasets for experimentation and benchmarking.
- **Feature Engineering**: Selection and preprocessing of relevant features for anomaly detection (src/data_processing/features.py).
- **Model Training**: Training and saving of anomaly detection models (e.g., Isolation Forest) with configurable parameters (src/models/training.py).
- **Prediction Pipeline**: Loading trained models and making predictions on new data (src/models/prediction.py).
- **Logging**: Centralized and configurable logging using a dedicated logging configuration file (config/logging.conf).
- **Jupyter Notebooks**: Example notebooks for exploratory data analysis, model training, scoring, and advanced techniques like autoencoders.

## Project Structure

```
config/         # Configuration files (logging, parameters)
data/           # Data storage (raw, processed)
docs/           # Documentation and design notes
notebooks/      # Jupyter notebooks for experiments and pipelines
src/            # Source code (data loading, processing, models)
```

## Getting Started

1. **Install dependencies**  
   Install required Python packages (see notebook cells for typical requirements: pandas, numpy, scikit-learn, joblib, etc.).

2. **Configure Logging**  
   Logging is set up via [`config/logging.conf`](config/logging.conf ). Logs are written to `logs/ml_pipeline.log` and the console.

3. **Run Notebooks or Scripts**  
   Use the notebooks in the [`notebooks`](notebooks ) directory for step-by-step workflows, or run scripts in [`src`](src ) for modular execution.

## Example Workflow

- Load and preprocess data using utilities in [`src/utils/load_data.py`](src/utils/load_data.py ).
- Select features with [`features_selection`](src/data_processing/features.py ).
- Train a model and save it with [`model_train_save`](src/models/training.py ).
- Predict anomalies on new data using [`prediction_pipeline`](src/models/prediction.py ).
- Visualize results and analyze anomalies in the provided notebooks.

## Documentation

See the [`docs`](docs ) folder for detailed documentation on architecture, data, code explanations, and advanced topics.

---

**Goal:**  
To provide a reproducible, extensible, and well-logged pipeline for anomaly detection tasks, supporting both