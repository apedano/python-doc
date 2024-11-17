import logging
import logging.config

# Custom logger configuration
custom_logger_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "customFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "formatter": "customFormatter",
            "level": "DEBUG"
        },
        "fileHandler": {
            "class": "logging.FileHandler",
            "formatter": "customFormatter",
            "level": "INFO",
            "filename": "app.log",
            "mode": "w"
        }
    },
    "loggers": {
        "customLogger": {
            "handlers": ["consoleHandler", "fileHandler"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}

# Apply the custom logger configuration
logging.config.dictConfig(custom_logger_config)

# Create the custom logger
logger = logging.getLogger("customLogger")

# Example log messages
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
