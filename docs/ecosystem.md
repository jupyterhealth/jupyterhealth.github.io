# Technical Components

JupyterHealth is composed of several semi-independent technology projects that are designed to work together as one combined system via the {term}`JupyterHealth hub <hub>`.
This page lists the documentation for each piece.

- **[JupyterHealth Exchange](https://docs.jupyterhealth.org/software-documentation/)**: stores {term}`patient-consented data` and serves it over REST, {term}`FHIR`, and {term}`MCP`. Also handles login for the {term}`Hub`.
- **[JupyterHealth client](https://jupyterhealth-client.readthedocs.io)**: Python library for reading {term}`Exchange` data.
- **[JupyterHealth Hub](https://docs.jupyterhealth.org/hub/)**: hosted JupyterHub for analyzing Exchange data and deploying Voilà apps for clinicians.
- **[Demos](https://docs.jupyterhealth.org/demos/)**: example notebooks, each with a researcher view in JupyterLab and a clinician view as a Voilà dashboard. These only run on the demo deployment.
- **[Helm charts](https://github.com/jupyterhealth/helm-charts)**: Helm chart for deploying the Exchange and its MCP server to Kubernetes.
- **[Single-user image](https://github.com/jupyterhealth/singleuser-image)**: the software environment that each user of the hub can access.
- **[SMART on FHIR Jupyter extension](https://github.com/jupyterhealth/jupyter-smart-on-fhir)**: lets an {term}`EHR` launch into a Hub session with {term}`SMART on FHIR` credentials.
- **[SMART on FHIR provider template](https://github.com/jupyterhealth/jupyterhealth-sof-provider-template)**: starter app template that you can fork/modify to create your own dashboard using the Exchange.
- **[OMH shim](https://github.com/jupyterhealth/omh-shim)**: converts wearable data from vendor schemas to {term}`IEEE 1752` and {term}`Open mHealth` schemas.
