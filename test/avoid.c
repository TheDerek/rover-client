#include <wiringPi.h>
#include <softPwm.h>
#include <unistd.h>

/*
def pulse(port):
    GPIO.output(port, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(port, GPIO.LOW)
*/ 

const int MOTOR_1A = 4;
const int MOTOR_1B = 1;
const int MOTOR_1E = 3;
const int MOTOR_2A = 19;
const int MOTOR_2B = 21;
const int MOTOR_2E = 23;

const int TRIG = 31;
const int ECHO = 32;

void forward(int power);

int main()
{
    wiringPiSetupGpio();
    pinMode(MOTOR_1A, OUTPUT);
    pinMode(MOTOR_1B, OUTPUT);
    pinMode(MOTOR_2A, OUTPUT);
    pinMode(MOTOR_2B, OUTPUT);
    softPwmCreate(MOTOR_2E, OUTPUT, 100);
    softPwmCreate(MOTOR_1E, OUTPUT, 100);

    pinMode(TRIG, OUTPUT);
    pinMode(ECHO, INPUT);
    forward(100);
}

void forward(power)
{
    softPwmWrite(MOTOR_1E, power);
    softPwmWrite(MOTOR_2E, power);
    pinMode(MOTOR_1A, HIGH);
    pinMode(MOTOR_1B, LOW);
    pinMode(MOTOR_2A, HIGH);
    pinMode(MOTOR_2B, LOW);
}
