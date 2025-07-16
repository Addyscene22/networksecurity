from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
import sys 
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

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

       
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)