import os
import shutil

from .setup_logging import configure_logging
from .logger_wrapper import LoggerWrapper

path_config_logger_template = 'pylogger/.config_logger.json'
path_config_logger = 'pylogger/config_logger.json'

if not os.path.exists(path_config_logger):
  shutil.copy(path_config_logger_template, path_config_logger)

configure_logging(path_config_logger)


