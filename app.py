"""A simple test application."""


def greet(name="World"):
    """
    Greet someone by name.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int/float): First number.
        b (int/float): Second number.
    
    Returns:
        int/float: The sum of a and b.
    """
    return a + b


def main():
    """Main function to demonstrate the application."""
    print(greet())
    print(greet("Python"))
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
