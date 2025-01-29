import time
import wiringpi

PIN_PWM = 2  # wPi #2 = PWM15_IR_M1

def setup_hardware_pwm():
    # 1) Inicializa
    wiringpi.wiringPiSetup()  # ou wiringpi.wiringPiSetupGpio(), dependendo da sua placa
    # 2) Define o pino como PWM output
    wiringpi.pinMode(PIN_PWM, wiringpi.PWM_OUTPUT)
    # 3) Define o MODO de PWM (Mark-Space) → pwmSetMode(pin, mode)
    wiringpi.pwmSetMode(PIN_PWM, wiringpi.PWM_MODE_MS)  # PWM_MODE_MS é 0
    # 4) Define o range (ARR = 4000)
    wiringpi.pwmSetRange(PIN_PWM, 4000)
    # 5) Define o clock divisor (120)
    wiringpi.pwmSetClock(PIN_PWM, 120)
    # Com isso, frequência ~ 50Hz
    
def set_servo_ccr(ccr_value):
    """ Ajusta o duty cycle pela CCR no pino. """
    wiringpi.pwmWrite(PIN_PWM, ccr_value)

def test_servo():
    setup_hardware_pwm()
    while True:
        for ccr in [200, 300, 400]:
            print(f"CCR={ccr}")
            set_servo_ccr(ccr)
            time.sleep(1)

if __name__ == "__main__":
    test_servo()
