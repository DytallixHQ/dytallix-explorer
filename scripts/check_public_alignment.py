#!/usr/bin/env python3

from __future__ import annotations

import json
import pathlib
import ssl
import sys
import urllib.request

try:
    import certifi
except ImportError:  # pragma: no cover - best effort local TLS fix
    certifi = None


ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "public-surface.json"


def open_json(url: str) -> dict:
    context = None
    if certifi is not None:
        context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(url, timeout=20, context=context) as response:
        return json.load(response)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    require(config["canonicalStatement"] in readme, "Missing canonical statement in README.md")
    require("docs-only service-surface repository" in readme, "README.md must classify the repo as docs-only")
    require("`dytallix-website` repository" in readme, "README.md must point to dytallix-website as the canonical frontend source repo")
    require("src/pages/build/blockchain.tsx" in readme, "README.md must point to the explorer source path in dytallix-website")
    require(CONFIG_PATH.name in readme, "README.md must reference public-surface.json")

    payload = open_json(config["explorer"]["validatorFeed"]["url"])

    for key in config["explorer"]["validatorFeed"]["requiredKeys"]:
        require(key in payload, f"Live validator feed missing key: {key}")

    validators = payload.get("validators", [])
    forbidden = set(config["explorer"]["validatorFeed"]["forbiddenPlaceholderIds"])
    for validator in validators:
        address = validator.get("address")
        require(address not in forbidden, f"Live validator feed still includes placeholder ID: {address}")

    capabilities = open_json(config["explorer"]["capabilitiesUrl"])

    require(
        capabilities.get("canonicalStatement") == config["canonicalStatement"],
        "Live capabilities statement drifted from explorer manifest",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())