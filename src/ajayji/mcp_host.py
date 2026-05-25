import asyncio
import threading
import uvicorn
from mcp.server.fastmcp import FastMCP

class JupyterMCPHost:
    """
    A helper class to run a FastMCP SSE Server in a background thread
    within a Jupyter Notebook. This allows the Ajayji Dart Daemon to
    connect to this Notebook and execute registered Python functions.
    """
    
    def __init__(self, name: str = "JupyterHost", host: str = "127.0.0.1", port: int = 0):
        if port == 0:
            import socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, 0))
                port = s.getsockname()[1]
                
        self.mcp = FastMCP(name, host=host, port=port)
        self.host = host
        self.port = port
        self._thread = None
        self._stop_event = threading.Event()
        
    @property
    def sse_uri(self) -> str:
        """Returns the full URI for the Server-Sent Events endpoint."""
        return f"http://{self.host}:{self.port}/sse"

    def tool(self, name=None, description=None):
        """Decorator to register a function as an MCP tool."""
        return self.mcp.tool(name=name, description=description)

    def start(self):
        """Starts the SSE Server in a background thread."""
        if self._thread and self._thread.is_alive():
            print(f"MCP Server is already running on http://{self.host}:{self.port}/sse")
            return

        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_server, daemon=True)
        self._thread.start()
        print(f"✅ FastMCP Server started in background. SSE URL: http://{self.host}:{self.port}/sse")

    def stop(self):
        """Stops the background SSE Server."""
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout=2)
            print("🛑 FastMCP Server stopped.")

    def _run_server(self):
        try:
            print(f"🐍 [Jupyter] Starting FastMCP server on port {self.port}...")
            # Run using SSE transport, relying on the host/port set during initialization
            self.mcp.run(transport='sse')
        except Exception as e:
            if not self._stop_event.is_set():
                 print(f"🐍 [Jupyter] MCP Server crashed: {e}")