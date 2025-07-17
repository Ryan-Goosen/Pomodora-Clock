from configparser import ConfigParser
from pathlib import Path

class Data:

    def __init__(self):
        self.file_path = Path('config/settings.ini')
        self.config = None
        self.parsed_data = None
        self._read_file()  


    def _read_file(self):
        self.config = ConfigParser()
        self.config.read(self.file_path)

        app = self.config['app']
        self.parsed_data = {
            'study_time': app.get('study_time'),
            'rest_time': app.get('rest_time'),
            'study_extension': app.get('study_extension'),
            'rest_extension': app.get('rest_extension'),
            'num_sessions': app.get('num_sessions')
        }

    def get_data(self):       
        return self.parsed_data