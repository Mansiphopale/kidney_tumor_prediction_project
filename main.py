from src.cnnClassifier.pipeline.stage_01_dataingpipeline import DataIngestionTrainingPipeline
from src.cnnClassifier import * 
from src.cnnClassifier.pipeline.stage_02_preparebasepipeline import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_training_pipeline import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_eva_pipeline import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  data_ingestion = DataIngestionTrainingPipeline()
  data_ingestion.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e

STAGE_NAME = "Prepare base model"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  prepare_base_model = PrepareBaseModelTrainingPipeline()
  prepare_base_model.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e


STAGE_NAME = "model training"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  model_trainer = ModelTrainingPipeline()
  model_trainer.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e
     
     
    
STAGE_NAME = "model evaluation"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  model_eva = EvaluationPipeline()
  model_eva.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e