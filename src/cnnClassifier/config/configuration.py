from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig

 
class ConfigurationManager:
    """
        - Initializing for reading config and params file.
        - In config file we have the path for the artificats.
        - In params file we have all the parameters mention
    """
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])



    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
            This will return all the configuration for data ingestion. Like:
            - root folder:  This is a root folder named 'Artifacts/Ingestion/'
            - source url: This the url from where you can get the data set in zip format
            - local data file: This the path where that zip data set is saved
            - unzip directory: This is the path where that data set is unzip and saved
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
                                                    root_dir=config.root_dir,
                                                    source_URL=config.source_URL,
                                                    local_data_file=config.local_data_file,
                                                    unzip_dir=config.unzip_dir 
                                                )
        return data_ingestion_config
    

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_directories([config.root_dir])
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config