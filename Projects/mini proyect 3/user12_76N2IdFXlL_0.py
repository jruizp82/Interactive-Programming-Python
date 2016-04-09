# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import time

hora = (int(time.time())) // 3600
print hora        
        
dia = hora // 24
print dia

anyo = dia // 365
print anyo

print 2013 - anyo