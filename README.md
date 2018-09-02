# Local_Python_HTTPServer_Application

This application hosts a simple HTTP Server in Python2.7. You don't need to have Python installed for this as it is built on side of a Python2.7 virtual environment. Just download the package and follow 2 simple steps :

1. On Unix or MacOS, run:
   ~ source path_to_application/Local_Python_HTTPServer_Application/venv/bin/activate
   
   On Windows, run:
   ~ path_to_application\Local_Python_HTTPServer_Application\Scripts\activate.bat

2. Now you are on a virtual environment. Now you can run the application using:
   ~ python path_to_application/Local_Python_HTTPServer_Application/Server.py
   
   Your server is running...
   
   
   
   
Or if you want to build a server on top of it you may just use the script Server.py. Dependencies include :
   a) json
   b) urlparse
   c) BaseHTTPServer

   All of these dependencies can be easily installed using pip or easy-install. After resolving dependencies you can run the script on you terminal using:
   ~ python path_to_application/Local_Python_HTTPServer_Application/Server.py
