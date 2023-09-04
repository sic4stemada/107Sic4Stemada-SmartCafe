from __future__ import division
import time
import Adafruit_PCA9685

# Inisialisasi PCA9685 menggunakan alamat default (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Atur frekuensi PWM ke 60Hz (baik untuk servos).
pwm.set_pwm_freq(60)

# Configure min dan max servo pulse lengths
servo_min = 150  # Panjang pulsa minimum (0 derajat)
servo_max = 600  # Panjang pulsa maksimum (180 derajat)

# Menghitung panjang pulsa untuk 60 derajat
target_degrees = 60
target_pulse = int(servo_min + (target_degrees / 180.0 * (servo_max - servo_min)))

print('Moving servo on channel 0...')
try:
     time.sleep(1)
     pwm.set_pwm(12, 1, target_pulse)
     time.sleep(1)
     pwm.set_pwm(12, 1, servo_min)
     time.sleep(1)

     time.sleep(1)
     pwm.set_pwm(8, 1, target_pulse)
     time.sleep(1)
     pwm.set_pwm(8, 1, servo_min)
     time.sleep(1)
     
     time.sleep(1)
     pwm.set_pwm(4, 1, target_pulse)
     time.sleep(1)
     pwm.set_pwm(4, 1, servo_min)
     time.sleep(1)

     time.sleep(1)
     pwm.set_pwm(2, 1, target_pulse)
     time.sleep(1)
     pwm.set_pwm(2, 1, servo_min)
     time.sleep(1)
    
except KeyboardInterrupt:
    # Tangani jika pengguna menekan Ctrl-C
    pwm.set_pwm(0, 0, 0)  # Pastikan servo dimatikan sebelum keluar

# Bersihkan GPIO saat selesai
pwm.set_pwm(0, 0, 0)
