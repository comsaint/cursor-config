#!/usr/bin/env python3
"""Replace ds-project template tokens in pyproject.toml after copy.

Call once from the new project root with your real top-level import name and
(optional) directory to put on PYTHONPATH for pytest.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

TOKEN_IMPORT = "__DS_PACKAGE_IMPORT__"
TOKEN_PYTHONPATH = "__DS_PYTHONPATH__"

TARGET_FILES = ("pyproject.toml",)


def _validate_identifiers(package: str, pythonpath_rel: str) -> None:
    if TOKEN_IMPORT in package or TOKEN_PYTHONPATH in pythonpath_rel:
        raise SystemExit("Refusing to use values that still contain template tokens.")
    if not package.strip():
        raise SystemExit("package must be non-empty.")
    if not pythonpath_rel.strip():
        raise SystemExit("pythonpath must be non-empty (use . for flat layout).")


def apply_config(root: Path, package: str, pythonpath_rel: str) -> None:
    """Write package import name and pythonpath into templated config files."""
    _validate_identifiers(package, pythonpath_rel)
    changed = False
    for name in TARGET_FILES:
        path = root / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if TOKEN_IMPORT not in text and TOKEN_PYTHONPATH not in text:
            continue
        new_text = text.replace(TOKEN_IMPORT, package).replace(
            TOKEN_PYTHONPATH, pythonpath_rel
        )
        path.write_text(new_text, encoding="utf-8")
        changed = True
    if not changed:
        print("No template tokens found; already configured or unexpected layout.")
        return
    print(f"Configured package import={package!r} pythonpath={pythonpath_rel!r} in {root}")


def main(argv: list[str] | None = None) -> int:
    """Parse CLI args and apply template substitution."""
    parser = argparse.ArgumentParser(
        description="Set ds-project first-party package name and pytest pythonpath."
    )
    parser.add_argument(
        "package",
        help="Top-level import name (e.g. my_ds_app), matching your package folder.",
    )
    parser.add_argument(
        "--pythonpath",
        default="src",
        help="Relative dir on PYTHONPATH for tests (default: src). Use . for flat layout.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Project root (default: directory containing this script).",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve() if args.root else Path(__file__).resolve().parent
    apply_config(root, args.package.strip(), args.pythonpath.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
