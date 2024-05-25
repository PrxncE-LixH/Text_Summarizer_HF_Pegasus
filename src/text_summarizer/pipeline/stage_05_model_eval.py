from src.text_summarizer.config.configuration import configManager
from src.text_summarizer.components.model_evaluation import ModelEvaluation
from src.text_summarizer.logging import logger



class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
      config = configManager()
      model_evaluation_config = config.get_model_evaluation_config()
      model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
      model_evaluation_config.evaluate()