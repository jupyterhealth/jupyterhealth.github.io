# What is JupyterHealth?

JupyterHealth is a project aimed at leveraging the flexibility and open nature of Jupyter to transform medicine, and to empower doctors, patients, and hospitals to make better use of patient data.

## A few key concepts and terminology for JupyterHealth

Here are some high-level ways to understand the JupyterHealth project:

:::{list-table}
:header-rows: 1

* - When people say "JupyterHealth" they might mean...
  - We call it
* - The entire project
  - **JupyterHealth**
* - The collection of tools we build
  - The {term}`JupyterHealth platform <platform>`[^jupyter]
* - A specific tool we build as part of the platform
  - Each has its own name, like the {term}`Exchange` or the {term}`Hub`
* - A specific service someone runs with the JupyterHealth platform
  - A {term}`deployment`, like the demo deployment at UC Berkeley
:::

[^jupyter]: Jupyter is _also_ a platform: a collection of building blocks, standards, and protocols that enable interactive computing, and can be woven together for opinionated services and products.

    JupyterHub is a particular tool for exposing open source tools (in and outside of Jupyter) as an integrated, opinionated service.
    It's a common way to use Jupyter's platform to generate an opinionated product or service.
    A {term}`distribution` of JupyterHub is a collection of choices that can be bundled with a JupyterHub to provide an integrated end-user experience.

## The core workflow we aim to enable

JupyterHealth builds technology, and recipes for deploying that technology, to enable this loop:

1. **A patient** connects their device or personal data with a JupyterHealth {term}`Exchange`, which stores their data securely and only shares it with their {term}`consent <patient-consented data>`.
2. **A data engineer or org administrator** oversees that Exchange to ensure the right things are coming in, and that authenticated parties have the right permissions to access data from many sources via an API.
3. **A data scientist, researcher, or developer** accesses data in the Exchange from a secure cloud environment like the {term}`Hub`, with all the tools needed to understand it.
   They create a {term}`data product` that is meant to be shared with a clinician or patient, with a tool like Voilà or Jupyter Book.
4. **An end user** (usually a clinician or patient) accesses that data product in an authenticated way, on the Hub or in an app that their {term}`EHR` opens, without any coding skills required.

## What JupyterHealth builds

To enable this workflow, JupyterHealth builds technology that fills in the missing pieces.
Together, these make up the {term}`JupyterHealth platform <platform>`.

- The **{term}`JupyterHealth Exchange <Exchange>`** is its flagship new technology.
  It solves the problem of integrating with health-adjacent data systems, consumer health products, etc.
  It also provides authenticated access to that data, scoped by permissions and patient consent.
- The **{term}`JupyterHealth Hub <Hub>`** is an opinionated JupyterHub distribution that is set up alongside an Exchange.
  It provides easy, authenticated access to the Exchange, with a collection of tools that are designed for technically capable users to use that data to create {term}`data products` for clinicians and patients.
  The [Hub configuration is public](https://github.com/2i2c-org/infrastructure/tree/main/config/clusters/jupyter-health), so others can replicate it wherever they like.

The {term}`client library` is a Python tool that lets you quickly pull data from the {term}`Exchange`.
It comes pre-installed on the Hub, but works from any Python environment.
See [Technical components](ecosystem.md) for the documentation of each piece.

## Design principles

JupyterHealth follows the same design principles for its technology that Jupyter uses:

- **Modular.** Each piece should be independently useful and re-usable in other contexts, outside of the full JupyterHealth platform.
  For example, an organization that has its own computing infrastructure could run an Exchange and connect it to that infrastructure instead of a Hub.
- **Built on open standards.** Data is stored and served with standards like {term}`FHIR` and {term}`Open mHealth`, so it works with other tools in health care.
- **Open source and replicable.** The code and deployment configuration are public, so anybody can run their own deployment.

## Origins and governance

JupyterHealth was founded at UC Berkeley and UCSF, and is developed with partners across the open-source scientific computing and digital health communities.
It is governed as a [JupyterHub subproject](https://github.com/jupyterhub/team-compass/issues/752).
See the [team page](https://jupyterhealth.org/team) for who works on it, and [use cases](https://jupyterhealth.org/use-cases) for where it's used.

## Primary sources

- [Platform page on jupyterhealth.org](https://jupyterhealth.org/platform): the platform's components and the standards it uses.
- [JupyterCon 2025 talk](https://www.youtube.com/watch?v=zOeLIFt-z3M): a platform overview from the project leads.
- [IEEE Pulse article](https://doi.org/10.1109/mpuls.2025.3618427): an interview with co-director Ida Sim on open infrastructure for health wearables.
- [Berkeley launch announcement](https://cdss.berkeley.edu/news/berkeley-launches-agile-metabolic-health-and-open-platforms-initiative): the initiative that started the project.
- [JupyterHub subproject proposal](https://github.com/jupyterhub/team-compass/issues/752): why the project joined JupyterHub, and what it set out to do.
