# JupyterHealth Documentation

The project-wide docs for JupyterHealth.
For example: what the project is, how the pieces fit together, and where to find each component's docs.
[jupyterhealth.org](https://jupyterhealth.org) is the project's public website.
This site has more reference information and is more complete in general.

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
It sets the theme, logo, navbar, footer, and shared plugins.

To reuse that configuration in another MyST site, add this to its `myst.yml`:

```yaml
extends:
  - https://raw.githubusercontent.com/jupyterhealth/jupyterhealth.github.io/main/docs/_site/site.yml
```

Plugins listed there are merged with the site's own `project.plugins`.

If the site defines its own `site.parts`, it replaces the shared parts (navbar icons and footer), so copy the ones you want to keep from `docs/_site/site.yml`.
