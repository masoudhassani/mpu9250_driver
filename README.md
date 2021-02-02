Python3 driver for mpu9250 sensor:
https://learn.sparkfun.com/tutorials/mpu-9250-hookup-guide/all

# Installation
```
python3 -m pip install git+https://github.com/masoudhassani/mpu9250_driver.git
```

# Usage
```
import FaBo9Axis_MPU9250
mpu9250 = FaBo9Axis_MPU9250.MPU9250()

while True:
    accel = mpu9250.readAccel()
    print (" ax = " , ( accel['x'] ))
    print (" ay = " , ( accel['y'] ))
    print (" az = " , ( accel['z'] ))

    gyro = mpu9250.readGyro()
    print (" gx = " , ( gyro['x'] ))
    print (" gy = " , ( gyro['y'] ))
    print (" gz = " , ( gyro['z'] ))

    mag = mpu9250.readMagnet()
    print (" mx = " , ( mag['x'] ))
    print (" my = " , ( mag['y'] ))
    print (" mz = " , ( mag['z'] ))
    print()
```