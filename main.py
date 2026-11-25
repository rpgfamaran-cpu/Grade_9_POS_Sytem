import importlib.util
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_module(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {file_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    developer_a = load_module(
        "developer_a",
        BASE_DIR / "dev a" / "feature-menu.py",
    )
    developer_b = load_module(
        "developer_b",
        BASE_DIR / "Dev-B" / "Ord sytem.py",
    )

    print("Welcome to the Ordering System")
    orders = developer_a.take_orders()
    developer_b.display_receipt(orders)


if __name__ == "__main__":
    main()
