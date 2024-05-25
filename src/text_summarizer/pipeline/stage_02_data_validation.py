from src.text_summarizer.config.configuration import configManager
from src.text_summarizer.components.data_validation import DataValidation
from src.text_summarizer.logging import logger




class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()