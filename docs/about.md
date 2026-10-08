# How JupyterHealth works

JupyterHealth builds open source tools, and recipes for deploying them, that give patients, clinicians, and analysts more control over health data.

## The core workflow

JupyterHealth is built around four steps:

1. **[](collect.md).** An organization sets up a {term}`study` in a JupyterHealth {term}`Exchange`.
   Patients join the study, choose what to share, and set up the devices and apps that send data to the Exchange.
   The Exchange only accepts the kinds of data from a patient that they have {term}`consented <patient-consented data>` to share.
2. **[](manage.md).** An administrator or data engineer runs the Exchange.
   The administrator decides who can access the data, and which applications can read it through the Exchange's APIs.
3. **[](analyze.md).** A data scientist, researcher, or developer pulls data from the Exchange into an environment like the {term}`Hub` for analysis.
   The analyst turns the results into a {term}`data product` (like a dashboard or website), with a tool like Voilà, which shows a notebook as a dashboard, or Jupyter Book.
4. **[](share.md).** Clinicians and patients open that data product on the Hub, or from their {term}`EHR`, without writing any code.

See [](components.md) for the documentation of each tool in this workflow.

## Design principles

JupyterHealth follows the same design principles as {term}`Jupyter`:

- **Modular.** Each piece should be useful on its own, outside the full JupyterHealth {term}`platform`.
  For example, an organization that has its own computing infrastructure could run an Exchange and connect it to that infrastructure instead of a Hub.
- **Built on open standards.** Data is stored and served with standards like {term}`FHIR` and {term}`Open mHealth`, so it works with other tools in health care.
- **Open source and replicable.** The code and deployment configuration are public, so anybody can run their own {term}`deployment`.
