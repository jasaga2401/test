#!/usr/bin/env python3
"""
A simple hello world application for demonstration purposes.
"""


def greet(name="World"):
    """
    Return a greeting message.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main():
    """Main entry point for the application."""
    print(greet())
    print(greet("Python"))


if __name__ == "__main__":
    main()
