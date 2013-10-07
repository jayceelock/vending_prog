import subprocess

def process_card():
    
    process = subprocess.Popen('nfc-poll', stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    
    out, err = process.communicate()
    
    out = out.split('\n')
    
    uid_line = out[5]
    
    uid = uid_line.split(':')[1]
    
    return uid