from .setup_logging import configure_logging
from .logger_wrapper import LoggerWrapper

configure_logging('log/config_logger.json')
lw = LoggerWrapper(lib_name='data_analysis')
