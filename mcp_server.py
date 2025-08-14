"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource


@mcp.resource("config://settings")
def get_settings() -> str:
    """Get application settings."""
    return """{
  "theme": "dark",
  "language": "en",
  "debug": false
}"""


# Add a resource to read the README file
@mcp.resource("file://README.md")
def get_readme() -> str:
    """Read the README.md file from the repository."""
    import os
    try:
        readme_path = os.path.join(os.path.dirname(__file__), "README.md")
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content if content.strip() else "README.md file is empty"
    except FileNotFoundError:
        return "README.md file not found in the repository"
    except Exception as e:
        return f"Error reading README.md: {str(e)}"
