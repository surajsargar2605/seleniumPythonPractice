import logging


class Loggen:

    @staticmethod
    def Loggen():
        logging.basicConfig(filename=".//Logs//automation.log",
                            force=True,
                            format="%(asctime)s:%(levelname)s:%(message)s:"
                            )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
