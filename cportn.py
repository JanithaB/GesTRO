import serial.tools.list_ports
import time

def detect_esp32_com_port():
    # List all available serial ports
    ports = serial.tools.list_ports.comports()

    for port, desc, hwid in sorted(ports):
        try:
            # Try to open the serial port
            ser = serial.Serial(port, baudrate=115200, timeout=2)

            # Wait for a short moment to receive data
            time.sleep(1)

            # Read the data from the port
            data = ser.readline()

            # Check if the data contains any expected information
            if data:
                ser.close()
                return port

            ser.close()

        except (OSError, serial.SerialException):
            pass
            
    return None

