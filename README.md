# The JupyterHealth website

**note: currently built at https://jupyterhealth.github.io/ not https://jupyterhealth.org**

This is a [Hugo](https://gohugo.io) website hosted on GitHub pages.
The public site

## Building and testing locally

You can run a local build by [installing Hugo](https://gohugo.io/installation/).

The [Hugo quickstart is helpful](https://gohugo.io/getting-started/quick-start/).

If you are editing the site, you can run:

```
hugo server
```

and visit http://localhost:1313 to see a test build of the site.
Hugo will rebuild on any detected change, so you can have your editor and browser open without going back to the terminal.

Or you can run a single build:

```
hugo build
```

The result will be in `./public`, which you can test with:

```
python3 -m http.server -b 127.0.0.1 -d ./public
```

and visiting http://127.0.0.1:8000
