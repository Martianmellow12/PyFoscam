<html>

  <h1>PyFoscam</h1>
  <p>A Python library for interfacing with and controlling Foscam cameras</p>
  <br>
  <h2>Introduction</h2>
  <p>The PyFoscam library is made to make communicating with and controlling Foscam cameras easier.</p>
  <br>
  <h2>Usage</h2>
  <p>PyFoscam's goal is to be easy-to-use, which is reflected in how little code it takes to get up and running.</p>
  ```python
  import time
  
  # Connect to the camera
  mycam = pyfoscam.Foscam('192.168.0.xxx', 80, 'admin', '')
  # Move the camera left, then stop it after 2 seconds
  mycam.moveLeft()
  time.sleep(2)
  mycam.moveStop()
  ```
  
  <h2>License</h2>
  <p>Copyright © 2016 Michael Kersting Jr
  <br>
  Released under a <a href="https://github.com/Martianmellow12/PyFoscam/blob/master/LICENSE.md">modified version of the MIT License</a></p>
  
</html>
