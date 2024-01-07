from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# we could also use src.mlProject rather than only mlProject


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nX-----------------X")
except Exception as e:
    logger.exception("f An error occurred while executing the Data Ingest stage.\n {e}")




STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nX-----------------X")
except Exception as e:
    logger.exception("f An error occurred while executing the Data Ingest stage.\n {e}")


STAGE_NAME = "Data Tranformation Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    data_transform = DataTransformationTrainingPipeline()
    data_transform.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nX-----------------X")
except Exception as e:
    logger.exception("f An error occurred while executing the Data Ingest stage.\n {e}")
    raise e