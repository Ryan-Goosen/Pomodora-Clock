import os

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

    def _write_file(self, input_study_time, input_rest_time, input_study_extension, input_rest_extension, input_num_sessions):
        self.config = ConfigParser()
        if os.path.exists(self.file_path):
            self.config.read(self.file_path)

        if 'app' not in self.config:
            self.config['app'] = {}
        app = self.config['app']

        app['study_time'] = input_study_time
        app['rest_time'] = input_rest_time
        app['study_extension'] = input_study_extension
        app['rest_extension'] = input_rest_extension
        app['num_sessions'] = input_num_sessions

        # Write updated config back to file
        with open(self.file_path, 'w') as configfile:
            self.config.write(configfile)

    def get_data(self):
        return self.parsed_data