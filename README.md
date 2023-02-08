## Wrapper on native python logging module

- To be used as a submodule in other projects (name the submodule `pylogger`)
- Create somewhere in your project (outside `pylogger`) a file `config_logger.json` based on the template `.config_logger.json` that can be found in this repo
- Create somewhere in your project (outside `pylogger`) a file (you can name it `log.py`) with the following code:
    ```
    from pylogger.setup_logging import configure_logging
    from pylogger.logger_wrapper import LoggerWrapper
    
    path_config_logger = <path to config_logger.json>
    session_id = configure_logging(path_config_logger)

    log = LoggerWrapper(lib_name='std') # lib_name depends on the logger names that were provided in config_logger.json
    ```
