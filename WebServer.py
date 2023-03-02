import socket
import gc
import os
gc.collect()


def file_or_dir_exists(filename):
    try:
        os.stat(filename)
        return True
    except OSError:
        return False

def getType(name):
    if name.endswith("/"):
        name="/index.html"
    tipo = "text/plain" 
    if name.endswith("html"):
        tipo = "text/html"
    if name.endswith("js"):
        tipo = "application/javascript"
    if name.endswith("css"):
        tipo = "text/css"
    return tipo
        
def SendFile(conn, name):
    if name.endswith("/"):
        name="/index.html"
    
    #f = open("web" + name)
    #data = f.read()
    #f.close() 
    with open("web" + name,'rb') as infile:
        while True:
            result = infile.read(128)
            if result == b'':
                break
            conn.sendall(result)


def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        indice_get  = request.index("GET ")
        indice_http = request.index(" HTTP")
        file = request[indice_get+4:indice_http]
        print('Content = %s' % request)
        print('File = %s' % file)
        print('File =' + str(file_or_dir_exists("web" + file)))
        if file_or_dir_exists("web" + file):
            conn.send('HTTP/1.1 200 OK\n')
            tipo = getType(file)
            conn.send('Content-Type: ' +tipo+ '\n')
            conn.send('Connection: close\n\n')
            SendFile(conn,file)
        else:
            conn.send('HTTP/1.1 404 Not Found\n')
            conn.send('Content-Type: text/plain\n')
            conn.send('Connection: close\n\n')
            conn.send("Sin datos!")
        conn.close()