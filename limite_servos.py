import time
import wiringpi

PIN_PWM = 2    # Ajuste pino wPi correto
ARR = 4000
CLK = 120

def setup_pwm():
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(PIN_PWM, wiringpi.PWM_OUTPUT)
    wiringpi.pwmSetMode(PIN_PWM, wiringpi.PWM_MODE_MS)
    wiringpi.pwmSetRange(PIN_PWM, ARR)
    wiringpi.pwmSetClock(PIN_PWM, CLK)

def test_servo():
    setup_pwm()
    while True:
        # Digite aqui valores “manuais” de CCR
        for ccr in [100, 150, 200, 250, 300, 350, 400, 450]:
            print(f"Enviando CCR={ccr}")
            wiringpi.pwmWrite(PIN_PWM, ccr)
            time.sleep(2)

if __name__ == "__main__":
    test_servo()
