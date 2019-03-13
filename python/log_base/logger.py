import os
import logging
import logging.config
import yaml
import sys

LEVEL = {
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}


def disable_existing_loggers(logger_name):
    """Disable existing loggers given a name
    
    Args:
        logger_name (str): Logger name
    """
    log_dict = logging.root.manager.loggerDict
    for logger in log_dict:
        if logger_name in logger:
            log_dict[logger].disabled = True


def setup_logger(debug_level="ERROR", config_file=""):
    """Setup logging configuration. To set up the logger, call this function in your main script.
    To get the logger in other modules, call `log = logging.getLogger(__name__)` in each module,
    it will automatically get the setup configuration.
    
    Args:
        debug_level (str): Debug level as string.
        config_file (str): Yaml configuration file.
    
    Returns:
        obj: Logging object.
    
    Examples:
        >>> log = setup_logger(debug_level='DEBUG')#It will show: 2018-03-10 09:05:14 DEBUG [test.py:6]: Debug log_base
        >>> log.debug("Debug log_base") #doctest: +ELLIPSIS
        20... DEBUG [<doctest python.log_base.logger.setup_logger[1]>:1]: Debug log_base
        >>> log.info("Debug log_base") #doctest: +ELLIPSIS
        20... INFO [<doctest python.log_base.logger.setup_logger[2]>:1]: Debug log_base
        >>> log = setup_logger(debug_level='INFO', config_file='python/log_base/logging.yaml')
        >>> log.error("Error log_base") #doctest: +ELLIPSIS
        20... ERROR [<doctest python.log_base.logger.setup_logger[4]>:1]: Error log_base
        >>> log.debug("Debug log_base") #should return nothing because log level is set to info

        >>> os.environ['DEBUG_LEVEL'] = "DEBUG"
        >>> log = setup_logger(debug_level='INFO')
        >>> log.debug("Debug log_base") #doctest: +ELLIPSIS
        20... DEBUG [<doctest python.log_base.logger.setup_logger[8]>:1]: Debug log_base
    
    """
    level = LEVEL.get(debug_level, None)

    # Get environment debug level if it is defined (then overwrite level in code)
    env = os.getenv("DEBUG_LEVEL", None)
    env_level = LEVEL.get(env, None)
    if env_level is not None:
        level = env_level

    # Get logger
    log = logging.getLogger()
    log.setLevel(level)

    # Format logger
    if config_file:
        try:
            with open(config_file, "rt") as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        except:
            raise
    else:
        console = logging.StreamHandler(stream=sys.stdout)
        format_str = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)s]: %(message)s"
        format_time = "%Y-%m-%d %H:%M:%S"
        console.setFormatter(logging.Formatter(format_str, format_time))
        log.addHandler(console)

    return log

