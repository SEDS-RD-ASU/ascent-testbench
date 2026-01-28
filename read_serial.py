import pigpio
import time

def main():
    pi = pigpio.pi()
    serial_handle = pi.serial_open('/dev/ttyAMA0', 115200)
    print(f"Serial handle: {serial_handle}")
    
    while True:
        available_bytes = pi.serial_data_available(serial_handle)
        if available_bytes > 0:
            count, data = pi.serial_read(serial_handle, available_bytes)
            if count > 0:
                text = data.decode('utf-8', errors='replace')
                print(text, end='')
        time.sleep(0.01)

if __name__ == '__main__':
    main()