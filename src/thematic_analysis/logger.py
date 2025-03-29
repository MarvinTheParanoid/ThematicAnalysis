import logging


def get_logger() -> logging.Logger:
    """
    Get a logger instance for the thematic_analysis namespace.
    The logger will be configured according to the log_conf.yaml settings.

    Returns:
        logging.Logger: Configured logger instance
    """
    return logging.getLogger("thematic_analysis")
