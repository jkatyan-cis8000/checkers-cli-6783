#!/usr/bin/env python3
"""Lint script to enforce layer architecture and file constraints."""

import ast
import os
import sys
from pathlib import Path


# Layer order defines the dependency direction
LAYERS = ["model", "config", "repo", "service", "runtime", "ui", "providers", "utils"]

# Allowed imports per layer
ALLOWED_IMPORTS = {
    "model": ["model"],
    "config": ["model", "config"],
    "repo": ["model", "config", "repo"],
    "service": ["model", "config", "repo", "providers", "service"],
    "runtime": ["model", "config", "repo", "service", "providers", "runtime"],
    "ui": ["model", "config", "service", "runtime", "providers", "ui"],
    "providers": ["model", "config", "utils", "providers"],
    "utils": ["utils"],
}

MAX_LINES = 300


def get_layer(file_path: Path) -> str | None:
    """Get the layer directory containing this file."""
    src_dir = Path("src")
    try:
        rel_path = file_path.relative_to(src_dir)
        parts = rel_path.parts
        if parts:
            return parts[0]
    except ValueError:
        pass
    return None


def get_imports(file_path: Path) -> list[str]:
    """Extract import statements from a Python file."""
    imports = []
    try:
        with open(file_path, "r") as f:
            tree = ast.parse(f.read(), filename=str(file_path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module.split(".")[0])
    except SyntaxError:
        pass
    return imports


def check_file_lines(file_path: Path) -> list[str]:
    """Check if file exceeds line limit."""
    errors = []
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
        if len(lines) > MAX_LINES:
            errors.append(
                f"{file_path}:{len(lines)}: File exceeds {MAX_LINES} lines ({len(lines)} lines)"
            )
    except Exception:
        pass
    return errors


def check_imports(file_path: Path, layer: str) -> list[str]:
    """Check if imports respect layer dependencies."""
    errors = []
    allowed = ALLOWED_IMPORTS.get(layer, [])
    imports = get_imports(file_path)

    for imp in imports:
        # Handle relative imports (starting with ..)
        if imp.startswith(".."):
            # Relative imports are allowed; extract the target layer
            # e.g., "..model" -> "model", "..config" -> "config"
            parts = imp.split(".")
            if len(parts) > 2:
                # e.g., "..service.moves" -> target layer is "service"
                imported_layer = parts[-2] if len(parts) > 2 else parts[-1]
                if imported_layer not in allowed:
                    errors.append(
                        f"{file_path}:1: Import '{imp}' not allowed. Layer '{layer}' may only import from: {', '.join(allowed)}"
                    )
            continue
        
        # Check if this is an internal import (starts with src.)
        if imp.startswith("src."):
            # Extract the actual layer from the import
            parts = imp.split(".")
            if len(parts) > 1:
                imported_layer = parts[1]
                if imported_layer not in allowed:
                    errors.append(
                        f"{file_path}:1: Import '{imp}' not allowed. Layer '{layer}' may only import from: {', '.join(allowed)}"
                    )
        elif imp == "src":
            # Handle 'import src' - check what comes after
            errors.append(
                f"{file_path}:1: Import 'src' is not allowed. Use direct layer imports."
            )

    return errors


def check_layer_membership(file_path: Path) -> list[str]:
    """Check if file is inside a layer directory."""
    errors = []
    try:
        rel_path = file_path.relative_to(Path("src"))
        parts = rel_path.parts
        # First part after src/ should be a valid layer
        if parts and parts[0] not in LAYERS:
            errors.append(
                f"{file_path}:1: File is not inside a valid layer directory. Expected one of: {', '.join(LAYERS)}"
            )
    except ValueError:
        errors.append(f"{file_path}:1: File is not under src/ directory")

    return errors


def lint() -> int:
    """Run all lint checks. Returns 0 on success, 1 on failure."""
    errors = []
    src_dir = Path("src")

    if not src_dir.exists():
        print("Error: src/ directory not found")
        return 1

    # Find all Python files
    for root, _, files in os.walk(src_dir):
        for filename in files:
            if not filename.endswith(".py"):
                continue

            file_path = Path(root) / filename

            # Check layer membership
            layer = get_layer(file_path)
            if layer is None:
                continue

            # Check file size
            errors.extend(check_file_lines(file_path))

            # Check imports
            errors.extend(check_imports(file_path, layer))

            # Check layer membership (already checked above, but for completeness)
            errors.extend(check_layer_membership(file_path))

    if errors:
        print("Lint errors found:")
        for err in errors:
            print(err)
        return 1

    print("All checks passed!")
    return 0


if __name__ == "__main__":
    sys.exit(lint())
