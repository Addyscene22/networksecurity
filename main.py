from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
import sys 
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.components.Model_Trainer import ModelTrainer
from networksecurity.entity.config_entity import ModelTrainerConfig

if __name__ =="__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation comppleted")
        print(dataingestionartifact)
        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate the data validation config")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data vlaidation Completed")
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)

        logging.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

       
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)