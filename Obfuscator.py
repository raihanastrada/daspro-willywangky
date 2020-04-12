import base64

def obs(password):
    sct = base64.standard_b64encode(password.encode('utf-8'))
    sctb = sct.decode('ascii')
    return sctb

def deobs(code):
    rvl = base64.standard_b64decode(code.encode('utf-8'))
    srvl = rvl.decode('ascii')
    return srvl