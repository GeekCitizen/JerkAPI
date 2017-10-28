import socket, sys, os

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    # Connect to Backend, sent URI and collect result
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 8080))
    conn.sendall(environ['REQUEST_METHOD'] + "|" + environ['REQUEST_URI'])
    answer = conn.recv(4096)

    return answer
