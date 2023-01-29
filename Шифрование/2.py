try:
    import os
    from elevate import elevate

    elevate()
except:
   from ctypes import windll
   import sys
   import psutil

   try:
       if windll.shell32.IsUserAnAdmin(): pass
       else:
           windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
   except: pass