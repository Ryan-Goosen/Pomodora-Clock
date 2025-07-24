import os

from configparser import ConfigParser
from distutils.file_util import write_file
from pathlib import Path

class Data:

    def __init__(self):
        self.file_path = Path('config/settings.ini')
        self.config = ConfigParser()
        self._read_file()  


    def _read_file(self):
        if not self.file_path.exists():
            self.write_file(
                input_study_time = 5,
                input_rest_time = 2,
                input_study_extension = 5,
                input_rest_extension = 0,
                input_num_sessions = 5)

        self.config.read(self.file_path)
        self._update_parsed_data()

    def _update_parsed_data(self):
        app = self.config['app']
        self.parsed_data = {
            'study_time': app.get('study_time'),
            'rest_time': app.get('rest_time'),
            'study_extension': app.get('study_extension'),
            'rest_extension': app.get('rest_extension'),
            'num_sessions': app.get('num_sessions')
        }

    def write_file(self, input_study_time, input_rest_time, input_study_extension, input_rest_extension, input_num_sessions):
        if 'app' not in self.config:
            self.config['app'] = {}
        app = self.config['app']

        app['study_time'] = str(input_study_time)
        app['rest_time'] = str(input_rest_time)
        app['study_extension'] = str(input_study_extension)
        app['rest_extension'] = str(input_rest_extension)
        app['num_sessions'] = str(input_num_sessions)

        # Write updated config back to file
        with open(self.file_path, 'w') as configfile:
            self.config.write(configfile)

        self._update_parsed_data()

    def get_data(self):
        return self.parsed_data