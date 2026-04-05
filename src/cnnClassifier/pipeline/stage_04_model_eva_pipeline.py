from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_eva_components import Evaluation
from src.cnnClassifier import logger
import os


STAGE_NAME = "Evaluation stage"




class EvaluationPipeline:
    def __init__(self):
        pass
        # os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Mansiphopale/kidney_tumor_prediction_project.mlflow"
        # # Set your DagsHub credentials (MLflow uses HTTP Basic Auth)
        # os.environ["MLFLOW_TRACKING_USERNAME"] = "Mansiphopale"
        # os.environ["MLFLOW_TRACKING_PASSWORD"] = "deeb02e71df1418bbf4e0e119b8058fc4774e721"


    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        #evaluation.log_into_mlflow()






