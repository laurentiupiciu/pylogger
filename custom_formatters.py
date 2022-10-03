import logging

_COLORS = dict(
  grey = "\x1b[0;37m",
  green = "\x1b[1;32m", g = "\x1b[1;32m", success = "\x1b[1;32m",
  yellow = "\x1b[1;33m", warning = "\x1b[1;33m", y = "\x1b[1;33m", w = "\x1b[1;33m",
  red = "\x1b[1;31m", error = "\x1b[1;31m", r = "\x1b[1;31m", e = "\x1b[1;31m",
  bold_red = "\x1b[31;21m", critical = "\x1b[31;21m", c = "\x1b[31;21m",
  purple = "\x1b[1;35m", p = "\x1b[1;35m",
  blue = "\x1b[1;34m", b = "\x1b[1;34m",
  light_blue = "\x1b[1;36m",
  reset = "\x1b[0m",
)

class ColoredFormatter(logging.Formatter):

  def __init__(self, *args):
    super(ColoredFormatter, self).__init__(*args)
    if len(args) == 0:
      self._fmt = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"

    self.formats = self._get_formats()
    return

  def _format_with_color(self, color_code):
    return _COLORS[color_code] + self._fmt + _COLORS['reset']

  def _get_formats(self):
    return {
      logging.DEBUG    : self._format_with_color('purple'),
      logging.INFO     : self._fmt,
      logging.WARNING  : self._format_with_color('yellow'),
      logging.ERROR    : self._format_with_color('red'),
      logging.CRITICAL : self._format_with_color('bold_red')
    }

  def _get_log_fmt(self, record):
    if not isinstance(record.args, dict):
      return self.formats.get(record.levelno)

    color_code = record.args.get('color')
    color = _COLORS.get(color_code)
    if color is None:
      return self.formats.get(record.levelno)

    return self._format_with_color(color_code)

  def format(self, record):
    log_fmt = self._get_log_fmt(record=record)
    formatter = logging.Formatter(log_fmt)
    return formatter.format(record)
