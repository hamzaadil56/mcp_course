from jsonrpcserver import method, serve, Success


@method
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@method
def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return Success(a - b)


@method
def greet(name: str) -> str:
    """Greet a person by name."""
    return Success(f"Hello, {name}!")


if __name__ == "__main__":
    print("Starting JSON-RPC server on localhost:5001...")
    serve(name="localhost", port=5001)
