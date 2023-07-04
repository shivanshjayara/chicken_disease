from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path #from config.yaml
    base_model_path: Path #from config.yaml
    updated_base_model_path: Path #from config.yaml
    
    params_image_size: list #from params.yaml
    params_learning_rate: float #from params.yaml
    params_include_top: bool #from params.yaml
    params_weights: str #from params.yaml
    params_classes: int #from params.yaml

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path