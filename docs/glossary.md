# Glossary

Terms used across the JupyterHealth documentation.

:::{glossary}
Jupyter
: Project Jupyter.
  An open source project that builds tools and standards for interactive computing, like Jupyter notebooks, JupyterLab, Jupyter Book, and JupyterHub.
  JupyterHealth is a JupyterHub subproject, and the {term}`Hub` and data products like Voilà dashboards are built with Jupyter tools.
  [jupyter.org](https://jupyter.org).

platform
: The JupyterHealth platform.
  The collection of tools that JupyterHealth builds to work together, mainly the {term}`Exchange` and the {term}`Hub`.
  See [](about.md).

deployment
: A running service that someone hosts with JupyterHealth tools.
  A deployment might include an {term}`Exchange`, a {term}`Hub`, or both.
  The demo deployment at UC Berkeley has both.

distribution
: A JupyterHub bundled with configuration, software, and services, so it works as one product for its users.
  The {term}`Hub` is a JupyterHub distribution.

data product
: Something a data scientist creates from health data to share with clinicians or patients, like a dashboard, app, or report.
  Often built in a notebook and shared with a tool like Voilà or Jupyter Book.

Exchange
: The JupyterHealth Exchange (JHE).
  A back-end web service that stores patient-consented health data and serves it through APIs, including a {term}`FHIR` API.
  Researchers create studies, patients consent and contribute data, and analysts can query it with the {term}`client library`.
  See the [Exchange documentation](xref:jhe).

organization
: A group in the {term}`Exchange` that is used to manage access to data.
  Researchers, clinicians, patients, and studies belong to organizations.
  See [](xref:jhe/jhe/access-control).

Hub
: The JupyterHealth Hub.
  An opinionated [JupyterHub](https://jupyter.org/hub) {term}`distribution` that is set up alongside an {term}`Exchange`.
  The Hub uses the Exchange for login and has the {term}`client library` pre-installed.
  Researchers and data scientists use it to explore data and build {term}`data products <data product>` for clinicians and patients.
  Its [configuration is public](https://github.com/2i2c-org/infrastructure/tree/main/config/clusters/jupyter-health), so anybody can copy and adapt it.

client library
: `jupyterhealth-client`, a Python package for reading data from the Exchange.
  Returns observations as pandas DataFrames.
  See the [exchange client documentation](xref:client).

FHIR
: Fast Healthcare Interoperability Resources.
  The HL7 standard for exchanging clinical data over a web API.
  The Exchange serves its data through a FHIR API, so clinical data from an EHR and wearable data can be read the same way.
  [hl7.org/fhir](https://hl7.org/fhir/).

SMART on FHIR
: A standard that lets an outside app log in to an EHR or patient portal and read limited FHIR data.
  JupyterHealth uses it in two ways: clinicians open dashboards from their EHR, and patients bring in records from their hospital's patient portal.
  See [](share.md) and [smarthealthit.org](https://smarthealthit.org).

Open mHealth
: An open schema standard for mobile and wearable health data such as heart rate, steps, and glucose.
  JupyterHealth stores wearable data in Open mHealth and {term}`IEEE 1752` formats.
  [openmhealth.org](https://www.openmhealth.org).

IEEE 1752
: The IEEE standard for mobile health data, derived from {term}`Open mHealth`.
  [standards.ieee.org](https://standards.ieee.org/ieee/1752.1/6982/).

patient-generated data
: Health data that patients collect themselves, outside a clinic, from wearables, sensors, mobile apps, and surveys.
  JupyterHealth brings it together with clinical data from an EHR.

patient-consented data
: Data that a patient has explicitly agreed to share with a specific study.
  The Exchange only accepts the kinds of data from a patient that they have consented to share.
  See [](xref:jhe/jhe/access-control) for what consent does and doesn't control.

study
: A group of patients whose data an organization collects in the {term}`Exchange` for one purpose.
  Patients choose what to share with each study they join.
  See [](collect.md).

CommonHealth
: An Android app, built by the nonprofit [The Commons Project](https://www.thecommonsproject.org), that patients use to connect health devices and send their readings to the {term}`Exchange`.
  CommonHealth is a partner project, separate from JupyterHealth.
  [Google Play](https://play.google.com/store/apps/details?id=org.thecommonsproject.android.phr).

Open Wearables
: An open source, self-hosted platform that connects to wearable vendors like Oura and serves their data through one API.
  The {term}`Exchange` can pull data from an Open Wearables server.
  Open Wearables is a separate project from JupyterHealth.
  [GitHub](https://github.com/the-momentum/open-wearables).

EHR
: Electronic health record.
  The clinical system a hospital or clinic uses to store patient charts, such as Epic or Cerner.

MRN
: Medical record number.
  The ID a hospital or clinic uses for a patient.
  Dashboards launched from an {term}`EHR` use it to find the same patient in the {term}`Exchange`.

CGM
: Continuous glucose monitor.
  A wearable sensor that records blood glucose every few minutes.
  The {term}`Exchange` docs include a [CGM tutorial](xref:jhe/tutorial/tutorial-cgm).

MCP
: Model Context Protocol.
  An open protocol that lets AI assistants call tools and read data.
  The {term}`Exchange` has an optional MCP server, deployed separately, so AI tools can query health data.

:::
