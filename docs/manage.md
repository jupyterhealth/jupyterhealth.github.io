# Manage access to data

Once data is in the {term}`Exchange`, an administrator or data engineer controls who can use it for research or clinical care.

## How it works

- **Run an Exchange.** You can use an Exchange that someone already runs, like the one in the UC Berkeley demo, or run your own.
  Running your own is a job for an engineer or IT team, who can start with the Exchange's [Getting Started guide](xref:jhe/jhe/getting-started).
  If your organization runs its cloud services on Kubernetes, the [Helm chart](https://github.com/jupyterhealth/helm-charts) installs the Exchange there.
  To talk through running JupyterHealth at your organization, [contact the team](https://jupyterhealth.org/#contact).
- **Decide who can see what.** Researchers and clinicians belong to organizations.
  They can read data for the patients in their organizations, and their role (viewer, member, or manager) controls what they can change.
  Patient consent decides what data gets into the Exchange.
  Once data is in, consent doesn't limit which people in the organization can read it.
  See [](xref:jhe/jhe/access-control).
- **Connect other tools.** Other software reads data through the Exchange's APIs, which check the same permissions.
  The {term}`Hub` uses the Exchange for login, and an {term}`EHR` can launch apps that use it (see [step 4](share.md)).
- **Trust your EHR, if you want EHR launches.** For clinicians to open dashboards from their {term}`EHR`, the admin tells the Exchange which EHRs to accept logins from.
  Each clinician also needs a record in the Exchange that is linked to their EHR account.
  See [](xref:jhe/jhe/provider-ehr-launch).

The Exchange has two APIs, plus an optional AI server:

- A [REST API](xref:jhe/jhe/admin-api) for managing organizations, studies, and patients.
- A [FHIR API](xref:jhe/jhe/fhir/fhir-api) for reading and writing health data in the {term}`FHIR` standard.
- An [MCP server](xref:jhe/jhe/mcp-server), deployed separately, so AI tools can query the data.
  See {term}`MCP`.

## Learn more

- [Exchange documentation](xref:jhe)
- [Exchange clients](xref:jhe/jhe/jhe-clients/jhe-clients): how other tools log in to the Exchange.

Next step: [](analyze.md).
