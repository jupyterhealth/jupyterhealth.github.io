# Collect patient data

The first step is getting health data into the {term}`Exchange`.
This step usually involves a research team or clinic that runs a {term}`study`, and the patients who join the study.

Health data is scattered across vendor apps, devices, and hospital systems, each with its own format.
Because of this, patients rarely get to see or use their own data.
The Exchange gives that data one home, in open standard formats, and lets patients control which kinds of data go into it.

## How it works

1. **An organization creates a study** in the Exchange.
   The study lists the kinds of data the organization wants, like blood glucose or heart rate, and which apps can send that data.
2. **It invites patients** with a link.
3. **Each patient joins and chooses what to share.** The Exchange won't accept a kind of data from a patient until they agree to share it.
   Patients can share some kinds of data and not others, and change their choices later.
   See {term}`patient-consented data`.
4. **Their data flows into the Exchange.** Data can come in a few ways:
   - **Wearables, through the {term}`CommonHealth` Android app.** Patients connect devices like glucose monitors to the app, and it sends their readings to the Exchange.
   - **Wearables, through {term}`Open Wearables`.** The Exchange regularly checks an Open Wearables server for new data from devices like the Oura ring, and converts it with the [OMH shim](https://github.com/jupyterhealth/omh-shim), a JupyterHealth library.
     See [](xref:jhe/jhe/ow-integration).
   - **A patient's own hospital records.** The patient logs in to their hospital's patient portal with {term}`SMART on FHIR`, and the Exchange copies in records like conditions, medications, allergies, and lab results.
     See [](xref:jhe/jhe/patient-access-integration).
   - **Any other app**, through the Exchange's [FHIR API](xref:jhe/jhe/fhir/fhir-api).

Everything can be read through the Exchange's {term}`FHIR` API.
Wearable readings are FHIR Observations whose values use the {term}`Open mHealth` and {term}`IEEE 1752` formats, so a reading has the same structure no matter which device it came from.

## Learn more

- [Exchange documentation](xref:jhe): how studies, patients, and consent work.
- [](xref:jhe/jhe/patient-identifiers): how the Exchange tells patients apart, including their hospital {term}`MRN`.

Next step: [](manage.md).
