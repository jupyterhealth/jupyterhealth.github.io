# Analyze data and build data products

With data in the {term}`Exchange`, a data scientist, researcher, or developer can analyze it.
The goal is usually a {term}`data product`, like a dashboard, that a clinician or patient can use without writing code.

## How it works

- **Work on the Hub.** The {term}`Hub` is a JupyterLab environment that logs you in with your Exchange account.
  The {term}`client library` is already installed and set up to reach the Exchange.
  See the [Hub documentation](xref:hub).
- **Or work anywhere else.** The client library works in any Python environment, and other {term}`FHIR` tools can read from the Exchange's FHIR API.
- **Pull data into a DataFrame.** The client library returns observations as pandas DataFrames, so you can explore them with the usual Python tools.
- **Turn a notebook into a data product.** Voilà shows a notebook as a dashboard, without the code.
  Jupyter Book turns notebooks into reports and websites.
  The [SMART on FHIR provider template](https://github.com/jupyterhealth/jupyterhealth-sof-provider-template) turns a notebook into an app that clinicians open from their {term}`EHR` (see [step 4](share.md)).

The [demos](xref:demos) are worked examples.
Most pair a notebook for researchers with a dashboard for clinicians.
The demos only run on the demo deployment at UC Berkeley.

## Learn more

- [](xref:hub/run-an-analysis): a first notebook, from a blank page.
- [Client library documentation](xref:client)
- [Blood pressure tutorial](xref:demos/getting-started-blood-pressure): a getting started tutorial for pulling and plotting blood pressure data from the Exchange.
- [{term}`CGM` tutorial](xref:demos/researcher-view-cgm): an end-to-end tutorial for pulling and analyzing continuous glucose monitor data from the Exchange.

Next step: [](share.md).
