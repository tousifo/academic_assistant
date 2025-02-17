import serial

class SerialController:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        self.ser = None
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            self.ser.flush()
            print("Serial connection established")
        except Exception as e:
            print(f"Serial connection failed: {e}")

    def move_forward(self):
        return self.send_command(b'F')
    
    def move_backward(self):
        return self.send_command(b'B')
    
    def turn_left(self):
        return self.send_command(b'L')
    
    def turn_right(self):
        return self.send_command(b'R')
    
    def dance(self):
        return self.send_command(b'D')
    
    def show_happy(self):
        return self.send_command(b'S')
    
    def show_love(self):
        return self.send_command(b'V')  # Changed from 'L' to 'V'
    
    def greeting_smile(self):
        return self.send_command(b'G')  # New command for greeting expression

    def super_happy(self):
        return self.send_command(b'H')  # New command for super happy expression

    def send_command(self, command):
        if self.ser:
            try:
                self.ser.write(command)
                return True
            except Exception as e:
                print(f"Failed to send command: {e}")
        return False

    def close(self):
        if self.ser:
            self.ser.close()
