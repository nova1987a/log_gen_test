#!/usr/bin/python3

import pytest
import logging
import os
from datetime import datetime

# create "logs" folder
if not os.path.exists('logs'):
    os.makedirs('logs')

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    log_file = f"logs/test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # catch the result and records to the Log
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        logging.info(f"Test {item.nodeid} - Result: {report.outcome}")
