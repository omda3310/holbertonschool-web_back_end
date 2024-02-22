#!/usr/bin/env python3
"""
 A function called filter_datum that returns the log message obfuscated
"""

import os
import re
from typing import List


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
