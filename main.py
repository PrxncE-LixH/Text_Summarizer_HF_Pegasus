from src.text_summarizer.pipeline.stage_01_ingestion import DataIngestionTrainingPipeline
from src.text_summarizer.logging import logger
from src.text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.text_summarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.text_summarizer.pipeline.stage_05_model_eval import ModelEvaluationTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"++++++++++++++++++++++++++++++++")
    logger.info(f">>>>> {STAGE_NAME} started <<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<< \n\nx===========X")
    
except Exception as e:
    logger.exception(e)
    raise e
 
 
 
 
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"--------------------------------")
    logger.info(f">>>>> {STAGE_NAME} started <<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<< \n\nx===========X")
    
except Exception as e:
    logger.exception(e)
    raise e
 
 

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    logger.info(f">>>>> {STAGE_NAME} started <<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<< \n\nx===========X")
    
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Training Stage"
try:
    logger.info(f"********************************")
    logger.info(f">>>>> {STAGE_NAME} started <<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<< \n\nx===========X")
    
except Exception as e:
    logger.exception(e)
    raise e
 
 
STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"##############################")
    logger.info(f">>>>> {STAGE_NAME} started <<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<< \n\nx===========X")
    
except Exception as e:
    logger.exception(e)
    raise e
 