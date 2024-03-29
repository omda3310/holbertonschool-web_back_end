#!/usr/bin/env python3
"""
 A function called filter_datum that returns the log message obfuscated
"""

import os
import re
from typing import List
import logging
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """constructor of class"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Method to filter values in incoming log records using filter_datum
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating
    all fields in the log line (message)
    """
    for f in fields:
        message = re.sub(rf"{f}=.*?{separator}", f"{f}={redaction}{separator}",
                         message)
    return message


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)

    return Logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to the database
    """

    connx = mysql.connector.connect(
        username=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )
    return connx


def main():
    """
    Obtain a database connection using get_db and retrieve
    all rows in the users table and display each row
    """
    data = get_db()
    cursor = data.cursor()
    cursor.execute('SELECT * FROM users;')
    collects = []
    for collect in cursor:
        notice = f"name={collect[0]}; email={collect[1]}; " \
            f"phone={collect[2]}; ssn={collect[3]}; " \
            f"password={collect[4]}; ip={collect[5]}; " \
            f"last_login={collect[6]}; user_agent={collect[7]}"
        collects.append(notice)

    logg = get_logger()
    for coll in collects:
        logg.INFO(coll)

    cursor.close()
    data.close()


if __name__ == "__main__":
    main()
