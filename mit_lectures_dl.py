import os, sys
n = 1
style = sys.argv[2]
prepend = "https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec"
prepend = sys.argv[1]
append = ".pdf"

while True:
    ns = str(n)
    if n < 10:
        if style == 0:
            ns = '0' + str(n)
    
    url  = prepend + ns + append
        
    s = os.system(f" wget {url}")
    if s == 2048: break
    n += 1
