## Wrapper on native python logging module

- To be used as a submodule in other projects (name the submodule `pylogger`)
- The default logger configuration is `.config_logger.json`. The package automatically creates `config_logger.json` which is used to configure the native `logging` module
- Instantiate a `LoggerWrapper` using a name from `config_logger.json`. Use it in your project.
