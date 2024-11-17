# 09-Debugging with Assertions and Logging

https://www.pythoncheatsheet.org/cheatsheet/debugging

## Assertions

An assertion is a sanity check to make sure your code isn’t doing something obviously wrong. These sanity checks are performed by assert statements. 
If the assertion fails, an `AssertionError` exception is raised. 
In code, an assert has the following format:

```python
    assert <boolean_expression> , <string_printed_if_condition_fails>
```
Example

```python
pod_bay_door_status = 'it is definitely not open.'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'

# Traceback (most recent call last):
#   File "<pyshell#10>", line 1, in <module>
#     assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
# AssertionError: The pod bay doors need to be "open".
```

### Disabling Assertions
Assertions can be disabled by passing the `-O` option when running Python

## Logging
https://realpython.com/python-logging/
https://arjancodes.com/blog/how-to-set-up-python-logging-module/

To enable the `logging` module needs to be imported together with the **loggin configuration**:

```python
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
```

### Logging levels

| Level    | Logging Function   | Description                                                                                                                    |
|----------|--------------------|--------------------------------------------------------------------------------------------------------------------------------|
| DEBUG    | `logging.debug()`   | The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.                 |
| INFO     | `logging.info()`    | Used to record information on general events in your program or confirm that things are working at their point in the program. |
| WARNING  | `logging.warning()`  | Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.              |
| ERROR    | `logging.error()`    | Used to record an error that caused the program to fail to do something.                                                       |
| CRITICAL | `logging.critical()` | The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.   |

### Logging format

The `LogRecord` has a number of attributes, most of which are derived from the parameters to the constructor.
(Note that the names do not always correspond exactly between the LogRecord constructor parameters and the LogRecord attributes.) These attributes can be used to merge data from the record into the format string. 

If you are using **{}-formatting** (`str.format()`), you can use `{attrname}` as the placeholder in the format string. 
If you are using **$-formatting** (`string.Template`), use the form `${attrname}`.

In the case of **{}-formatting**, you can **specify formatting flags by placing them after the attribute name**, 
separated from it with a colon. 
For example: a placeholder of `{msecs:03.0f}` would format a millisecond value of 4 as 004. 
Refer to the `str.format()` documentation for full details on the options available to you.

| Attribute name  | Format                                         | Description                                                                                                                                                                                                      |
|-----------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| args            | You shouldn’t need to<br>format this yourself. | The tuple of arguments merged into msg to<br>produce message, or a dict whose values<br>are used for the merge (when there is only one<br>argument, and it is a dictionary).                                     |
| asctime         | %(asctime)s                                    | Human-readable time when the<br>LogRecord was created.  By default<br>this is of the form ‘2003-07-08 16:49:45,896’<br>(the numbers after the comma are millisecond<br>portion of the time).                     |
| created         | %(created)f                                    | Time when the LogRecord was created<br>(as returned by time.time_ns() / 1e9).                                                                                                                                    |
| exc_info        | You shouldn’t need to<br>format this yourself. | Exception tuple (à la sys.exc_info) or,<br>if no exception has occurred, None.                                                                                                                                   |
| filename        | %(filename)s                                   | Filename portion of pathname.                                                                                                                                                                                    |
| funcName        | %(funcName)s                                   | Name of function containing the logging call.                                                                                                                                                                    |
| levelname       | %(levelname)s                                  | Text logging level for the message<br>('DEBUG', 'INFO', 'WARNING',<br>'ERROR', 'CRITICAL').                                                                                                                      |
| levelno         | %(levelno)s                                    | Numeric logging level for the message<br>(DEBUG, INFO,<br>WARNING, ERROR,<br>CRITICAL).                                                                                                                          |
| lineno          | %(lineno)d                                     | Source line number where the logging call was<br>issued (if available).                                                                                                                                          |
| message         | %(message)s                                    | The logged message, computed as msg %<br>args. This is set when<br>Formatter.format() is invoked.                                                                                                                |
| module          | %(module)s                                     | Module (name portion of filename).                                                                                                                                                                               |
| msecs           | %(msecs)d                                      | Millisecond portion of the time when the<br>LogRecord was created.                                                                                                                                               |
| msg             | You shouldn’t need to<br>format this yourself. | The format string passed in the original<br>logging call. Merged with args to<br>produce message, or an arbitrary object<br>(see Using arbitrary objects as messages).                                           |
| name            | %(name)s                                       | Name of the logger used to log the call.                                                                                                                                                                         |
| pathname        | %(pathname)s                                   | Full pathname of the source file where the<br>logging call was issued (if available).                                                                                                                            |
| process         | %(process)d                                    | Process ID (if available).                                                                                                                                                                                       |
| processName     | %(processName)s                                | Process name (if available).                                                                                                                                                                                     |
| relativeCreated | %(relativeCreated)d                            | Time in milliseconds when the LogRecord was<br>created, relative to the time the logging<br>module was loaded.                                                                                                   |
| stack_info      | You shouldn’t need to<br>format this yourself. | Stack frame information (where available)<br>from the bottom of the stack in the current<br>thread, up to and including the stack frame<br>of the logging call which resulted in the<br>creation of this record. |
| thread          | %(thread)d                                     | Thread ID (if available).                                                                                                                                                                                        |
| threadName      | %(threadName)s                                 | Thread name (if available).                                                                                                                                                                                      |
| taskName        | %(taskName)s                                   | asyncio.Task name (if available).                                                                                                                                                                                |

