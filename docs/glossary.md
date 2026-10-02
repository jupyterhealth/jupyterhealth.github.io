# Glossary

Terms used across the JupyterHealth documentation.

:::{glossary}
platform
: The JupyterHealth platform. The collection of tools that JupyterHealth builds to work together, mainly the {term}`Exchange` and the {term}`Hub`. See [What is JupyterHealth?](about.md).

deployment
: A running service that someone hosts with JupyterHealth tools, such as the demo deployment at UC Berkeley.

distribution
: A collection of choices bundled with a JupyterHub (configuration, software, and services) that provide an integrated end-user experience. The {term}`Hub` is a JupyterHub distribution.

data product
: Something a data scientist creates from health data to share with clinicians or patients, like a dashboard, app, or report. Often built in a notebook and shared with a tool like Voilà or Jupyter Book.

Exchange
: The JupyterHealth Exchange (JHE). A back-end web service that stores patient-consented health data and serves it through REST, {term}`FHIR`, and MCP APIs. Researchers create studies, patients consent and contribute data, and analysts can query it with the {term}`client library`. See the [Exchange documentation](https://jupyterhealth.github.io/software-documentation/).

Hub
: The JupyterHealth Hub. An opinionated [JupyterHub](https://jupyter.org/hub) {term}`distribution` that is set up alongside an {term}`Exchange`. It uses the Exchange for login and has the {term}`client library` pre-installed. Researchers and data scientists use it to explore data and build {term}`data products <data product>` for clinicians and patients. Its [configuration is public](https://github.com/2i2c-org/infrastructure/tree/main/config/clusters/jupyter-health) so anybody can copy it and reconfigure it for themselves.

client library
: `jupyterhealth-client`, a Python package for reading data from the Exchange. Returns observations as pandas DataFrames. See the [exchange client documentation](https://jupyterhealth-client.readthedocs.io).

FHIR
: Fast Healthcare Interoperability Resources. The HL7 standard for exchanging clinical data over a web API. The Exchange stores data as FHIR, so clinical data from an EHR and wearable data use the same format. [hl7.org/fhir](https://hl7.org/fhir/).

SMART on FHIR
: A standard that lets an EHR open an outside app with a patient already selected and give it limited FHIR access. JupyterHealth uses it to open apps, on the {term}`Hub` or standalone, from clinical systems. [smarthealthit.org](https://smarthealthit.org).

Open mHealth
: An open schema standard for mobile and wearable health data such as heart rate, steps, and glucose. JupyterHealth stores wearable data in Open mHealth and {term}`IEEE 1752` formats. [openmhealth.org](https://www.openmhealth.org).

IEEE 1752
: The IEEE standard for mobile health data, derived from {term}`Open mHealth`. [standards.ieee.org](https://standards.ieee.org/ieee/1752.1/6982/).

patient-generated data
: Health data that patients collect themselves, outside a clinic, from wearables, sensors, mobile apps, and surveys. JupyterHealth brings it together with clinical data from an EHR.

patient-consented data
: Data that a patient has explicitly agreed to share with a specific study or organization. The Exchange enforces consent when serving data.

EHR
: Electronic health record. The clinical system a hospital or clinic uses to store patient charts, such as Epic or Cerner.

CGM
: Continuous glucose monitor. A wearable sensor that records blood glucose every few minutes. The {term}`Exchange` docs include a [CGM tutorial](https://jupyterhealth.github.io/software-documentation/tutorial/tutorial-cgm).

MCP
: Model Context Protocol. An open protocol that lets AI assistants call tools and read data. The {term}`Exchange` exposes an MCP server so AI tools can query health data.

Zulip
: The [#jupyterhealth channel on the Jupyter Zulip](https://jupyter.zulipchat.com/#narrow/channel/531270-jupyterhealth) is a place for general discussion with the project's community and team.

Team Compass
: The [JupyterHealth Team Compass](https://github.com/jupyterhealth/team-compass) is the source of truth for overall project goals, direction, and ways of working.
:::
