
import logging.config
import os
import json
from datetime import datetime as dt

def setup_filename_for_handlers(cfg):
  """
  Auto-completes the `filename` param for each handler in the logging config if it is an empty string.
  """
  LOGS_DIR = '_logs'
  session_id = dt.now().strftime('%Y%m%d_%H%M%S_%f')
  os.makedirs(LOGS_DIR, exist_ok=True)

  for handler_name, handler_cfg in cfg['handlers'].items():
    if handler_cfg.get('filename') == '{}':
      handler_cfg['filename'] = handler_cfg['filename'].format('{}/{}.log'.format(LOGS_DIR, session_id))

  return session_id

def configure_logging(config_path):
  """
  Loads and apply the json configuration for the logging module of the current project.
  """
  with open(config_path, 'r') as fp:
    cfg_logging = json.load(fp)

  session_id = setup_filename_for_handlers(cfg_logging)
  logging.config.dictConfig(cfg_logging)
  return session_id
