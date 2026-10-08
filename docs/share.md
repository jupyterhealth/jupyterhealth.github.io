# Share data products with clinicians and patients

Once someone has built a {term}`data product` from {term}`Exchange` data, like a dashboard, clinicians and patients need a way to open it.

## For clinicians

Clinicians can open a data product in two ways.
Both are still being developed, so the details may change.

:::{list-table}
:header-rows: 1

* -
  - On the Hub
  - Launched from the EHR
* - Where the clinician starts
  - The {term}`Hub`'s website
  - Their {term}`EHR`, with a patient's chart open
* - How they log in
  - With an Exchange account
  - No extra login. The app uses their EHR login.
* - How the patient is chosen
  - The clinician picks one in the dashboard
  - The EHR passes along the patient whose chart is open
* - Best for
  - Research teams, prototypes, and people who already use the Hub
  - Day-to-day clinical care
:::

Hub dashboards are the easiest place to start.
See the [Hub documentation](xref:hub) and the [demos](xref:demos), which only run on the demo deployment.

The rest of this section covers the second path, which uses {term}`SMART on FHIR`.
It's the better fit for day-to-day care, because clinicians already work in their EHR all day.

### What SMART on FHIR does

SMART on FHIR is a standard that lets an EHR open an outside app and tell it two things: who the user is, and which patient they're looking at.
Most major EHRs, like Epic and Cerner, support SMART on FHIR.

For JupyterHealth, this means a clinician can click a button in a patient's chart and see that patient's wearable data from the Exchange, without a second login and without searching for the patient again.

Patients also use SMART on FHIR in [step 1](collect.md), when they log in to their hospital's patient portal to bring in their own records.
For clinicians, it works the other way around: their EHR uses it to open an outside app.

### How a launch works

```{mermaid}
sequenceDiagram
  participant C as Clinician
  participant E as EHR
  participant A as Dashboard app
  participant X as Exchange
  C->>E: Opens a patient's chart, clicks the app
  E->>A: Opens the app
  E->>A: Gives it the patient and a signed ID for the clinician
  A->>X: Trades the clinician's ID for an Exchange token
  A->>X: Looks up the patient by MRN, asks for their data
  X->>A: Returns data the clinician is allowed to see
  A->>C: Shows the dashboard inside the EHR
```

Two things must be set up first:

- **The Exchange has to trust the EHR.** The Exchange admin sets this up.
  See [](manage.md).
- **The patient has to exist in both systems with the same {term}`MRN`.** The app uses the MRN to match the EHR's patient to the Exchange's patient.
  See [](xref:jhe/jhe/patient-identifiers).

### Where to start

- **[SMART on FHIR provider template](https://github.com/jupyterhealth/jupyterhealth-sof-provider-template)**: start here.
  Copy this repository, edit one cell of a notebook, and serve it as a dashboard with Voilà.
  The app runs on its own server, separate from the Hub.
  Its quickstart walks through a test launch, and it includes an example {term}`CGM` dashboard.
- **[jhe-smart-demo](https://github.com/jupyterhealth/jhe-smart-demo)**: a mock EHR, FHIR server, and Exchange that run on your own machine, for testing a launch without a real EHR.
  The demo still asks for a separate Exchange login instead of trading the EHR's ID for an Exchange token.
- **[jupyter-smart-on-fhir](https://github.com/jupyterhealth/jupyter-smart-on-fhir)**: the Jupyter extension that handles the SMART launch.
  The provider template uses this extension, so you only need it directly if you're building something different.
- **[](xref:jhe/jhe/provider-ehr-launch)** and the [MedPlum dashboard tutorial](xref:jhe/tutorial/medplum-provider-dashboard), in the Exchange docs: how to set up the Exchange side of a launch.

:::{warning} These are early-stage tools
The template is a starting point, not a production app.
Before using it with real patients, your organization still needs to register the app with its EHR, do a security review, and plan for many clinicians using it at once.
The template's [scope notes](https://github.com/jupyterhealth/jupyterhealth-sof-provider-template#scope) list what's missing.
:::

## For patients

Data products for patients are earlier along, and there isn't a standard way to share them yet.
The [demos](xref:demos) include a patient view of the CGM dashboard, as an example of what one could look like.
