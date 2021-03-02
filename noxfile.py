"""Nox sessions."""

import nox
from nox.sessions import Session


package = "artworks"
locations = "artworks", "tests", "noxfile.py", "docs/conf.py"


@nox.session(python="3.8")
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    session.run("flake8", *args, external=True)


@nox.session(python="3.8")
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    session.run("mypy", *args, external=True)


@nox.session(python="3.8")
def tests(session: Session) -> None:
    """Run the test suite."""
    args = session.posargs or ["--cov", "artworks"]
    session.run("pytest", *args, external=True)


@nox.session(python="3.8")
def docs(session: Session) -> None:
    """Build the documentation."""
    session.run("sphinx-build", "docs", "docs/_build", "-E", "-a", external=True)
