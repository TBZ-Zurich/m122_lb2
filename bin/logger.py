import logging

# Create and configure logger
logging.basicConfig(filename="git-tool.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

# Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")


def logInformation(information):
    logString = "INFO: " + information

    print(logString)
    logger.info(logString)


def logWarning(warning):
    logString = "WARN: " + warning

    print(logString)
    logger.info(logString)


def logError(error):
    logString = "ERROR: " + error

    print(logString)
    logger.info(logString)
