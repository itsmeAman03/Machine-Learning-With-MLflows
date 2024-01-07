from mlProject.config.configuration import ConfigurationManager
from mlProject.components.Data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path


STAGE_NAME = "Data Tranformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
        data_transform = DataTransformationTrainingPipeline()
        data_transform.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nX-----------------X")
    except Exception as e:
        logger.exception("f An error occurred while executing the Data Ingest stage.\n {e}")
        raise e