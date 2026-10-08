---
title: JupyterHealth
site:
  hide_outline: true
---

**Open infrastructure for health care.**
JupyterHealth connects wearable, clinical, and {term}`patient-generated data` to computational and AI tools for health care.
It is open source, built on {term}`Jupyter` and open standards like {term}`FHIR` and {term}`Open mHealth`, and made for researchers, clinicians, and patients.
Its two main pieces are the {term}`Exchange`, which stores {term}`patient-consented data`, and the {term}`Hub`, where people analyze that data and build {term}`data products <data product>` for clinicians and patients.

Here's the workflow it supports.

```{mermaid}
flowchart LR
  collect["<b>1. Collect</b><br>Patients share data from devices, apps, and health records"]
  manage["<b>2. Manage</b><br>The Exchange stores it and controls who can see it"]
  analyze["<b>3. Analyze</b><br>Researchers explore it and build dashboards on the Hub"]
  share["<b>4. Share</b><br>Clinicians and patients open those dashboards"]
  collect --> manage --> analyze --> share
  %% Translucent fills so the diagram works in light and dark mode
  classDef jh fill:#f0702c1a,stroke:#f0702c
  classDef neutral fill:#8881,stroke:#888
  class manage,analyze jh
  class collect,share neutral
```

:::{note} JupyterHealth is under active development
These pages describe what the project is building toward.
Some pieces are further along than others.
:::

## What do you want to do?

Each page covers one step of the workflow.

::::{grid} 1 1 2 2

:::{card} 1. Collect patient data
:link: collect.md
Set up a study in the {term}`Exchange`, invite patients, and bring in data from their devices and health records.
:::

:::{card} 2. Manage access to data
:link: manage.md
Run your own Exchange, and decide who can see which data and which tools can connect to it.
:::

:::{card} 3. Analyze data and build data products
:link: analyze.md
Explore Exchange data on the {term}`Hub` or in your own Python environment, and turn it into dashboards.
:::

:::{card} 4. Share data products with clinicians and patients
:link: share.md
Put a dashboard on the Hub, or in front of clinicians in their {term}`EHR` with {term}`SMART on FHIR`.
:::

::::

## Try the demo

To try JupyterHealth, [sign up for the demo Exchange](xref:hub/sign-up) and then [log in to the demo Hub](xref:hub/log-in).
The demo Exchange and Hub are hosted at UC Berkeley.

To learn who uses JupyterHealth, see the [use cases](https://jupyterhealth.org/use-cases), or [contact the team](https://jupyterhealth.org/#contact) about running it at your organization.
