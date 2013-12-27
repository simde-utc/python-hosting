Put here protected files: the webapp will be called before to serve these files.
In the webapp handler this is possible to perform checks and then return the header 
to tell the server (nginx, apache, etc...) which file to serve.
See X-Sendfile and X-Accel for more informations.

