import nox

nox.options.default_venv_backend = "uv"
nox.options.reuse_existing_virtualenvs = True


@nox.session
def docs(session):
    """Build the documentation."""
    session.install("mystmd")
    session.chdir("docs")
    session.run("myst", "build", "--html", *session.posargs)


@nox.session(name="docs:live")
def docs_live(session):
    """Serve the documentation with live reload."""
    session.install("mystmd")
    session.chdir("docs")
    session.run("myst", "start", *session.posargs)
