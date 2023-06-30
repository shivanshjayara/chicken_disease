from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig


 
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