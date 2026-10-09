# Components

JupyterHealth is made of several projects that can be used on their own or together as a combined {term}`JupyterHealth platform <platform>`.
This page links to the documentation for each component.

- **[JupyterHealth Exchange](xref:jhe)**: stores {term}`patient-consented data` and serves it over REST and {term}`FHIR`, with an optional {term}`MCP` server.
  The Exchange also handles login for the {term}`Hub`.
- **[JupyterHealth client](xref:client)**: Python library for reading {term}`Exchange` data.
- **[JupyterHealth Hub](xref:hub)**: hosted JupyterHub for analyzing Exchange data and prototyping dashboards.
  Its [configuration is public](https://github.com/2i2c-org/infrastructure/tree/main/config/clusters/jupyter-health).
- **[Demos](xref:demos)**: example notebooks, each with a researcher view in JupyterLab and a clinician view as a Voilà dashboard.
  The demos only run on the demo deployment.
- **[Helm charts](https://github.com/jupyterhealth/helm-charts)**: Helm chart for deploying the Exchange and its MCP server to Kubernetes.
- **[Single-user image](https://github.com/jupyterhealth/singleuser-image)**: the software environment each Hub user gets.
- **{term}`SMART on FHIR` tools**: for dashboards that clinicians open from their {term}`EHR`.
  See [](share.md) for how they fit together.
  - **[Provider template](https://github.com/jupyterhealth/jupyterhealth-sof-provider-template)**: a starter dashboard app to copy and edit.
  - **[jhe-smart-demo](https://github.com/jupyterhealth/jhe-smart-demo)**: a mock EHR and Exchange for testing a launch locally.
  - **[jupyter-smart-on-fhir](https://github.com/jupyterhealth/jupyter-smart-on-fhir)**: the Jupyter extension that handles the SMART launch.
- **[OMH shim](https://github.com/jupyterhealth/omh-shim)**: converts wearable data from vendor schemas to {term}`IEEE 1752` and {term}`Open mHealth` schemas.
