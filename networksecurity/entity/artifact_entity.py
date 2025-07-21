from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    validated_train_file_path: str = None
    validated_test_file_path: str = None
    invalid_train_file_path: str = None
    invalid_test_file_path: str = None
    drift_report_file_path: str = None
    message: str = ""

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path : str
    trained_train_file_path : str
    test_train_file_path: str

@dataclass
class ClassificationMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float
    
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    train_metric_artifact: ClassificationMetricArtifact
    test_metric_artifact: ClassificationMetricArtifact