#!/usr/bin/env python3

from __future__ import annotations

import json
import pathlib
import sys
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "public-surface.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    require(config["canonicalStatement"] in readme, "Missing canonical statement in README.md")
    require("docs-only service-surface repository" in readme, "README.md must classify the repo as docs-only")
    require("does not\npublish the deployed frontend source" in readme, "README.md must state that frontend source is unpublished")
    require(CONFIG_PATH.name in readme, "README.md must reference public-surface.json")

    with urllib.request.urlopen(config["explorer"]["validatorFeed"]["url"], timeout=20) as response:
        payload = json.load(response)

    for key in config["explorer"]["validatorFeed"]["requiredKeys"]:
        require(key in payload, f"Live validator feed missing key: {key}")

    validators = payload.get("validators", [])
    forbidden = set(config["explorer"]["validatorFeed"]["forbiddenPlaceholderIds"])
    for validator in validators:
        address = validator.get("address")
        require(address not in forbidden, f"Live validator feed still includes placeholder ID: {address}")

    with urllib.request.urlopen(config["explorer"]["capabilitiesUrl"], timeout=20) as response:
        capabilities = json.load(response)

    require(
        capabilities.get("canonicalStatement") == config["canonicalStatement"],
        "Live capabilities statement drifted from explorer manifest",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())