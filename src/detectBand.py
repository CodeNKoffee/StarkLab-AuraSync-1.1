import asyncio
from bleak import BleakScanner
import os
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MI_MAC_ADDRESS = os.getenv('MI_MAC_ADDRESS', '').lower()
PIXEL_MAC_ADDRESS = os.getenv('PIXEL_MAC_ADDRESS', '').lower()
print(f"MI_MAC_ADDRESS: {MI_MAC_ADDRESS}")
print(f"PIXEL_MAC_ADDRESS: {PIXEL_MAC_ADDRESS}")

def wake_nova():
  try:
    # Execute the command to wake the Mac
    result = subprocess.run(
      ["caffeinate", "-u", "-t", "1"], check=True, capture_output=True
    )
    print(f"Standard Output: {result.stdout.decode()}")
    print(f"Standard Error: {result.stderr.decode()}")
  except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")


async def scan_for_device():
  print("Scanning for devices...")
  devices = await BleakScanner.discover()
  for device in devices:
    print(f"Detected device: {device.name} - {device.address}")
    # print(f"Details: {device}")
    if device.address.lower() in [MI_MAC_ADDRESS, PIXEL_MAC_ADDRESS]:
      print(f"Target device detected with address: {device.address}")
      wake_nova()
      return True
  return False

if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  while True:
    found = loop.run_until_complete(scan_for_device())
    if found:
      print("Device connected")
      break
    print("Device not found. Rescanning in 10 seconds...")
    loop.run_until_complete(asyncio.sleep(10))
