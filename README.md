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

## Shared navbar, footer, and plugins

This is a MyST site, and provides [shared MyST configuration](https://mystmd.org/guide/configuration#composing-myst-yml) that other documentation sites can use.
Find those in: `docs/_site/site.yml`.
It sets the theme, logo, navbar, footer, and shared plugins.

To reuse that configuration in another MyST site, add this to its `myst.yml`:

```yaml
extends:
  - https://raw.githubusercontent.com/jupyterhealth/jupyterhealth-docs/main/docs/_site/site.yml
```

Plugins listed there are merged with the site's own `project.plugins`.

If the site defines its own `site.parts`, it replaces the shared parts (navbar icons and footer), so copy the ones you want to keep from `docs/_site/site.yml`.
