#!/usr/bin/env python3

import platform

def get_system_info():
  """Retrieves and prints system information."""
  os_name = platform.system()
  os_release = platform.release()
  os_version = platform.version()
  machine_type = platform.machine()
  processor_info = platform.processor()

  print(f"OS Name: {os_name}")
  print(f"OS Release: {os_release}")
  print(f"OS Version: {os_version}")
  print(f"Machine Type: {machine_type}")
  print(f"Processor Information: {processor_info}")

if __name__ == "__main__":
  get_system_info()
