from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/index.html"):
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("404 - Pagina no encontrada".encode("utf-8"))
            return

        html = """<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hola Mundo DevOps</title>
    <style>
      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        font-family: Arial, sans-serif;
        background: #f4f7fb;
        color: #172033;
      }

      main {
        text-align: center;
        padding: 32px;
      }

      h1 {
        font-size: 48px;
        margin: 0 0 12px;
      }

      p {
        font-size: 20px;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <main>
      <h1>Hola Mundo</h1>
      <p>Aplicacion web ejecutandose en Docker.</p>
    </main>
  </body>
</html>
"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


def main():
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), HelloWorldHandler)
    print(f"Servidor iniciado en http://0.0.0.0:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
