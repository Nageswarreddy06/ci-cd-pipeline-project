"""
Basic automated tests for the CI/CD pipeline project.
These run in the 'Test' stage of the pipeline. If any test fails,
the pipeline stops and the Docker image is never built or deployed.
"""

import os


def test_index_html_exists():
    """The web page that gets served must exist."""
    assert os.path.exists("index.html"), "index.html is missing"


def test_dockerfile_exists():
    """The Dockerfile used to containerize the app must exist."""
    assert os.path.exists("Dockerfile"), "Dockerfile is missing"


def test_index_html_not_empty():
    """The web page should actually have content."""
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert len(content.strip()) > 0, "index.html is empty"


def test_index_html_has_html_tag():
    """Basic sanity check that index.html is real HTML."""
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read().lower()
    assert "<html" in content or "<!doctype html" in content, \
        "index.html does not look like valid HTML"
