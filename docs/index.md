---
title: JupyterHealth
site:
  hide_outline: true
---

**Open infrastructure for health care.**
JupyterHealth is a project that connects wearable, clinical, and {term}`patient-generated data` to computational and AI tools for health care.
All of the tools it builds are open source, built on {term}`Jupyter` and open standards like {term}`FHIR` and {term}`Open mHealth`, and made for researchers, clinicians, and patients.

JupyterHealth's two main components are the {term}`Exchange`, which stores {term}`patient-consented data`, and the {term}`Hub`, where people analyze that data and build {term}`data products <data product>` for clinicians and patients.
Those data products can open inside an {term}`EHR` with {term}`SMART on FHIR`, so clinicians use them from a patient's chart.

**Thinking about what you could build with JupyterHealth tools, or whether it fits your organization?**
Start with the [use cases](https://jupyterhealth.org/use-cases) and [](about.md), or [talk to the team](https://jupyterhealth.org/#contact).

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

## Try the Berkeley demo

You can try JupyterHealth with the Berkeley demo {term}`Exchange` and {term}`Hub`.
The Exchange has sample data that you can explore in a notebook on the Hub.
You'll need an invite code to create an account.
To request one, ask in the [#jupyterhealth Zulip channel](https://jupyter.zulipchat.com/#narrow/channel/531270-jupyterhealth).

1. Create an account on the [Berkeley demo Exchange](https://berkeley-jhe-demo.jupyterhealth.org/) with your invite code.
2. Open the [Berkeley demo Hub](https://jupyter-health.2i2c.cloud/) to use JupyterLab, where you can create notebooks and use the AI chat interface.

To get started exploring some data, you can:

- [Add the blood pressure tutorial to your Hub workspace](https://jupyter-health.2i2c.cloud/hub/user-redirect/git-pull?branch=main&repo=https%3A%2F%2Fgithub.com%2Fjupyterhealth%2Fdemos&urlpath=lab%2Ftree%2Fdemos%2Ftutorials%2Fgetting-started-blood-pressure.ipynb).
- [Add the CGM tutorial to your Hub workspace](https://jupyter-health.2i2c.cloud/hub/user-redirect/git-pull?branch=main&repo=https%3A%2F%2Fgithub.com%2Fjupyterhealth%2Fdemos&urlpath=lab%2Ftree%2Fdemos%2Fdashboards%2Fresearcher-view-cgm.ipynb).
- Or follow [](xref:hub/run-an-analysis) to start with a blank notebook.

These links are specific to the Berkeley demo.
Other institutions may run their own Exchange and Hub, or connect their Exchange to a different computing environment.
If you use JupyterHealth through another institution, use the links and instructions it gives you.
