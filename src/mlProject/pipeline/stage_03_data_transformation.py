from mlProject.config.configuration import ConfigurationManager
from mlProject.components.Data_transformation import DataTransformation
from mlProject import logger


STAGE_NAME = "Data Tranformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nX-----------------X")
    except Exception as e:
        logger.exception("f An error occurred while executing the Data Ingest stage.\n {e}")