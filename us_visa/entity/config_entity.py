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

@dataclass
class DataValidationConfig:
    pass
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, constants.DATA_VALIDATION_DIR_NAME)
    drift_report_file_path: str = os.path.join(data_validation_dir, constants.DATA_VALIDATION_DRIFT_REPORT_DIR,
                                               constants.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
    
@dataclass
class DataTransformationConfig:
    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, constants.DATA_TRANSFORMATION_DIR_NAME)
    transformed_train_file_path: str = os.path.join(data_transformation_dir, constants.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    constants.TRAIN_FILE_NAME.replace("csv", "npy"))
    transformed_test_file_path: str = os.path.join(data_transformation_dir, constants.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                   constants.TEST_FILE_NAME.replace("csv", "npy"))
    transformed_object_file_path: str = os.path.join(data_transformation_dir,
                                                     constants.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                     constants.PREPROCSSING_OBJECT_FILE_NAME)    