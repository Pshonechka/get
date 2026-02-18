import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.verbose = verbose
        self.dynamic_range = dynamic_range
    def deinit(self):
        self.bus.close()
    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return
        if not (0 <= number <=4095):
            print("Число выходит за разрядность MCP4725 (12 бит)")
            return
        first_byte = (number >> 4)& 0x0F
        second_byte = (number & 0xFF) << 4
        self.bus.write_byte_data(self.address, first_byte, second_byte)
        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print("Ошибка")
            return
            
        number = int(voltage/self.dynamic_range * 4095)
        self.set_number(number)
if name == "__main__":
    try:
        dac = MCP4725(5, 0x61, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах:"))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()