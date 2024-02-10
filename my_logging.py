#!/usr/bin/env python3

import logging
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("debug")
# logging.info("info")
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
