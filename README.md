# AuraSync

AuraSync is a project developed by StarkLab for synchronizing data with external devices.

## Introduction

AuraSync facilitates the communication between your application and external devices, such as the Mi Band, through Bluetooth Low Energy (BLE) services. This allows your application to perform various tasks, such as detecting device presence and initiating actions based on device events.

## Installation

To install AuraSync, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd AuraSync
   ```

3. Install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Create a virtual environment and activate it:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use AuraSync in your project, follow these steps:

1. Ensure you have the necessary environment variables set in the `.env` file:

   ```python
   DEVICE_MAC_ADDRESS=XX:XX:XX:XX:XX:XX
   ```

2. Run the Python script to start scanning for the device:

   ```bash
   python src/detectBand.py
   ```

## Script Details

The `detectBand.py` script performs the following functions:

1. Imports necessary modules:

   ```python
   import asyncio
   from bleak import BleakScanner
   import os
   from dotenv import load_dotenv
   import subprocess
   ```

2. Loads environment variables:

   ```python
   load_dotenv()
   MAC_ADDRESS = os.getenv('DEVICE_MAC_ADDRESS')
   ```

3. Defines the device detection and action execution logic:

   ```python
   def wake_nova():
    result = subprocess.run(['caffeinate', '-u', '-t', '1'], capture_output=True, text=True)
    print(f"Output: {result.stdout}")
    print(f"Error: {result.stderr}")

    async def run():
      scanner = BleakScanner()
      devices = await scanner.discover()
      for device in devices:
        if device.address.lower() == MAC_ADDRESS.lower():
          print("Mi Band detected")
          wake_nova()
          break

    asyncio.run(run())
   ```

## License

This project is currently not licensed. It is part of StarkLab projects and is under control of StarkLab. Any use, modification, or redistribution is subject to StarkLab's policies.