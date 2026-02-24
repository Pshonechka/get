import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_pin = gpio_pin
        self.freq = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial=0)
        self.pwm = GPIO.PWM(self.gpio_pin, self.freq)
        self.pwm.start(0)

        if self.verbose:
            print(f"PWM_DAC инициализирован на пине {self.gpio_pin}")

    def deinit(self):
        self.pwm.stop()
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
        if self.verbose:
            print("PWM_DAC деинициализирован")

    def set_voltage(self, voltage):
        if 0.0 <= voltage <= self.dynamic_range:
            duty_cycle = (voltage / self.dynamic_range) * 100.0
            self.pwm.ChangeDutyCycle(duty_cycle)
            if self.verbose:
                print(f"Установлено напряжение: {voltage:.3f} В, duty cycle = {duty_cycle:.1f}%")
        else:
            print(f"Напряжение {voltage:.2f} В выходит за диапазон (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            self.pwm.ChangeDutyCycle(0)


if __name__ == "__main__":
    dac = None
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        if dac is not None:
            dac.deinit()
