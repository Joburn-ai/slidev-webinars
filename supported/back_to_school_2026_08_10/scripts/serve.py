#!/usr/bin/env python3
"""Static server with SPA fallback, for QC screenshots of the built deck.

    python3 scripts/serve.py dist [port]

A plain `python3 -m http.server` 404s on every deep route (/14, /50, ...) because
Slidev's build is a history-mode SPA. That 404 renders as a white "Error response"
page, and a screenshot of it looks like a broken slide rather than a broken server.
"""
import http.server
import os
import socketserver
import sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else 'dist')
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8899
os.chdir(ROOT)


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path) and '.' not in os.path.basename(self.path):
            self.path = '/index.html'
        return super().do_GET()

    def log_message(self, *args):
        pass


socketserver.TCPServer.allow_reuse_address = True
print(f'serving {ROOT} on :{PORT}', flush=True)
socketserver.TCPServer(('', PORT), Handler).serve_forever()
