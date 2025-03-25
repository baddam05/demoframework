import logging
import os

class loggen:
    @staticmethod
    def getlog():
        #log_dir = os.path.join(os.getcwd(), "logs")
        if not os.path.exists("logs"):#checking logs directory whether exists or not
            os.makedirs("logs") #if not create one

        log_file = "logs/automation.log" #creating logs file in logs directory

        logger = logging.getLogger("customLogger")# getting one specific logger from many by giving name
        logger.setLevel(logging.INFO)# setting level to logger

        # Add handler only if it's not already added
        #if not logger.handlers:
        file_handler = logging.FileHandler(log_file,mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger
