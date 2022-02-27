import logging
def my_log(name):
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	# create file handler which logs even debug messages
	debug_logger = logging.FileHandler('app.log')
	debug_logger.setLevel(logging.DEBUG)
	# create console handler with a higher log level
	info_logger = logging.StreamHandler()
	info_logger.setLevel(logging.INFO)
	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	info_logger.setFormatter(formatter)
	debug_logger.setFormatter(formatter)
	# add the handlers to logger
	logger.addHandler(info_logger)
	logger.addHandler(debug_logger)

	return logger