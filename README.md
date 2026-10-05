# JupyterHealth Documentation

The landing site for the JupyterHealth documentation and broader ecosystem.
This describes what the project is, and where to find the docs for each piece.

This is a complement to https://jupyterhealth.org, which serves more as a _brochure site_.
This site is more of a definitive project-wide documentation.

## Preview the site locally

Preview locally with [nox](https://nox.thea.codes):

```bash
nox -s docs:live
```

## How the site is published

Our documentation is built and published via a GitHub workflow that runs `nox -s docs`.

This repository is the org's GitHub Pages site, so it is served at https://docs.jupyterhealth.org.
Every other repository that's served by GitHub Pages will exist at:

```
docs.jupyterhealth.org/[reponame]
```

For example, the docs at [`/hub`](https://github.com/jupyterhealth/hub) are served at https://docs.jupyterhealth.org/hub.

## Shared navbar, footer, and plugins

This is a MyST site, and provides [shared MyST configuration](https://mystmd.org/guide/configuration#composing-myst-yml) that other documentation sites can use.
Find those in: `docs/_site/site.yml`.
It sets the theme, logo, navbar, footer, and a few plugins (footer, iconify, listing, gui-text).

To reuse that configuration in another MyST site, add this to its `myst.yml`:

```yaml
extends:
  - https://raw.githubusercontent.com/jupyterhealth/jupyterhealth.github.io/main/docs/_site/site.yml
```

Plugins listed there are merged with the site's own `project.plugins`.

If the site defines its own `site.parts`, it replaces the shared parts (navbar icons and footer), so copy the ones you want to keep from `docs/_site/site.yml`.
