from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_validation import DataValidation
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataValidationConfig, DataTransformationConfig
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import ModelTrainerConfig

import sys

if __name__ == "__main__":
  try:
    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config)
    logging.info("Initiate the data ingestion")
    data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    print(data_ingestion_artifact)
    data_validation_config = DataValidationConfig(training_pipeline_config)
    data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
    logging.info("Initiate the data validation")
    data_validation_artifact = data_validation.initiate_data_validation()
    logging.info("data validation completed")
    print(data_validation_artifact)
    data_tansformation_config = DataTransformationConfig(training_pipeline_config)
    logging.info("data transformation started.")
    data_transforamtion = DataTransformation(data_validation_artifact,data_tansformation_config)
    data_transformation_artifact = data_transforamtion.initiate_data_transformation()
    print(data_transformation_artifact)
    logging.info("data transformation completed.")

    logging.info("Model Training sstared")
    model_trainer_config=ModelTrainerConfig(training_pipeline_config)
    model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
    model_trainer_artifact=model_trainer.initiate_model_trainer()
    
  except Exception as e:
    raise NetworkSecurityException(e,sys)