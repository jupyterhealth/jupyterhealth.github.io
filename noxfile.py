import shutil

import nox

nox.options.default_venv_backend = "uv"
nox.options.reuse_existing_virtualenvs = True


@nox.session
def docs(session):
    """Build the documentation."""
    session.install("mystmd")
    session.chdir("docs")
    session.run("myst", "build", "--html", *session.posargs)
    # Temporary: replace MyST's robots.txt to keep the site out of search engines.
    shutil.copy("robots.txt", "_build/html/robots.txt")


@nox.session(name="docs:live")
def docs_live(session):
    """Serve the documentation with live reload."""
    session.install("mystmd")
    session.chdir("docs")
    session.run("myst", "start", *session.posargs)
