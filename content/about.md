+++
title = "About"
description = "We are Reimagining How Data Drives Healthcare"
date = "2024-04-04"
aliases = ["about-us", "about-jupyterhealth", "contact"]
+++

<!-- <p style="text-align: center; font-weight: 500; font-size: 36px">We Are Reimagining How Data Drives Healthcare.</p>  -->


To create a smarter, more connected, and patient-centered future, explore our open platform that enhances data accessibility and supports informed decision-making for healthcare researchers, clinicians, and patients.

<!-- [Go to Modular Section](#modular-platform) -->


## **Modular Platform Overview**
**Empowering Healthcare with Modular Platform:**
JupyterHealth introduces a modular platform composed of opens-source components that span the entire lifecycle of digital health research, development, and deployment. From data ingestion involving wearable and clinical data to advanced data analysis and presentation via JupyterHub and Voila, each component is designed to operate independently or in conjunction. This modular setup not only supports rigorous health data standards like HL7 FHIR and Open mHealth but also offers customizable environments to suit diverse operational needs – from secure data storage and robust authentication systems to real-time data processing and scalable infrastructure.  

![JupyterHealthOverview](/images/JupyterHealthDiagram100.png)
<br>
<br>

---

## **Why Choose JupyterHealth?**
<br>

**Democratizing Health Data Management:** Historically, the integration of real-world data from patients into research and clinical care has been confined to the largest and most technologically sophisticated organizations. JupyterHealth is changing this landscape by championing open-source platforms and accessibility for all. Our initiatives are designed to level the playing field, allowing varied healthcare entities and research organizations to leverage comprehensive data for improved care and research outcomes.

**Empowering Research and Care with Open Source Technology:** JupyterHealth embodies the ethos of Project Jupyter, bringing open-source software, shareable notebooks, and reproducible code into the healthcare domain. Our vendor-agnostic infrastructure ensures that various research groups and healthcare providers can adopt and adapt our platform without barriers, fostering unprecedented levels of collaboration across the healthcare ecosystem.

**Ensuring Interoperability and Data Sovereignty:**
In partnership with The Commons Project ([TCP](https://www.thecommonsproject.org/)), we focus on ensuring that our technical stack is interoperable with standard U.S. healthcare protocols. This collaboration not only expands our platform's capabilities but also allows various organizations to develop and implement advanced health technologies. JupyterHealth facilitates seamless data sharing among [The Common Health](https://www.commonhealth.org/) users and healthcare providers, enhancing data sovereignty and empowering users to fully control their data and infrastructure.

**Streamlining Interactive Computing for Healthcare Professionals:**
In partnership with [Project Jupyter](https://jupyter.org/) and International Interactive Computing Collaboration ([2i2c](https://2i2c.org/)), we advance interactive computing to support healthcare research and clinical practice. JupyterHub centralizes access to computational tools, removing the burden of software management and allowing healthcare professionals to concentrate on patient outcomes rather than IT overhead. Our platform is scalable and customizable, ensuring it meets the diverse needs of the healthcare community.

<br>

---
<!-- In HTML -->
<h2 id="modular-platform"></h2>

## **JupyterHealth Modular Platform**
JupyterHealth will be a modular platform consisting of open-source components that span the life cycle of digital health research, development, and deployment. Our approach ensures that each module can function independently or in conjunction, providing flexibility and scalability to meet diverse healthcare needs.  Below is a detailed overview of each module:

<br>

![JupyterHealthDataPiplinePlatform](/images/JupyterHealthDataPlatform100.png)

<br>

* **Data Ingestion:** Seamlessly integrate data from wearable devices, electronic health records (EHRs), and other key health data sources, ensuring a steady flow into JupyterHealth environment. More specifically this will include at least the following:
	* Tools to acquire wearable and clinical data from [Apple HealthKit](https://developer.apple.com/documentation/healthkit) and [CommonHealth](https://www.commonhealth.org/developers)
	* Shims to acquire wearable data from the most common manufacturers
	* Interfaces to import clinical data from federally certified EHR platforms 

<br>

* **Data Standardization and Transformation:** Utilizing tools to standardize and filter data from disparate health data sources, making it easier to work with and analyze. More specifically this will include at least the following: 
	* Tools to standardize wearable data to [Open mHealth](https://www.openmhealth.org/documentation/#/overview/get-started) and [FHIR formats](https://build.fhir.org/ig/HL7/cimi-vital-signs/)
	* Templates for other transformations.

<br>

* **Storage and Authentication:** Securely store and manage access to sensitive health data including PHI. More specifically this will include at least the following:
	* Reference [SMART on FHIR](https://docs.smarthealthit.org) server capable of storing data as FHIR, Open mHealth, and other formats, and managing authentication and access.
	* Modules for connecting to common databases and data lakes
	* Modules to connect existing authentication services, eg via [OIDC](https://openid.net/developers/how-connect-works/.

<br> 

* **Data Management and Analysis:** Leverage JupyterHub for working with and combining data sets, data exploration, analysis, and algorithm development. [JupyterHub](https://jupyter.org/hub) ([documentation](https://jupyterhub.readthedocs.io/en/latest/)) provides the core environment for managing and conducting data analyses. JupyterHub can be used for health-related data work today so long as care is taken with protected data. Additional components will include at least:
	* JupyterHub modules for incorporating data from health data storage
	* Health data-specific analysis packages and libraries contributed by the community.

<br> 

* **Presentation:** Not only to share research and analysis findings but to give care providers data views and visualizations that fit with their current patient workflows. Jupyter Voila ([documentation](https://voila.readthedocs.io/en/stable/)) is a starting point for visualizing Notebooks and outputs of developed algorithms.  Beyond existing tools, this will include at least:
	* Modules for deploying standardized SMART Launch applications to the major EHR platforms supporting federally mandated APIs.

<br>

---

## **Standard Compliance** 

JupyterHealth modules are being built on top of trusted open health data interoperability standards, most of which are federally mandated in the US:
* Clinical data will adhere to [US Core](https://www.hl7.org/fhir/us/core/) and by extension could support [International Patient Access](https://build.fhir.org/ig/HL7/fhir-ipa/) outside the US.
* Wearable and patient-generated data will be [Open mHealth](https://www.openmhealth.org/documentation/#/overview/get-started) and [FHIR](https://build.fhir.org/ig/HL7/cimi-vital-signs/)
* Authentication will follow [SMART on FHIR](https://docs.smarthealthit.org)

![JupyterHealthOverview](/images/JupyterHealthOverview100.png)

This detailed framework underlines our commitment to providing a robust, scalable, and secure environment for healthcare data management and analysis, empowering researchers, clinicians, and technologists to drive innovation in healthcare. 



<!-- ---

## **Implementing JupyterHealth**
For detailed instructions on how to integrate and utilize the JupyterHealth platform within your organization, please visit our [documentation](https://jupyterhealth.github.io/software-documentation/). Our step-by-step guide provides all the necessary information to get you started smoothly and efficiently.


--- 

## **Join Our Community**
Become part of the JupyterHealth community to learn, share, and contribute to the development of our technologies. Engage with us on[GitHub](https://github.com/jupyterhealth) to contribute to the project, find support and collaborate with like-minded professionals across the globe. Your involvement can help shape the future of healthcare technology. -->



