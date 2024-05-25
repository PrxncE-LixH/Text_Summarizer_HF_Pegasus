from src.text_summarizer.config.configuration import configManager
from src.text_summarizer.components.data_ingestion import DataIngestion
from src.text_summarizer.logging import logger




class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()