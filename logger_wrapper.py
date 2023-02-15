import logging

class LoggerWrapper(object):
  """
  Wrapper over one logger defined in the configuration file.
  If multiple loggers are defined in the configuration file, then multiple wrappers should be created.
  """
  def __init__(self, logger=None, lib_name=None, session_id=None):
    super(LoggerWrapper, self).__init__()
    if logger is not None:
      self._logger = logger
    else:
      assert lib_name is not None
      self._logger = logging.getLogger(lib_name)
    self.session_id = session_id
    return

  @property
  def logger(self):
    return self._logger

  def debug(self, msg):
    self._logger.debug(msg)
    return

  def info(self, msg):
    self._logger.info(msg)
    return

  def cinfo(self, msg, color=None):
    self._logger.info(msg, dict(color=color))
    return

  def warning(self, msg):
    self._logger.warning(msg)
    return

  def error(self, msg, exc_info=False):
    self._logger.error(msg, exc_info=exc_info)
    return

  def critical(self, msg, exc_info=True):
    self._logger.critical(msg, exc_info=exc_info)
    return

  def success(self, msg):
    """
    Works only if log.custom_fornatters.ColoredFormatter is employed as a formatter for self._logger
    """
    self._logger.info(msg, dict(color='success'))
    return
