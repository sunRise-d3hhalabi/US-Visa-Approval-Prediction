import os
# from us_visa.constants import *
from us_visa import constants
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = constants.PIPELINE_NAME
    artifact_dir: str = os.path.join(constants.ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, constants.DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, constants.DATA_INGESTION_FEATURE_STORE_DIR, constants.FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, constants.DATA_INGESTION_INGESTED_DIR, constants.TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, constants.DATA_INGESTION_INGESTED_DIR, constants.TEST_FILE_NAME)
    train_test_split_ratio: float = constants.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = constants.DATA_INGESTION_COLLECTION_NAME