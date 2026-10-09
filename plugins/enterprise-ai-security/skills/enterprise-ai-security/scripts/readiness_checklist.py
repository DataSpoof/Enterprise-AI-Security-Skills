#!/usr/bin/env python3
"""Emit a blank CSV or JSON tracker for the baseline's 23 readiness items."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


ITEMS = [
    ("Identity and access", "SSO/MFA and backend authorization"),
    ("Identity and access", "Least-privilege model and agent identities"),
    ("Identity and access", "Tenant and document-level access control"),
    ("Identity and access", "Credential rotation and revocation"),
    ("Data and RAG", "Data classification and sensitive-data protection"),
    ("Data and RAG", "Secure ingestion and isolated document parsing"),
    ("Data and RAG", "Trusted metadata and retrieval authorization"),
    ("Data and RAG", "Embedding, cache and memory isolation"),
    ("Data and RAG", "Deletion propagation and citation verification"),
    ("LLM and agent security", "Prompt-injection and jailbreak evaluations"),
    ("LLM and agent security", "Output validation and safe rendering"),
    ("LLM and agent security", "Tool allowlists and argument validation"),
    ("LLM and agent security", "Independent approval for high-impact actions"),
    ("LLM and agent security", "Agent budgets, isolation and emergency stop"),
    ("Infrastructure and supply chain", "Network segmentation and egress controls"),
    ("Infrastructure and supply chain", "Secure containers and cloud IAM"),
    ("Infrastructure and supply chain", "Model, package and dataset provenance"),
    ("Infrastructure and supply chain", "CI/CD security and controlled model updates"),
    ("Monitoring and governance", "Correlated audit logs and privacy controls"),
    ("Monitoring and governance", "AI incident response and recovery tests"),
    ("Monitoring and governance", "Automated adversarial security testing"),
    ("Monitoring and governance", "Risk ownership and framework mapping"),
    ("Monitoring and governance", "Continuous remediation and regression testing"),
]

FIELDS = ["number", "domain", "control", "status", "evidence", "owner", "target_maturity"]


def rows() -> list[dict[str, str | int]]:
    return [
        {
            "number": number,
            "domain": domain,
            "control": control,
            "status": "unknown",
            "evidence": "",
            "owner": "",
            "target_maturity": "",
        }
        for number, (domain, control) in enumerate(ITEMS, start=1)
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("csv", "json"), default="csv")
    parser.add_argument("--output", type=Path, help="Write to this path instead of stdout")
    args = parser.parse_args()

    if args.format == "json":
        output = json.dumps(rows(), indent=2, ensure_ascii=False) + "\n"
    else:
        from io import StringIO

        buffer = StringIO(newline="")
        writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows())
        output = buffer.getvalue()

    if args.output:
        args.output.write_text(output, encoding="utf-8", newline="")
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
