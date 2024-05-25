from src.text_summarizer.config.configuration import configManager
from src.text_summarizer.components.model_trainer import ModelTrainer
from src.text_summarizer.logging import logger



class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
      config = configManager()
      model_trainer_config = config.get_model_trainer_config()
      model_trainer_config = ModelTrainer(config=model_trainer_config)
      model_trainer_config.train()