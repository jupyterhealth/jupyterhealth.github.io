---
title: JupyterHealth
site:
  hide_outline: true
---

**Open infrastructure for health care.**
JupyterHealth is a secure, connective layer for bringing wearable, clinical, and {term}`patient-generated data` into modern computational and AI-enabled health care workflows.
It is open source, built on open standards like {term}`FHIR` and {term}`Open mHealth`, and made for researchers, clinicians, and patients.
It has three main pieces:

- The {term}`Exchange` stores {term}`patient-consented data` and serves it through REST, FHIR, and {term}`MCP` APIs.
- The {term}`Hub` is where researchers and data scientists analyze that data, and the platform for building and deploying dashboards and apps for clinicians and other downstream users.
- The {term}`client library` reads Exchange data from Python for analysis and re-use.

## Try JupyterHealth: Berkeley demo

You can try JupyterHealth using the Berkeley demo {term}`Exchange` and {term}`Hub`. The Exchange contains sample data that you can explore in a notebook on the Hub. You'll need an invite code to create an account. If you weren't given one, ask in the {term}`#jupyterhealth Zulip channel <Zulip>`.

**Getting started takes two steps:**

1. Create an account on the [Berkeley demo Exchange](https://berkeley-jhe-demo.jupyterhealth.org/) using your invite code.
2. Open the [Berkeley demo Hub](https://jupyter-health.2i2c.cloud/) to use JupyterLab, where you can create notebooks and use the AI chat interface.

From there, follow the [Explore your data guide](https://docs.jupyterhealth.org/hub/run-an-analysis/) to start with a blank notebook or [open the CGM example notebook](https://jupyter-health.2i2c.cloud/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fjupyterhealth%2Fdemos&urlpath=lab%2Ftree%2Fdemos%2Fdashboards%2Fresearcher-view-cgm.ipynb&branch=main) to add it to your Hub workspace.

These instructions and links are specific to the Berkeley demo. If you’re using JupyterHealth through another institution, it may have its own Exchange and Hub, or connect its to Exchange using a different computational environment. Use the URLs and access instructions provided by your institution.

## How JupyterHealth works

The diagram shows the broader workflow that JupyterHealth aims to support.[^1]

[^1]: Adapted from the [JupyterHealth integration page](https://jupyterhealth.org/#integration).


```{mermaid}
flowchart BT
  sources["<b>DATA SOURCES</b><br>EHRs · devices · sensors · apps · surveys"]
  subgraph platform["<b>JupyterHealth Platform</b>"]
    direction BT
    exchange["<b>EXCHANGE</b><br>Ingestion · Standardization · Storage"]
    hub["<b>HUB</b><br>JupyterAI · Notebooks · Dashboards · APIs"]
    exchange ~~~ hub
  end
  subgraph outputs[" "]
    discovery["Discovery"]
    decision["Decision support"]
    care["Remote care"]
  end
  sources --> platform --> outputs
  %% Translucent fills so the diagram works in light and dark mode
  classDef jh fill:#f0702c1a,stroke:#f0702c
  classDef neutral fill:#8881,stroke:#888
  class platform,hub,exchange jh
  class sources,discovery,decision,care neutral
  style outputs fill:none,stroke:none
```

This site describes the project at a high level and points to each component's documentation.
Read [About the project](about.md) for its origins and primary materials.

:::{note} JupyterHealth is under active development
These pages describe what the project is building toward. Some pieces are further along than others.
:::

## What do you want to do?

::::{grid} 1 1 2 2

:::{card} Analyze data and build dashboards on the Hub
:link: https://docs.jupyterhealth.org/hub/
Log in to the {term}`Hub` with your {term}`Exchange` account, pull data into a notebook with the client library, and run your own analyses.
:::

:::{card} Write Python that uses data from the Exchange
:link: https://jupyterhealth-client.readthedocs.io
The {term}`client library` returns observations as pandas DataFrames.
The [{term}`CGM` tutorial](https://docs.jupyterhealth.org/software-documentation/tutorial/tutorial-cgm) is an end-to-end example.
:::

:::{card} Run the Exchange for your organization
:link: https://docs.jupyterhealth.org/software-documentation/
Deploy your own {term}`Exchange`.
The docs cover setup, access control, the FHIR API, and the data model.
:::

:::{card} Deploy an app that uses the Exchange
:link: https://github.com/jupyterhealth/jupyterhealth-sof-provider-template
The linked repository lets you turn a notebook into a Voilà application. It can be served either on the {term}`Hub` or as a standalone app that an {term}`EHR` opens with {term}`SMART on FHIR`.
:::

::::
