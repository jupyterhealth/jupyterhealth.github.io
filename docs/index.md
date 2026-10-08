---
title: JupyterHealth
site:
  hide_outline: true
---

**Open infrastructure for health care.**
JupyterHealth is a secure, connective layer for bringing wearable, clinical, and {term}`patient-generated data` into modern computational and AI-enabled health care workflows.
It is open source, built on open standards like {term}`FHIR` and {term}`Open mHealth`, and made for researchers, clinicians, and patients.
Its two main pieces are the {term}`Exchange`, which stores {term}`patient-consented data`, and the {term}`Hub`, where people analyze that data and build {term}`data products <data product>` for clinicians and patients.

Here's a diagram of the major workflow we want to enable.[^1]

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
Read [What is JupyterHealth?](about.md) for how the pieces fit together.

:::{note} JupyterHealth is under active development
These pages describe what the project is building toward. Some pieces are further along than others.
:::

## Get access

To try JupyterHealth, [sign up for the demo Exchange](xref:hub/sign-up) and then [log in to the demo Hub](xref:hub/log-in).
The demo Exchange and Hub are hosted at UC Berkeley.
Other institutions may set up access differently, for example by connecting their own Exchange to an existing computing environment instead of a Hub.

## What do you want to do?

::::{grid} 1 1 2 2

:::{card} Analyze data and build dashboards on the Hub
:link: https://docs.jupyterhealth.org/hub/
Log in to the {term}`Hub` with your {term}`Exchange` account, pull data into a notebook with the client library, and run your own analyses.
:::

:::{card} Write Python that uses data from the Exchange
:link: https://jupyterhealth-client.readthedocs.io
The {term}`client library` returns observations as pandas DataFrames.
The [{term}`CGM` tutorial](xref:jhe/tutorial/tutorial-cgm) is an end-to-end example.
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
