import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

class R2R_DAC:
    def init(self, dynamic_range):
        self.dynamic_range = dynamic_range
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print("Ошибка")
            return
            
        number = int(voltage/self.dynamic_range * 4095)
        self.set_number(number)

try:
    dac = r2r.R2R_DAC(5.0)
    while True:
        start_time = time.perf_counter()
        sg.wait_for_sampling_period(sampling_frequency)
        t = time.perf_counter()
        normalized_value = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = normalized_value*amplitude
        dac.set_voltage('OUT', voltage)
except ValueError:
    print("Вы ввели не число. Попробуйте еще раз\n")
finally:
    dac.deinit()