#### Default formatting `%(attrname)s`

```python
import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    style='%', #default
    datefmt='%Y-%m-%d %H:%M:%S',
    )


logging.info('This is my log') # 2024-11-10 10:23:56 - root - INFO - This is my log

#Use the modulo operator % for string interpolation
name = "Samara"
logging.info("name=%s", name) #2024-11-10 10:43:58 - root - INFO - name=Samara
```
#### String formatting `{` style

```python
import logging

# Configure basic logging with {} style formatting
logging.basicConfig(
    level=logging.INFO,
    format='{asctime} {levelname}: {message}',
    datefmt='%Y-%m-%d %H:%M:%S',
    style='{'
)

logging.info('This is an informational message.') # 2024-11-10 10:30:38 INFO: This is an informational message.

# use the string.format
name = "Samara"
logging.info(f"{name=}") #2024-11-10 10:45:41 INFO: name='Samara'
```

#### String templating `$` style

```python
import logging

# Configure basic logging with {} style formatting
logging.basicConfig(
    level=logging.INFO,
    format='{asctime} {levelname}: {message}',
    datefmt='%Y-%m-%d %H:%M:%S',
    style='{'
)

logging.info('This is an informational message.') # 2024-11-10 10:30:38 INFO: This is an informational message.

# use the string.format
name = "Samara"
logging.info(f"{name=}") #2024-11-10 10:45:41 INFO: name='Samara'
```

### Using a named `Logger`

While **utilizing the root logger** (basic config) is the simplest way to log messages and is fine in small applications, 
**it’s not recommended for larger applications**.

We can create a new logger by calling the `getLogger` method and **passing in the name of the logger**. 
This will create a new logger with the name we passed in.

It’s common to use `__name__` as the name of the logger, as this will create a logger with the name of the module that the logger is created in.

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('This is an info message')
```

We can define multiple **handlers** in a logger, so that we can customize the log configuration.


### Logging to a file

#### Logging to a file using `BasicConfig`

```python
import logging
logging.basicConfig(
    filename='myProgramLog.txt', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Log statement example") #2024-11-17 15:56:10,122 - INFO - Log statement example
```

#### Logging to a file using `FileHandler` in a `Logger`

```python
import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('app.log')
logger.addHandler(file_handler)
```

We can introduce a `RotatingFileHandler` to rotate log files and a console handler to log 
to the console and to the file at the same time

```python
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) #master log level (handlers will not log below this level)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.handlers.RotatingFileHandler(
    'app.log',
    maxBytes=1000,
    backupCount=3
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
# create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```
#### Configure logger and handlers with dict config

```python
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

```
### Filter log messages

```python
import logging
# Class inherits from logging.Filter class
class ImportantFilter(logging.Filter):
    def filter(self, record):
	    return 'important' in record.getMessage()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('my_logger')

logger.addFilter(ImportantFilter())
logger.info('This is a regular message')
logger.info('This is an important message')
```
