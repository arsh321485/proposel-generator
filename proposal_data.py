
PROPOSALS = {
    "Cybersecurity_Capability_Maturity_Assessment": {
        "methodology": [
            "Phase 1 - Mobilisation & Scoping: SecureITLab initiates the engagement with a formal kick-off meeting to align on objectives, confirm the capability domains in scope, and collect relevant documentation including existing policies, risk registers, and prior assessment results.",
            "Phase 2 - Assessment & Interviews: Structured interviews and workshops are conducted with domain owners and key stakeholders across each capability area. Evidence is reviewed against the selected maturity model (NIST CSF, CMMC, or equivalent), and current practices are mapped to defined maturity levels.",
            "Phase 3 - Analysis & Scoring: Assessment findings are analysed and scored per capability domain. Gap analysis is performed to identify the delta between current and target maturity, and findings are risk-rated to inform prioritisation.",
            "Phase 4 - Reporting & Roadmap Presentation: A comprehensive maturity scorecard and gap analysis report are produced, accompanied by a prioritised improvement roadmap. Findings are presented to key stakeholders and an executive summary deck is delivered.",
        ],
        "timeline": [
            ("Phase 1 - Mobilisation & Scoping", "Kick-off meeting; scope confirmation; documentation collection; stakeholder identification", "1 week", "Scoping document; stakeholder register"),
            ("Phase 2 - Assessment & Interviews", "Stakeholder interviews; evidence review; maturity mapping per domain", "2 weeks", "Interview notes; evidence log; draft maturity scores"),
            ("Phase 3 - Analysis & Scoring", "Gap analysis; maturity scoring; risk-rating of findings; improvement prioritisation", "1 week", "Maturity scorecard; gap analysis workbook"),
            ("Phase 4 - Reporting & Roadmap Presentation", "Report drafting; improvement roadmap; executive presentation; client debrief", "1 week", "Maturity assessment report; improvement roadmap; executive presentation"),
        ],
    },
    "Cybersecurity_Regulatory_and_Compliance": {
        "methodology": [
            "Phase 1 - Regulatory Scoping & Applicability Mapping: SecureITLab identifies all regulations, frameworks, and standards applicable to the organisation (e.g., GDPR, PCI-DSS, NCA ECC, NESA, DORA) based on jurisdiction, industry, and data types processed. A regulatory applicability matrix is produced.",
            "Phase 2 - Evidence Collection & Control Walkthroughs: Compliance evidence is gathered through document reviews, system walkthroughs, and structured interviews with process owners. Each control requirement is mapped to existing practices and documented.",
            "Phase 3 - Gap Analysis & Risk Rating: Identified gaps are assessed against each regulatory requirement, rated by risk severity, and categorised by remediation priority. Findings are consolidated into a compliance gap register.",
            "Phase 4 - Reporting & Remediation Planning: A compliance gap report, remediation action plan with ownership assignments, and a compliance evidence register are produced and presented to key stakeholders.",
        ],
        "timeline": [
            ("Phase 1 - Regulatory Scoping & Applicability Mapping", "Regulatory research; applicability determination; matrix development", "1 week", "Regulatory applicability matrix"),
            ("Phase 2 - Evidence Collection & Control Walkthroughs", "Document collection; stakeholder interviews; control mapping", "2 weeks", "Evidence log; control mapping workbook"),
            ("Phase 3 - Gap Analysis & Risk Rating", "Compliance gap assessment; risk-rating; finding categorisation", "1 week", "Compliance gap register; risk-rated findings"),
            ("Phase 4 - Reporting & Remediation Planning", "Gap report drafting; remediation action plan; evidence register; stakeholder presentation", "1 week", "Compliance gap report; remediation action plan; compliance evidence register"),
        ],
    },
    "Threat_and_Risk_Assessment": {
        "methodology": [
            "Phase 1 - Scoping & Asset Identification: SecureITLab conducts a kick-off to confirm scope, identify assets in scope (systems, data, processes), gather contextual documentation, and define the risk assessment criteria including likelihood and impact scales aligned with ISO 27005 / NIST SP 800-30.",
            "Phase 2 - Threat Identification & Analysis: A structured threat modelling exercise is performed, drawing on threat intelligence sources, industry threat catalogues, and stakeholder workshops. Threat actors, threat events, and attack vectors are documented against each asset.",
            "Phase 3 - Risk Evaluation & Treatment Planning: Likelihood and impact are assessed for each identified threat scenario. A risk register is populated, a risk heat-map is generated, and risk treatment options (accept, mitigate, transfer, avoid) are developed for each risk.",
            "Phase 4 - Reporting & Executive Presentation: A comprehensive TRA report is produced, including the threat catalogue, risk register, heat-map, and risk treatment plan. An executive risk summary is presented to senior stakeholders.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & Asset Identification", "Kick-off; asset inventory; risk criteria definition; documentation review", "1 week", "Scoping document; asset register; risk criteria matrix"),
            ("Phase 2 - Threat Identification & Analysis", "Threat modelling workshops; threat actor profiling; attack vector mapping", "2 weeks", "Threat catalogue; threat event register"),
            ("Phase 3 - Risk Evaluation & Treatment Planning", "Likelihood/impact scoring; risk register population; heat-map generation; treatment options", "1 week", "Risk register; risk heat-map; risk treatment plan"),
            ("Phase 4 - Reporting & Executive Presentation", "TRA report drafting; executive summary; client presentation and debrief", "1 week", "Threat and Risk Assessment report; executive risk summary; presentation deck"),
        ],
    },
    "Data_Governance_Framework": {
        "methodology": [
            "Phase 1 - Discovery & Current State Assessment: SecureITLab assesses the organisation's existing data governance maturity through stakeholder interviews, document reviews, and process walkthroughs. Key pain points, data domains, and governance gaps are identified.",
            "Phase 2 - Framework Design: A tailored Data Governance Framework is designed, encompassing governance principles, operating model, committee structures, data domain definitions, and accountability mechanisms aligned with business objectives and regulatory requirements.",
            "Phase 3 - Policy & Documentation Development: The governance charter, policy library, standard operating procedures, and RACI matrix are drafted, reviewed with stakeholders, and refined to reflect operational realities.",
            "Phase 4 - Review, Approval & Handover: Final documentation is presented for stakeholder approval. A handover session is conducted to transition ownership to the client's data governance team, including implementation guidance.",
        ],
        "timeline": [
            ("Phase 1 - Discovery & Current State Assessment", "Stakeholder interviews; document review; maturity assessment; pain-point identification", "2 weeks", "Current state assessment report; data domain inventory"),
            ("Phase 2 - Framework Design", "Operating model design; committee structure; governance principles; data domain mapping", "3 weeks", "Data governance framework design document; operating model"),
            ("Phase 3 - Policy & Documentation Development", "Policy drafting; RACI matrix; SOPs; stakeholder review cycles", "2 weeks", "Governance charter; policy library; RACI matrix; SOPs"),
            ("Phase 4 - Review, Approval & Handover", "Final review; stakeholder approval; handover session; implementation guidance", "1 week", "Approved governance framework package; implementation roadmap"),
        ],
    },
    "Data_Impact_Assessment": {
        "methodology": [
            "Phase 1 - Scoping & Project Understanding: SecureITLab works with the client to define the project, system, or process under assessment, confirm the legal basis for processing, and gather relevant documentation including technical specifications and data flow descriptions.",
            "Phase 2 - Data Flow Mapping & Necessity Assessment: Personal data flows are mapped across the project lifecycle. A necessity and proportionality assessment is performed to evaluate whether data collection and processing are justified and data-minimised.",
            "Phase 3 - Risk Identification & Mitigation Planning: Privacy risks are identified and assessed for likelihood and severity. Mitigation measures are proposed for each risk, and residual risk is documented.",
            "Phase 4 - Reporting, Review & Sign-off: The completed DPIA/PIA report is drafted, reviewed with DPO and relevant stakeholders, and submitted for formal sign-off. Residual risk statements and recommendations are finalised.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & Project Understanding", "Kick-off; requirements gathering; documentation collection; legal basis review", "1 week", "Scoping record; project description; data processing inventory"),
            ("Phase 2 - Data Flow Mapping & Necessity Assessment", "Data flow mapping; necessity and proportionality review; data minimisation assessment", "1 week", "Data flow map; necessity assessment record"),
            ("Phase 3 - Risk Identification & Mitigation Planning", "Privacy risk assessment; mitigation measure design; residual risk calculation", "1 week", "Risk register with mitigations; residual risk statement"),
            ("Phase 4 - Reporting, Review & Sign-off", "DPIA/PIA report drafting; DPO and stakeholder review; sign-off process", "1 week", "Final DPIA/PIA report; sign-off documentation"),
        ],
    },
    "Data_Policies,_Procedures_and_Guidelines": {
        "methodology": [
            "Phase 1 - Policy Inventory & Gap Review: SecureITLab conducts a review of the organisation's existing data policies, procedures, and guidelines, benchmarking them against regulatory requirements and best practice frameworks to identify gaps and outdated content.",
            "Phase 2 - Policy Drafting: New and updated policies, procedures, and quick-reference guidelines are drafted covering data classification, retention, access control, breach response, and third-party sharing, tailored to the organisation's context.",
            "Phase 3 - Stakeholder Review & Approval: Draft documents are circulated for review by legal, compliance, IT, and business stakeholders. Feedback is incorporated and documents are revised for formal approval.",
            "Phase 4 - Finalisation & Handover: Approved documents are formatted, version-controlled, and handed over with review and approval records. Implementation guidance and a policy communication plan are provided.",
        ],
        "timeline": [
            ("Phase 1 - Policy Inventory & Gap Review", "Existing policy review; regulatory benchmarking; gap identification; priority list", "1 week", "Policy inventory; gap analysis register"),
            ("Phase 2 - Policy Drafting", "Drafting of policies, procedures, and guidelines; internal quality review", "2 weeks", "Draft policy library; draft procedures; draft guidelines"),
            ("Phase 3 - Stakeholder Review & Approval", "Circulation for review; feedback collection; revision; approval workflow", "1 week", "Reviewed and revised documents; approval records"),
            ("Phase 4 - Finalisation & Handover", "Final formatting; version control; handover session; communication plan", "1 week", "Final policy and procedure library; quick-reference guides; review records"),
        ],
    },
    "Data_Privacy_Regulatory_and_Compliance": {
        "methodology": [
            "Phase 1 - Regulatory Scoping & Applicability Mapping: SecureITLab identifies applicable privacy regulations (GDPR, PDPA, LGPD, PIPL, and others) based on the organisation's jurisdictions of operation, data types processed, and sector-specific requirements. A regulatory applicability matrix is produced.",
            "Phase 2 - Current State Review & Evidence Collection: The organisation's data-handling practices, privacy notices, consent mechanisms, data subject rights processes, and third-party agreements are reviewed against each applicable regulation. Evidence is collected through document reviews and stakeholder interviews.",
            "Phase 3 - Gap Analysis & Risk Rating: Compliance gaps are identified, risk-rated by severity and regulatory exposure, and consolidated into a structured compliance gap register with priority ratings.",
            "Phase 4 - Reporting & Remediation Roadmap: A privacy compliance gap report, remediation roadmap with ownership and timelines, and a privacy obligations summary are produced and presented to key stakeholders.",
        ],
        "timeline": [
            ("Phase 1 - Regulatory Scoping & Applicability Mapping", "Regulatory research; jurisdiction mapping; applicability determination; matrix development", "1 week", "Regulatory applicability matrix; privacy obligations summary"),
            ("Phase 2 - Current State Review & Evidence Collection", "Document review; stakeholder interviews; consent and notice review; DPA review", "2 weeks", "Evidence log; current state assessment notes"),
            ("Phase 3 - Gap Analysis & Risk Rating", "Gap identification; risk-rating; finding categorisation; priority assignment", "1 week", "Compliance gap register; risk-rated findings list"),
            ("Phase 4 - Reporting & Remediation Roadmap", "Gap report drafting; roadmap development; stakeholder presentation", "1 week", "Privacy compliance gap report; remediation roadmap; privacy obligations summary"),
        ],
    },
    "Data_Protection_Strategies": {
        "methodology": [
            "Phase 1 - Discovery & Data Landscape Assessment: SecureITLab maps the organisation's data environment, including data types, sensitivity classifications, storage locations, processing activities, and existing protection controls. Key risks and protection gaps are identified.",
            "Phase 2 - Strategy Design & Control Mapping: A comprehensive data protection strategy is designed, covering data classification, encryption standards, access control frameworks, and DLP controls. Controls are mapped to regulatory requirements and risk appetite.",
            "Phase 3 - Technology & Tool Recommendations: SecureITLab evaluates the suitability of existing and potential technology solutions to support data protection strategy objectives, providing vendor-agnostic recommendations and control specifications.",
            "Phase 4 - Reporting & Implementation Roadmap: A data protection strategy document, technology recommendations, and a phased implementation roadmap with prioritised initiatives are produced and presented.",
        ],
        "timeline": [
            ("Phase 1 - Discovery & Data Landscape Assessment", "Data mapping; asset classification; existing control review; risk and gap identification", "2 weeks", "Data landscape map; protection gap register"),
            ("Phase 2 - Strategy Design & Control Mapping", "Classification scheme design; control framework mapping; encryption and access standards", "2 weeks", "Data classification scheme; control mapping matrix"),
            ("Phase 3 - Technology & Tool Recommendations", "Tool evaluation; vendor-agnostic assessment; control specifications", "1 week", "Technology recommendations report; control specifications"),
            ("Phase 4 - Reporting & Implementation Roadmap", "Strategy document finalisation; implementation roadmap; stakeholder presentation", "1 week", "Data protection strategy document; implementation roadmap; executive summary"),
        ],
    },
    "Data_Security_and_Privacy_Monitoring_Metrics": {
        "methodology": [
            "Phase 1 - Stakeholder Alignment & Requirements Gathering: SecureITLab engages with senior stakeholders, security, privacy, and risk teams to understand reporting needs, existing measurement capabilities, and desired programme outcomes.",
            "Phase 2 - Metrics Design & KPI/KRI Definition: A tailored metrics catalogue is developed, defining KPIs and KRIs for each data security and privacy programme area. Measurement methodologies, data sources, and calculation logic are specified for each metric.",
            "Phase 3 - Dashboard Design & Reporting Cadence: Dashboard templates are designed for both operational and executive audiences. A reporting cadence plan is established defining frequency, audience, and escalation triggers.",
            "Phase 4 - Finalisation, Review & Handover: The completed metrics framework, dashboard templates, and measurement guide are reviewed with stakeholders and formally handed over with implementation guidance.",
        ],
        "timeline": [
            ("Phase 1 - Stakeholder Alignment & Requirements Gathering", "Stakeholder interviews; reporting needs assessment; existing metrics inventory", "1 week", "Requirements document; existing metrics inventory"),
            ("Phase 2 - Metrics Design & KPI/KRI Definition", "Metrics catalogue development; KPI/KRI definition; data source mapping; calculation logic", "2 weeks", "Metrics catalogue; KPI/KRI definitions; measurement methodology guide"),
            ("Phase 3 - Dashboard Design & Reporting Cadence", "Dashboard template design; visualisation layout; reporting cadence plan", "1 week", "Dashboard design templates; reporting cadence plan"),
            ("Phase 4 - Finalisation, Review & Handover", "Stakeholder review; final revisions; handover session; implementation guidance", "1 week", "Final metrics framework; approved dashboard templates; implementation guidance"),
        ],
    },
    "API_Testing": {
        "methodology": [
            "Phase 1 - Scoping & API Discovery: SecureITLab confirms the API endpoints in scope (REST, SOAP, GraphQL), obtains API documentation (Swagger/OpenAPI specifications), and configures the testing environment including authentication credentials and test accounts.",
            "Phase 2 - Automated & Manual API Testing: Automated tooling is used to enumerate endpoints and perform baseline testing. Manual testing is conducted against the OWASP API Security Top 10, covering broken object-level authorisation, excessive data exposure, injection, and improper assets management.",
            "Phase 3 - Exploitation & Evidence Capture: Confirmed vulnerabilities are exploited in a controlled manner to demonstrate real-world impact. Proof-of-concept evidence including request/response captures and payload demonstrations is documented.",
            "Phase 4 - Reporting & Remediation Guidance: A comprehensive API security test report is produced, including findings with CVSS severity ratings, exploitation evidence, and detailed remediation guidance. A debrief is conducted with the development and security teams.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & API Discovery", "Scope confirmation; API documentation review; environment setup; credential provisioning", "3 days", "Scoping agreement; test environment configuration record"),
            ("Phase 2 - Automated & Manual API Testing", "Automated scanning; manual OWASP API Top 10 testing; endpoint enumeration", "1 week", "Testing notes; preliminary findings log"),
            ("Phase 3 - Exploitation & Evidence Capture", "Vulnerability confirmation; controlled exploitation; request/response capture; PoC documentation", "3 days", "Exploitation evidence package; PoC artefacts"),
            ("Phase 4 - Reporting & Remediation Guidance", "Report drafting; CVSS scoring; remediation guidance; client debrief", "3 days", "API security test report; remediation guidance document"),
        ],
    },
    "ASVS_-_Application_Security_Verification_Standard": {
        "methodology": [
            "Phase 1 - Scoping & Level Selection: SecureITLab works with the client to confirm the ASVS level (L1, L2, or L3) and the application components in scope. Test plans are prepared and access to the application and supporting documentation is arranged.",
            "Phase 2 - Verification Testing: Systematic verification is performed across all applicable ASVS control categories (authentication, session management, access control, input validation, cryptography, etc.) using both automated tooling and manual testing techniques.",
            "Phase 3 - Evidence Review & Scoring: Control compliance evidence is reviewed, scored, and documented per ASVS category. Gaps and failures are identified, risk-rated, and mapped to remediation actions.",
            "Phase 4 - Reporting & Attestation: An ASVS scorecard is produced showing pass/fail status per control. A findings report with remediation priorities is delivered. Where all controls are satisfied, an ASVS attestation letter is issued.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & Level Selection", "ASVS level confirmation; scope definition; test plan preparation; access arrangement", "3 days", "Scoping document; test plan; access credentials record"),
            ("Phase 2 - Verification Testing", "Systematic ASVS control testing; automated and manual techniques across all categories", "2 weeks", "Testing workbook; preliminary findings list"),
            ("Phase 3 - Evidence Review & Scoring", "Evidence review; scorecard population; gap identification; risk rating", "1 week", "ASVS scorecard; evidence package; gap register"),
            ("Phase 4 - Reporting & Attestation", "Findings report drafting; remediation priorities; attestation letter (if applicable); debrief", "1 week", "ASVS scorecard; findings and remediation report; attestation letter"),
        ],
    },
    "Application_Testing": {
        "methodology": [
            "Phase 1 - Scoping & Test Planning: SecureITLab confirms the application type (desktop, mobile, or thick-client), defines the test scope, obtains application builds and credentials, and prepares a detailed test plan covering authentication, authorisation, session management, and business logic.",
            "Phase 2 - Security Testing: Comprehensive security testing is conducted using both automated and manual techniques, assessing the application against OWASP standards. Testing covers authentication flaws, authorisation bypasses, session vulnerabilities, input validation, and business logic weaknesses.",
            "Phase 3 - Exploitation & Evidence Collection: Confirmed vulnerabilities are exploited to demonstrate real-world impact. CVSS scores are assigned and evidence artefacts (screenshots, payloads, traffic captures) are documented.",
            "Phase 4 - Reporting & Remediation Roadmap: A security test report with prioritised findings, CVSS scores, and evidence is produced. A remediation roadmap and debrief session are provided to development and security teams.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & Test Planning", "Application scoping; test plan preparation; environment setup; credential provisioning", "3 days", "Scoping agreement; test plan"),
            ("Phase 2 - Security Testing", "Automated scanning; manual testing (auth, authz, session, business logic, input validation)", "2 weeks", "Testing notes; preliminary findings log"),
            ("Phase 3 - Exploitation & Evidence Collection", "Vulnerability confirmation; CVSS scoring; evidence capture; PoC documentation", "1 week", "Exploitation evidence package; CVSS-rated findings list"),
            ("Phase 4 - Reporting & Remediation Roadmap", "Report drafting; remediation roadmap; debrief session", "3 days", "Application security test report; remediation roadmap"),
        ],
    },
    "Compromise_Assessment": {
        "methodology": [
            "Phase 1 - Scoping & Data Collection Setup: SecureITLab defines the scope of the compromise assessment, deploys or configures collection agents, and establishes data feeds from endpoint detection, SIEM, network logs, and Active Directory to support analysis.",
            "Phase 2 - Indicator Collection & Host/Network Analysis: Host-based and network-based indicators of compromise (IoCs) and indicators of attack (IoAs) are collected and analysed. Endpoint forensic artefacts, log sources, and network traffic are examined for signs of malicious activity.",
            "Phase 3 - Threat Hunting & Dwell-Time Analysis: SecureITLab's threat hunters actively search for stealthy attacker activity using MITRE ATT&CK-aligned techniques. Attacker dwell time, lateral movement paths, and persistence mechanisms are identified where present.",
            "Phase 4 - Reporting & Containment Recommendations: A comprehensive compromise assessment report is produced detailing IoC/IoA findings, attacker activity timelines, and dwell-time analysis. Containment, eradication, and hardening recommendations are provided.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & Data Collection Setup", "Scope definition; agent deployment; log source configuration; data feed validation", "3 days", "Scoping document; data collection confirmation"),
            ("Phase 2 - Indicator Collection & Host/Network Analysis", "IoC/IoA collection; endpoint forensics; log analysis; network traffic review", "1 week", "IoC/IoA findings list; host and network analysis notes"),
            ("Phase 3 - Threat Hunting & Dwell-Time Analysis", "ATT&CK-aligned threat hunting; lateral movement tracing; persistence identification; dwell-time calculation", "1 week", "Threat hunt findings; attacker activity timeline; dwell-time estimate"),
            ("Phase 4 - Reporting & Containment Recommendations", "Report drafting; containment and eradication guidance; hardening recommendations; debrief", "3 days", "Compromise assessment report; containment and eradication recommendations"),
        ],
    },
    "Configuration_Review": {
        "methodology": [
            "Phase 1 - Scoping & Target Identification: SecureITLab confirms the systems and devices in scope (firewalls, servers, databases, cloud resources), selects applicable CIS Benchmarks and vendor hardening guides, and coordinates configuration data collection with the client.",
            "Phase 2 - Configuration Data Collection: Configuration exports, scripts, and screenshots are gathered from target systems in a non-intrusive manner. Baseline documentation from the client is reviewed alongside live configuration data.",
            "Phase 3 - Analysis Against Benchmarks: Each configuration item is assessed against the relevant CIS Benchmark or vendor hardening standard. Pass/fail determinations are recorded per control and findings are risk-rated based on exploitability and impact.",
            "Phase 4 - Reporting & Hardening Guidance: A configuration review report with pass/fail results, risk-rated findings, and hardening script recommendations is produced and presented to technical and security stakeholders.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & Target Identification", "Scope confirmation; benchmark selection; data collection coordination", "2 days", "Scoping document; benchmark selection record"),
            ("Phase 2 - Configuration Data Collection", "Configuration export collection; baseline documentation review; data validation", "3 days", "Configuration data set; baseline documentation"),
            ("Phase 3 - Analysis Against Benchmarks", "CIS/vendor benchmark assessment; pass/fail determination; risk rating", "1 week", "Configuration analysis workbook; risk-rated findings list"),
            ("Phase 4 - Reporting & Hardening Guidance", "Report drafting; hardening script recommendations; compliance mapping; debrief", "3 days", "Configuration review report; hardening recommendations; compliance mapping"),
        ],
    },
    "Penetration_Testing": {
        "methodology": [
            "Phase 1 - Pre-Engagement & Reconnaissance: SecureITLab conducts rules-of-engagement finalisation, obtains written authorisation, and performs passive and active reconnaissance to map the attack surface, identify exposed assets, and gather intelligence on the target environment.",
            "Phase 2 - Vulnerability Discovery & Exploitation: Automated scanning and manual exploitation techniques (following PTES and OWASP methodologies) are used to identify and exploit vulnerabilities across the agreed scope. Exploitation is performed in a controlled, non-destructive manner.",
            "Phase 3 - Post-Exploitation & Lateral Movement: Successful exploits are leveraged to simulate post-compromise activities including privilege escalation, lateral movement, and persistence, demonstrating the realistic business impact of identified vulnerabilities.",
            "Phase 4 - Reporting & Debrief: A detailed penetration test report including executive summary, technical findings with CVSS scores, proof-of-concept evidence, and remediation recommendations is delivered. A debrief session is held with the security and technical teams.",
        ],
        "timeline": [
            ("Phase 1 - Pre-Engagement & Reconnaissance", "Rules of engagement; authorisation sign-off; passive/active reconnaissance; attack surface mapping", "3 days", "Rules of engagement document; reconnaissance summary"),
            ("Phase 2 - Vulnerability Discovery & Exploitation", "Automated scanning; manual exploitation; vulnerability confirmation; impact assessment", "2 weeks", "Vulnerability list; exploitation notes; preliminary findings"),
            ("Phase 3 - Post-Exploitation & Lateral Movement", "Privilege escalation; lateral movement simulation; persistence demonstration; impact quantification", "3 days", "Post-exploitation findings; attack path diagram"),
            ("Phase 4 - Reporting & Debrief", "Report drafting; CVSS scoring; PoC evidence packaging; debrief session", "3 days", "Executive summary; technical findings report; PoC evidence; remediation recommendations"),
        ],
    },
    "Red_Teaming_Exercise": {
        "methodology": [
            "Phase 1 - Planning & Intelligence Gathering: SecureITLab defines campaign objectives with the client's senior leadership, conducts open-source intelligence (OSINT) gathering, identifies initial access vectors, and develops a bespoke campaign plan aligned to realistic threat actor TTPs.",
            "Phase 2 - Initial Access & Persistence: The Red Team attempts to gain initial access through phishing, credential attacks, exploitation of internet-facing assets, or physical access techniques as agreed. Persistence mechanisms are established to maintain access for the campaign duration.",
            "Phase 3 - Lateral Movement & Objective Achievement: From the initial foothold, the Red Team conducts privilege escalation, credential harvesting, lateral movement, and attempts to achieve pre-defined campaign objectives (e.g., access to crown-jewel systems, data exfiltration simulation).",
            "Phase 4 - Purple Team Debrief & Reporting: A comprehensive Red Team campaign report is produced, detailing the attack narrative, MITRE ATT&CK kill-chain mapping, detection and response assessment, and strategic recommendations. A purple team debrief is facilitated with the Blue Team.",
        ],
        "timeline": [
            ("Phase 1 - Planning & Intelligence Gathering", "Campaign scoping; OSINT; initial access vector identification; campaign plan development", "2 weeks", "Campaign plan; OSINT summary; rules of engagement"),
            ("Phase 2 - Initial Access & Persistence", "Phishing simulation; exploitation; credential attacks; persistence establishment", "2 weeks", "Initial access record; persistence mechanisms documented"),
            ("Phase 3 - Lateral Movement & Objective Achievement", "Privilege escalation; lateral movement; crown-jewel access; objective attainment", "2 weeks", "Attack path documentation; objective achievement evidence"),
            ("Phase 4 - Purple Team Debrief & Reporting", "Campaign report; MITRE ATT&CK mapping; detection assessment; purple team debrief session", "1 week", "Red Team campaign report; ATT&CK mapping; detection and response assessment; strategic recommendations"),
        ],
    },
    "Source_Code_Review": {
        "methodology": [
            "Phase 1 - Scoping & Codebase Onboarding: SecureITLab confirms the application components and code repositories in scope, establishes secure access to the codebase, and reviews supporting documentation (architecture diagrams, threat models, previous findings) to focus review effort.",
            "Phase 2 - Automated SAST Scanning: Industry-standard static analysis security testing (SAST) tools are configured and run against the codebase to identify common vulnerability patterns, insecure coding practices, and dependency risks.",
            "Phase 3 - Manual Code Review: SecureITLab's security engineers perform targeted manual review of high-risk code areas (authentication, cryptography, input handling, session management, third-party integrations) against OWASP ASVS and SANS Top 25 standards.",
            "Phase 4 - Reporting & Developer Guidance: A source code review report is produced detailing vulnerabilities with code references, severity ratings, and remediation recommendations including corrected code samples. Developer guidance notes and a debrief session are provided.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & Codebase Onboarding", "Scope confirmation; secure repository access; documentation review; SAST tool configuration", "2 days", "Scoping document; repository access confirmation"),
            ("Phase 2 - Automated SAST Scanning", "SAST tool execution; scan result triage; false positive filtering; preliminary findings", "3 days", "SAST scan results; triaged findings list"),
            ("Phase 3 - Manual Code Review", "High-risk area manual review; OWASP ASVS / SANS Top 25 alignment; finding validation", "2 weeks", "Manual review notes; validated vulnerability catalogue with code references"),
            ("Phase 4 - Reporting & Developer Guidance", "Report drafting; code samples; developer guidance notes; debrief session", "3 days", "Source code review report; remediation recommendations with code samples; developer guidance notes"),
        ],
    },
    "Table_Top_Exercise": {
        "methodology": [
            "Phase 1 - Exercise Design & Scenario Development: SecureITLab works with the client to define exercise objectives, select realistic incident scenarios (e.g., ransomware, data breach, supply chain attack), and design inject sequences and decision points tailored to the organisation's context and incident response maturity.",
            "Phase 2 - Pre-Exercise Briefing & Preparation: Participants are briefed on exercise format, ground rules, and roles. Exercise materials including scenario packs and inject schedules are finalised. Facilitators and observers are briefed.",
            "Phase 3 - Exercise Facilitation: SecureITLab facilitates the live tabletop exercise, managing inject delivery, participant engagement, and timeline. Observers document decision points, response actions, gaps, and communication breakdowns in real time.",
            "Phase 4 - Post-Exercise Review & Reporting: A post-exercise findings report is produced identifying strengths, gaps, and improvement areas in the incident response plan. Prioritised recommendations are provided.",
        ],
        "timeline": [
            ("Phase 1 - Exercise Design & Scenario Development", "Objectives alignment; scenario selection; inject sequence design; exercise materials development", "1 week", "Exercise design document; scenario pack; inject schedule"),
            ("Phase 2 - Pre-Exercise Briefing & Preparation", "Participant briefing; role assignment; final materials preparation; facilitator briefing", "3 days", "Briefing notes; participant guide; final exercise materials"),
            ("Phase 3 - Exercise Facilitation", "Live tabletop facilitation; inject delivery; real-time observation and note-taking", "1 day", "Observation notes; decision log; real-time findings"),
            ("Phase 4 - Post-Exercise Review & Reporting", "Findings consolidation; report drafting; improvement roadmap; debrief presentation", "3 days", "Post-exercise findings report; improvement recommendations; roadmap"),
        ],
    },
    "Vulnerability_Assessment": {
        "methodology": [
            "Phase 1 - Scoping & Asset Enumeration: SecureITLab confirms the asset scope (IP ranges, hostnames, cloud resources), obtains authenticated scanning credentials, and validates network connectivity to ensure comprehensive coverage.",
            "Phase 2 - Authenticated Vulnerability Scanning: Credentialed scans are executed using industry-leading tools (Nessus, Qualys, or equivalent) across all in-scope assets. Scan configurations are optimised to minimise operational impact while maximising detection coverage.",
            "Phase 3 - Findings Analysis & Risk Rating: Raw scan results are analysed, false positives are removed, and findings are risk-rated using CVSS scores and contextual factors (asset criticality, exploitability, compensating controls). A prioritised vulnerability list is produced.",
            "Phase 4 - Reporting & Remediation Guidance: A vulnerability assessment report with an executive summary, prioritised findings, and a remediation action plan is produced and presented. Guidance on patch management and compensating controls is provided.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & Asset Enumeration", "Asset scope confirmation; credential provisioning; scan configuration; connectivity validation", "2 days", "Scoping document; asset list; scan configuration record"),
            ("Phase 2 - Authenticated Vulnerability Scanning", "Credentialed scanning across all in-scope assets; scan result collection", "3 days", "Authenticated scan reports; raw results"),
            ("Phase 3 - Findings Analysis & Risk Rating", "False positive removal; CVSS scoring; contextual risk rating; prioritised findings list", "3 days", "Prioritised vulnerability list; risk-rated findings"),
            ("Phase 4 - Reporting & Remediation Guidance", "Report drafting; remediation action plan; executive summary; client presentation", "2 days", "Vulnerability assessment report; remediation action plan; executive summary"),
        ],
    },
    "Web_Application_Testing": {
        "methodology": [
            "Phase 1 - Scoping & Reconnaissance: SecureITLab confirms the web application(s) and functional areas in scope, establishes test accounts, and conducts application reconnaissance to map functionality, authentication mechanisms, and data flows prior to testing.",
            "Phase 2 - Automated Scanning & Manual Testing: Automated web application scanners are deployed for baseline coverage. Manual testing is performed against the OWASP Top 10, including injection, broken authentication, IDOR, SSRF, security misconfigurations, and business logic flaws.",
            "Phase 3 - Exploitation & Evidence Capture: Confirmed vulnerabilities are exploited in a controlled manner to demonstrate impact. Proof-of-concept payloads, screenshots, and HTTP request/response captures are documented as evidence.",
            "Phase 4 - Reporting & Remediation Guidance: A web application test report with CVSS-scored findings, PoC evidence, and remediation guidance is produced and presented to development and security stakeholders.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & Reconnaissance", "Scope confirmation; test account setup; application mapping; functionality review", "3 days", "Scoping document; application map; test account confirmation"),
            ("Phase 2 - Automated Scanning & Manual Testing", "Automated scanning; OWASP Top 10 manual testing; business logic assessment", "2 weeks", "Testing notes; preliminary findings log"),
            ("Phase 3 - Exploitation & Evidence Capture", "Vulnerability confirmation; controlled exploitation; PoC payload capture; HTTP evidence", "3 days", "PoC evidence package; exploitation notes"),
            ("Phase 4 - Reporting & Remediation Guidance", "Report drafting; CVSS scoring; remediation guidance; client debrief", "3 days", "Web application test report; CVSS-scored findings; remediation guidance"),
        ],
    },
    "Application_Audit": {
        "methodology": [
            "Phase 1 - Audit Planning & Risk Assessment: SecureITLab prepares the audit plan, defines the control framework (COBIT, ISO 27001, or internal standards), performs a preliminary risk assessment of application controls, and agrees the fieldwork schedule with the client.",
            "Phase 2 - Control Design Assessment: The design of key application controls (access management, change management, data integrity, interface security) is evaluated to determine whether controls are suitably designed to mitigate identified risks.",
            "Phase 3 - Control Operating Effectiveness Testing: Testing is performed to assess whether controls are operating as designed over the audit period. Evidence is collected through inspection, enquiry, observation, and re-performance.",
            "Phase 4 - Reporting & Management Action Plan: An application audit report with findings rated by severity, exceptions, and recommendations is produced. A management action plan template is provided for tracking remediation.",
        ],
        "timeline": [
            ("Phase 1 - Audit Planning & Risk Assessment", "Audit plan preparation; risk assessment; control framework selection; fieldwork scheduling", "1 week", "Audit plan; risk assessment; fieldwork schedule"),
            ("Phase 2 - Control Design Assessment", "Control design walkthroughs; documentation review; design gap identification", "1 week", "Control design assessment workbook; design gap register"),
            ("Phase 3 - Control Operating Effectiveness Testing", "Evidence collection; testing via inspection, enquiry, re-performance; exception identification", "1 week", "Control testing workpapers; evidence pack; exceptions list"),
            ("Phase 4 - Reporting & Management Action Plan", "Audit report drafting; finding ratings; recommendations; management action plan template", "1 week", "Application audit report; management action plan template"),
        ],
    },
    "Cloud_Infrastructure_Audit": {
        "methodology": [
            "Phase 1 - Audit Planning & Environment Discovery: SecureITLab defines the cloud audit scope (AWS, Azure, GCP, or multi-cloud), maps the cloud environment including accounts, subscriptions, services, and regions, and prepares a risk-based audit plan.",
            "Phase 2 - Configuration & Access Control Review: Cloud environment configurations are reviewed against CIS Cloud Benchmarks and provider best-practice baselines. Identity and access management, network security groups, storage permissions, encryption settings, and logging configurations are assessed.",
            "Phase 3 - Control Testing & Evidence Collection: Findings are tested and confirmed through automated cloud security posture management (CSPM) tooling and manual review. Evidence is documented per finding with risk ratings.",
            "Phase 4 - Reporting & Recommendations: A cloud audit report with misconfiguration findings, risk ratings, a cloud security posture dashboard, and prioritised remediation recommendations is produced and presented.",
        ],
        "timeline": [
            ("Phase 1 - Audit Planning & Environment Discovery", "Scope definition; cloud environment mapping; risk-based audit plan; read-only access provisioning", "1 week", "Audit plan; cloud environment map; asset inventory"),
            ("Phase 2 - Configuration & Access Control Review", "CIS Benchmark assessment; IAM review; network and storage configuration review; logging audit", "1 week", "Configuration review workbook; IAM findings; preliminary findings list"),
            ("Phase 3 - Control Testing & Evidence Collection", "CSPM tooling; manual validation; finding confirmation; risk rating; evidence documentation", "1 week", "Control testing evidence; confirmed findings list; risk-rated workbook"),
            ("Phase 4 - Reporting & Recommendations", "Audit report drafting; posture dashboard; remediation recommendations; client presentation", "1 week", "Cloud audit report; security posture dashboard; remediation recommendations"),
        ],
    },
    "Internal_Audit_Support": {
        "methodology": [
            "Phase 1 - Planning & Audit Programme Development: SecureITLab works alongside the internal audit team to develop the IT and cybersecurity audit programme, including risk assessments, audit universe mapping, control framework selection, and individual audit planning documents.",
            "Phase 2 - Fieldwork Support & Work-Paper Preparation: SecureITLab provides specialist resource to support fieldwork execution, including control testing, evidence collection, and preparation of structured work-papers to audit standards.",
            "Phase 3 - Quality Assurance Review: Completed fieldwork and draft reports are subject to a quality assurance review by SecureITLab's senior consultants to ensure accuracy, consistency, and alignment with the agreed audit standards.",
            "Phase 4 - Reporting & Follow-Up Support: Final audit reports are produced in alignment with the client's internal audit reporting format. A follow-up tracking template is provided to support management action plan monitoring.",
        ],
        "timeline": [
            ("Phase 1 - Planning & Audit Programme Development", "Risk assessment; audit universe mapping; audit planning documents; framework selection", "1 week", "Audit programme; audit planning documents; risk assessment"),
            ("Phase 2 - Fieldwork Support & Work-Paper Preparation", "Control testing; evidence collection; work-paper preparation; specialist advisory", "2 weeks", "Fieldwork work-papers; evidence packs; testing documentation"),
            ("Phase 3 - Quality Assurance Review", "Work-paper review; draft report review; accuracy and consistency checks; feedback incorporation", "1 week", "QA review notes; revised work-papers; draft audit report"),
            ("Phase 4 - Reporting & Follow-Up Support", "Final report production; management action plan template; follow-up tracking setup", "1 week", "Final audit reports; follow-up tracking template"),
        ],
    },
    "IT_System_Audit": {
        "methodology": [
            "Phase 1 - Audit Planning & ITGC Scoping: SecureITLab prepares a risk-based IT audit plan, scopes the IT general controls (ITGCs) domains (change management, access control, operations, IT governance), and agrees the testing approach and fieldwork schedule.",
            "Phase 2 - Control Design Evaluation: The design adequacy of ITGCs across each domain is assessed through document reviews, process walkthroughs, and enquiries with IT process owners to determine whether controls are suitably designed to prevent or detect errors.",
            "Phase 3 - Operating Effectiveness Testing: Controls are tested over the audit period through inspection of evidence, re-performance, and observation. Exceptions and deviations are identified and risk-rated.",
            "Phase 4 - Reporting & Management Response: An IT system audit report with findings, severity ratings, and recommendations is produced. An action tracking register is provided for management to record and monitor agreed remediation actions.",
        ],
        "timeline": [
            ("Phase 1 - Audit Planning & ITGC Scoping", "Risk-based planning; ITGC domain scoping; testing approach; fieldwork scheduling", "1 week", "IT audit plan; ITGC scope document; fieldwork schedule"),
            ("Phase 2 - Control Design Evaluation", "Process walkthroughs; document review; design gap identification; stakeholder enquiries", "1 week", "Control design assessment workbook; design findings"),
            ("Phase 3 - Operating Effectiveness Testing", "Control testing; evidence collection; exception identification; risk rating", "1 week", "Control testing workpapers; evidence pack; exceptions list"),
            ("Phase 4 - Reporting & Management Response", "Audit report drafting; finding ratings; management recommendations; action tracking register", "1 week", "IT system audit report; management recommendations; action tracking register"),
        ],
    },
    "Third_Party_Audit": {
        "methodology": [
            "Phase 1 - Supplier Profiling & Audit Planning: SecureITLab profiles the supplier(s) to be audited, assesses inherent risk based on services provided and data access, and prepares a risk-based audit plan including control framework and evidence requirements.",
            "Phase 2 - Questionnaire Issue & Document Review: A tailored security and compliance questionnaire is issued to the supplier. Responses and supporting documentation (policies, certifications, audit reports) are reviewed and preliminary gaps are identified.",
            "Phase 3 - On-Site or Remote Audit Fieldwork: An on-site or virtual audit is conducted to validate questionnaire responses, test controls, interview key personnel, and collect evidence. Findings are risk-rated and documented.",
            "Phase 4 - Reporting & Supplier Action Plan: A third-party audit report with a supplier risk scorecard, findings, observations, and recommendations is produced. A supplier action-plan template is provided to track agreed remediation.",
        ],
        "timeline": [
            ("Phase 1 - Supplier Profiling & Audit Planning", "Supplier risk profiling; inherent risk assessment; audit plan preparation; control framework selection", "1 week", "Supplier risk profile; audit plan"),
            ("Phase 2 - Questionnaire Issue & Document Review", "Questionnaire issuance; response review; documentation review; preliminary gap identification", "1 week", "Completed questionnaire; document review notes; preliminary findings"),
            ("Phase 3 - On-Site or Remote Audit Fieldwork", "Control testing; personnel interviews; evidence collection; finding validation and risk-rating", "1 week", "Fieldwork workpapers; evidence pack; confirmed findings list"),
            ("Phase 4 - Reporting & Supplier Action Plan", "Audit report; supplier risk scorecard; recommendations; action-plan template", "1 week", "Third-party audit report; supplier risk scorecard; supplier action-plan template"),
        ],
    },
    "ISO_20000-2018_IT_Service_Management_System": {
        "methodology": [
            "Phase 1 - Gap Assessment: SecureITLab conducts a comprehensive gap assessment of the organisation's existing IT service management processes against the ISO/IEC 20000-1:2018 requirements. Gaps are documented, risk-rated, and prioritised to inform the implementation plan.",
            "Phase 2 - Process Design & Documentation: ITSM processes and procedures are designed or refined to meet ISO 20000-1 requirements, including service planning, delivery, relationship management, and control processes. An SMS documentation suite is developed.",
            "Phase 3 - Implementation & Internal Audit: Process implementations are supported through stakeholder engagement, training, and evidence collection. An internal audit programme is executed against the implemented SMS to verify conformance.",
            "Phase 4 - Certification Readiness & Pre-Audit: A pre-certification review is conducted to assess SMS readiness against ISO 20000-1 requirements. Outstanding gaps are closed and the organisation is prepared for the external certification audit.",
        ],
        "timeline": [
            ("Phase 1 - Gap Assessment", "ISO 20000-1 gap assessment; findings documentation; risk rating; prioritised implementation plan", "2 weeks", "SMS gap assessment report; prioritised implementation plan"),
            ("Phase 2 - Process Design & Documentation", "ITSM process design; documentation drafting; stakeholder review; SMS documentation suite", "4 weeks", "SMS documentation suite; process designs; SOPs"),
            ("Phase 3 - Implementation & Internal Audit", "Process implementation support; training; evidence collection; internal audit execution", "4 weeks", "Internal audit report; evidence pack; non-conformity register"),
            ("Phase 4 - Certification Readiness & Pre-Audit", "Pre-certification review; gap closure; corrective actions; certification audit preparation", "2 weeks", "Certification readiness report; closed non-conformities; audit preparation pack"),
        ],
    },
    "ISO_22301-2019_Business_Continuity_Management_System": {
        "methodology": [
            "Phase 1 - Business Impact Analysis & Risk Assessment: SecureITLab performs a Business Impact Analysis (BIA) to identify critical business functions, maximum tolerable periods of disruption (MTPD), recovery time objectives (RTO), and recovery point objectives (RPO). A business continuity risk assessment is conducted in parallel.",
            "Phase 2 - BCP & DRP Development: Business Continuity Plans and Disaster Recovery Plans are developed based on BIA and risk assessment findings, covering crisis management, business function recovery, IT recovery, and communication procedures.",
            "Phase 3 - Testing & Exercising: BCPs and DRPs are validated through structured testing and exercising activities (tabletop, functional, or full interruption exercises as agreed). Exercise results are documented and plans are updated accordingly.",
            "Phase 4 - Internal Audit & Certification Readiness: An internal audit of the BCMS is conducted against ISO 22301:2019 requirements. A certification readiness report is produced and outstanding gaps are addressed in preparation for the external audit.",
        ],
        "timeline": [
            ("Phase 1 - Business Impact Analysis & Risk Assessment", "BIA workshops; MTPD/RTO/RPO determination; BC risk assessment; criticality prioritisation", "3 weeks", "BIA report; business continuity risk assessment"),
            ("Phase 2 - BCP & DRP Development", "Plan development; crisis management procedures; IT recovery playbooks; communication plans", "4 weeks", "Business Continuity Plan; Disaster Recovery Plan; crisis management procedures"),
            ("Phase 3 - Testing & Exercising", "Exercise design; tabletop or functional testing; results documentation; plan updates", "3 weeks", "Exercise programme; exercise results report; updated BCP/DRP"),
            ("Phase 4 - Internal Audit & Certification Readiness", "BCMS internal audit; non-conformity resolution; certification readiness review", "2 weeks", "Internal audit report; certification readiness report; corrective action register"),
        ],
    },
    "ISO_27001-2022_Information_Security_Management_System": {
        "methodology": [
            "Phase 1 - Gap Assessment & ISMS Scoping: SecureITLab performs a structured gap assessment against ISO/IEC 27001:2022 clause requirements and Annex A controls. The ISMS scope is defined, context of the organisation is documented, and an implementation roadmap is produced.",
            "Phase 2 - Risk Assessment & Statement of Applicability: An information security risk assessment is conducted using an agreed methodology (aligned to ISO 27005). A risk treatment plan is developed and the Statement of Applicability (SoA) is produced, documenting control selection and justifications.",
            "Phase 3 - Policy, Control & ISMS Documentation: The full ISMS documentation suite is developed including policies, procedures, guidelines, and records. Selected Annex A controls are implemented with supporting evidence and operational processes established.",
            "Phase 4 - Internal Audit, Management Review & Certification Readiness: An internal ISMS audit is conducted and a management review is facilitated. Non-conformities are resolved and the organisation is prepared for the Stage 1 and Stage 2 external certification audits.",
        ],
        "timeline": [
            ("Phase 1 - Gap Assessment & ISMS Scoping", "Clause-by-clause gap assessment; scope definition; context documentation; implementation roadmap", "2 weeks", "Gap assessment report; ISMS scope document; implementation roadmap"),
            ("Phase 2 - Risk Assessment & Statement of Applicability", "Asset-based risk assessment; risk treatment planning; SoA development; control justifications", "3 weeks", "Risk assessment report; risk treatment plan; Statement of Applicability"),
            ("Phase 3 - Policy, Control & ISMS Documentation", "Policy drafting; Annex A control implementation; evidence collection; ISMS documentation suite", "6 weeks", "ISMS documentation suite; control implementation evidence; operational procedures"),
            ("Phase 4 - Internal Audit, Management Review & Certification Readiness", "Internal audit; management review facilitation; non-conformity closure; certification prep", "3 weeks", "Internal audit report; management review minutes; certification readiness report"),
        ],
    },
    "ISO_27017-2015_Cloud_Security_Controls": {
        "methodology": [
            "Phase 1 - Cloud Environment Assessment & Gap Analysis: SecureITLab assesses the organisation's cloud environment against ISO/IEC 27017:2015 supplemental controls, identifying gaps in existing cloud security practices for both cloud service customers and providers.",
            "Phase 2 - Control Design & SoA Update: Cloud-specific controls are designed or adapted, and the Statement of Applicability is updated to incorporate ISO 27017 supplemental controls with justifications for inclusion or exclusion.",
            "Phase 3 - Control Implementation & Evidence Collection: Selected ISO 27017 controls are implemented across cloud environments and supporting services. Evidence of control operation is collected and documented.",
            "Phase 4 - Internal Review & Certification Readiness: An internal review is conducted to verify compliance with ISO 27017 requirements. A certification readiness report is produced and outstanding gaps are resolved.",
        ],
        "timeline": [
            ("Phase 1 - Cloud Environment Assessment & Gap Analysis", "Cloud security review; ISO 27017 gap assessment; finding documentation; risk rating", "2 weeks", "Cloud security gap assessment report (ISO 27017)"),
            ("Phase 2 - Control Design & SoA Update", "Cloud control design; SoA update; justification documentation", "2 weeks", "Control design specifications; updated SoA (ISO 27017 supplemental controls)"),
            ("Phase 3 - Control Implementation & Evidence Collection", "Control implementation; cloud configuration; evidence documentation; stakeholder engagement", "3 weeks", "Control implementation evidence; cloud security configuration records"),
            ("Phase 4 - Internal Review & Certification Readiness", "Internal review; gap closure; corrective actions; certification preparation", "1 week", "Certification readiness report; closed findings register"),
        ],
    },
    "ISO_27018-2019_Protection_of_PII_in_Public_Clouds": {
        "methodology": [
            "Phase 1 - PII Processing Discovery & Gap Assessment: SecureITLab maps PII processing activities within public cloud environments and assesses existing controls against ISO/IEC 27018:2019 requirements, identifying gaps in consent management, data minimisation, and transparency obligations.",
            "Phase 2 - Control Design & Contractual Review: PII protection controls are designed for cloud environments and existing contractual arrangements (data processing agreements, cloud service agreements) are reviewed for ISO 27018 compliance clauses.",
            "Phase 3 - Control Implementation & Documentation: Selected ISO 27018 controls are implemented and documented. Privacy notices and contractual clauses are updated to reflect ISO 27018 obligations.",
            "Phase 4 - Certification Readiness Review: A readiness review is conducted against ISO 27018 requirements and a certification readiness report is produced. Outstanding non-conformities are resolved prior to external audit.",
        ],
        "timeline": [
            ("Phase 1 - PII Processing Discovery & Gap Assessment", "PII mapping in cloud; ISO 27018 gap assessment; control inventory; gap documentation", "2 weeks", "PII controls gap assessment report (ISO 27018); PII processing map"),
            ("Phase 2 - Control Design & Contractual Review", "PII control design; DPA and contract review; ISO 27018 clause recommendations", "2 weeks", "PII control implementation plan; contractual review findings; updated clause recommendations"),
            ("Phase 3 - Control Implementation & Documentation", "Control implementation; privacy notice updates; documentation; evidence collection", "3 weeks", "Implemented controls evidence; updated privacy notices; contractual clause updates"),
            ("Phase 4 - Certification Readiness Review", "Readiness assessment; non-conformity closure; certification preparation", "1 week", "Certification readiness report; closed findings register"),
        ],
    },
    "ISO_27701-2019_Privacy_Information_Management_System": {
        "methodology": [
            "Phase 1 - PIMS Gap Assessment & Scoping: SecureITLab assesses the organisation's existing ISMS against ISO/IEC 27701:2019 extension requirements for both PII controllers and processors. Gaps are documented and a PIMS implementation roadmap is produced.",
            "Phase 2 - Privacy Controls Design & SoA Extension: PIMS-specific privacy controls (Annex B and C) are designed and mapped to data processing activities. The SoA is extended to incorporate 27701 controls with appropriate justifications.",
            "Phase 3 - Controls Implementation & Documentation: Privacy controls are implemented within existing ISMS processes. Privacy-specific policies, procedures, and records are developed. Evidence of control operation is collected.",
            "Phase 4 - Internal Audit & Certification Readiness: An internal PIMS audit is conducted and non-conformities are resolved. A certification readiness report is produced to prepare the organisation for external PIMS certification.",
        ],
        "timeline": [
            ("Phase 1 - PIMS Gap Assessment & Scoping", "ISO 27701 gap assessment; PIMS scoping; PII controller/processor determination; roadmap", "2 weeks", "PIMS gap assessment report; implementation roadmap"),
            ("Phase 2 - Privacy Controls Design & SoA Extension", "Annex B/C control design; PII processing activity mapping; SoA extension and justifications", "2 weeks", "Privacy controls design; extended SoA (ISO 27701)"),
            ("Phase 3 - Controls Implementation & Documentation", "Privacy control implementation; policy and procedure development; evidence collection", "4 weeks", "PIMS documentation suite; control implementation evidence; privacy records"),
            ("Phase 4 - Internal Audit & Certification Readiness", "Internal PIMS audit; non-conformity resolution; certification readiness review", "2 weeks", "Internal audit report; certification readiness report; closed non-conformities"),
        ],
    },
    "ISO_42001-2023_AI_Management_System": {
        "methodology": [
            "Phase 1 - AI Landscape & Risk Assessment: SecureITLab maps the organisation's AI systems, use cases, and data assets. An AI risk and impact assessment is conducted to identify risks arising from AI development, deployment, and use, including bias, transparency, and safety concerns.",
            "Phase 2 - AIMS Framework Design & Documentation: An AI Management System framework is designed aligned to ISO/IEC 42001:2023, including AI governance principles, risk treatment processes, responsible AI policies, and role and responsibility definitions.",
            "Phase 3 - Governance & Control Implementation: AIMS controls and governance mechanisms are implemented across AI development and operational processes. Supporting documentation, evidence records, and monitoring processes are established.",
            "Phase 4 - Internal Audit & Certification Readiness: An internal AIMS audit is conducted to verify conformance with ISO 42001 requirements. Findings are resolved and a certification readiness report is produced for external audit preparation.",
        ],
        "timeline": [
            ("Phase 1 - AI Landscape & Risk Assessment", "AI system inventory; use case mapping; AI risk and impact assessment; gap identification", "2 weeks", "AI landscape map; AI risk and impact assessment report"),
            ("Phase 2 - AIMS Framework Design & Documentation", "Framework design; AI governance policy; risk treatment process; AIMS documentation suite", "3 weeks", "AIMS framework; AI governance policy framework; AIMS documentation suite"),
            ("Phase 3 - Governance & Control Implementation", "Control implementation; evidence collection; monitoring process setup; stakeholder engagement", "3 weeks", "Implemented AI controls; governance records; monitoring procedures"),
            ("Phase 4 - Internal Audit & Certification Readiness", "Internal AIMS audit; non-conformity resolution; certification readiness review", "2 weeks", "Internal audit report; certification readiness report; corrective action register"),
        ],
    },
    "Designing_Security_Organization": {
        "methodology": [
            "Phase 1 - Current State Assessment & Benchmarking: SecureITLab assesses the existing security organisation structure, roles, and capabilities, benchmarking against industry models (e.g., NIST, CIS) and peer organisations of similar size and risk profile.",
            "Phase 2 - Org Design & Role Profiling: An optimised security organisation design is developed, defining the recommended structure, reporting lines, team composition, and staffing model. Detailed role profiles and job descriptions are produced for each position.",
            "Phase 3 - RACI & Operating Model Development: A comprehensive RACI matrix is developed across security domains, and the security operating model is documented including collaboration mechanisms with IT, legal, risk, and business units.",
            "Phase 4 - Transition Planning & Handover: A transition and change management plan is developed to guide implementation of the new structure. A handover session is conducted with senior stakeholders.",
        ],
        "timeline": [
            ("Phase 1 - Current State Assessment & Benchmarking", "Current structure review; capability assessment; benchmarking; gap identification", "2 weeks", "Current state assessment; benchmarking report"),
            ("Phase 2 - Org Design & Role Profiling", "Structure design; reporting line definition; role profiling; job descriptions", "3 weeks", "Security org-design blueprint; role profiles; job descriptions"),
            ("Phase 3 - RACI & Operating Model Development", "RACI matrix development; operating model documentation; collaboration framework", "2 weeks", "RACI matrix; security operating model"),
            ("Phase 4 - Transition Planning & Handover", "Transition plan; change management guidance; stakeholder presentation; handover", "1 week", "Transition and change management plan; executive presentation"),
        ],
    },
    "Information_Security_Governance": {
        "methodology": [
            "Phase 1 - Governance Maturity Assessment: SecureITLab assesses the current information security governance maturity against recognised frameworks (COBIT, ISO 27014), identifying gaps in strategy, committee structures, policy frameworks, and performance measurement.",
            "Phase 2 - Framework & Committee Design: An IS governance framework is designed encompassing the governance hierarchy, security committee structure, terms of reference, decision-making authority, and escalation pathways.",
            "Phase 3 - Policy Development & KPI Definition: The policy hierarchy is established and key governance policies are drafted. A governance KPI dashboard is designed to enable ongoing monitoring and reporting of security programme performance.",
            "Phase 4 - Implementation Support & Handover: SecureITLab supports initial governance meetings, reviews, and reporting cycles. The completed framework is formally handed over with implementation guidance and a governance calendar.",
        ],
        "timeline": [
            ("Phase 1 - Governance Maturity Assessment", "Maturity assessment against frameworks; stakeholder interviews; gap identification; prioritisation", "2 weeks", "Governance maturity assessment; gap register"),
            ("Phase 2 - Framework & Committee Design", "Governance hierarchy design; committee structure; TOR drafting; authority matrix", "3 weeks", "IS governance framework; committee charter; TOR documents"),
            ("Phase 3 - Policy Development & KPI Definition", "Policy hierarchy development; key policy drafting; KPI catalogue; dashboard design", "3 weeks", "Policy hierarchy; key governance policies; KPI dashboard design"),
            ("Phase 4 - Implementation Support & Handover", "Initial meeting support; reporting cycle; framework handover; governance calendar", "2 weeks", "Approved IS governance framework; KPI dashboard; governance calendar; implementation guide"),
        ],
    },
    "Security_Operations_Services": {
        "methodology": [
            "Phase 1 - Current State SOC Assessment: SecureITLab assesses the existing security operations capability including tools, processes, staffing, and performance metrics, identifying gaps against a target operating model and best practice frameworks.",
            "Phase 2 - Operating Model Design: A SOC operating model is designed covering organisational structure, tier structure, shift patterns, escalation processes, tooling architecture (SIEM, SOAR, threat intelligence), and performance management.",
            "Phase 3 - Use-Case & Playbook Development: Detection use-cases are developed and mapped to MITRE ATT&CK. Incident response playbooks are created for priority threat scenarios, including triage, containment, eradication, and recovery steps.",
            "Phase 4 - Validation, KPI Framework & Handover: The designed operating model and use-cases are validated with the security team. A KPI framework for measuring SOC performance is established and the full package is formally handed over.",
        ],
        "timeline": [
            ("Phase 1 - Current State SOC Assessment", "Tooling and process review; staffing assessment; performance metric review; gap identification", "2 weeks", "Current state SOC assessment report; gap register"),
            ("Phase 2 - Operating Model Design", "SOC structure design; tooling architecture; shift model; escalation process; stakeholder review", "3 weeks", "SOC operating model design document"),
            ("Phase 3 - Use-Case & Playbook Development", "MITRE ATT&CK mapping; detection use-case design; IR playbook development; review cycles", "4 weeks", "Detection use-case catalogue; incident response playbooks"),
            ("Phase 4 - Validation, KPI Framework & Handover", "Operating model validation; KPI framework; handover session; implementation guidance", "1 week", "Validated SOC operating model; KPI framework; handover package"),
        ],
    },
    "Strategy_and_Business_Alignment": {
        "methodology": [
            "Phase 1 - Discovery & Stakeholder Interviews: SecureITLab conducts structured interviews with C-suite, IT, risk, legal, and business unit leaders to understand strategic priorities, risk appetite, regulatory obligations, and cybersecurity pain points.",
            "Phase 2 - Current State & Gap Analysis: The organisation's existing cybersecurity posture is assessed against business objectives and the target state, producing a structured gap analysis that informs strategic priorities.",
            "Phase 3 - Strategy Development & Roadmap: A multi-year cybersecurity strategy is developed, including vision, guiding principles, strategic pillars, and a prioritised 3-5 year initiative roadmap with resource and investment implications.",
            "Phase 4 - Validation & Executive Presentation: The strategy and roadmap are validated with senior leadership and a Board-level presentation pack is produced. Final strategy documents are delivered and a handover is conducted.",
        ],
        "timeline": [
            ("Phase 1 - Discovery & Stakeholder Interviews", "C-suite and stakeholder interviews; risk appetite workshops; regulatory requirement mapping", "2 weeks", "Discovery notes; stakeholder interview summaries; risk appetite statement"),
            ("Phase 2 - Current State & Gap Analysis", "Posture assessment; business alignment mapping; gap analysis; strategic priority identification", "2 weeks", "Current state assessment; gap analysis; business alignment map"),
            ("Phase 3 - Strategy Development & Roadmap", "Strategy document drafting; initiative roadmap; investment implications; resource planning", "3 weeks", "Cybersecurity strategy document; 3-5 year strategic roadmap"),
            ("Phase 4 - Validation & Executive Presentation", "Senior leadership review; Board presentation pack; final revisions; strategy handover", "1 week", "Approved strategy document; Board-level presentation pack"),
        ],
    },
    "Data_Cataloging_and_Metadata_Management": {
        "methodology": [
            "Phase 1 - Requirements & Tool Assessment: SecureITLab gathers requirements from data consumers, stewards, and IT teams, and assesses the suitability of existing or candidate data catalogue tools against defined criteria.",
            "Phase 2 - Catalogue Design & Taxonomy Development: The data catalogue architecture, business glossary structure, metadata standards, and data domain taxonomy are designed in collaboration with stakeholders.",
            "Phase 3 - Implementation & Data Onboarding: The data catalogue is configured and deployed. Priority data assets are onboarded, lineage maps are established, and metadata is populated and validated.",
            "Phase 4 - Testing, Training & Handover: The catalogue is tested for completeness and usability. Training sessions are delivered to data stewards and consumers. The solution is formally handed over with operational documentation.",
        ],
        "timeline": [
            ("Phase 1 - Requirements & Tool Assessment", "Stakeholder requirements gathering; tool assessment; selection criteria definition; gap analysis", "2 weeks", "Requirements document; tool assessment report; recommendation"),
            ("Phase 2 - Catalogue Design & Taxonomy Development", "Catalogue architecture design; business glossary; taxonomy and metadata standards", "3 weeks", "Data catalogue design; business glossary; metadata standards; taxonomy"),
            ("Phase 3 - Implementation & Data Onboarding", "Catalogue configuration; data asset onboarding; lineage mapping; metadata population", "4 weeks", "Deployed data catalogue; lineage maps; populated business glossary"),
            ("Phase 4 - Testing, Training & Handover", "Usability testing; steward and consumer training; operational documentation; formal handover", "1 week", "Test results; training materials; operational guide; handover record"),
        ],
    },
    "Data_Governance_Audits_and_Assessments": {
        "methodology": [
            "Phase 1 - Audit Planning & Framework Review: SecureITLab defines the data governance audit scope, selects the applicable assessment framework (DAMA-DMBOK, DCAM, or internal standards), and prepares the audit plan and evidence request list.",
            "Phase 2 - Evidence Collection & Stakeholder Interviews: Governance documentation, policies, committee minutes, and process records are collected and reviewed. Interviews are conducted with data owners, stewards, and governance council members.",
            "Phase 3 - Gap Analysis & Maturity Scoring: Assessment findings are analysed against the governance framework. Maturity scores are assigned per governance dimension, and gaps are risk-rated and prioritised.",
            "Phase 4 - Reporting & Management Action Plan: A data governance audit report with maturity scorecard, findings, recommendations, and a management action plan template is produced and presented.",
        ],
        "timeline": [
            ("Phase 1 - Audit Planning & Framework Review", "Scope definition; framework selection; audit plan; evidence request list", "1 week", "Audit plan; evidence request list; framework mapping"),
            ("Phase 2 - Evidence Collection & Stakeholder Interviews", "Document collection; governance record review; stakeholder interviews; process walkthroughs", "2 weeks", "Evidence log; interview notes; process documentation"),
            ("Phase 3 - Gap Analysis & Maturity Scoring", "Maturity scoring; gap analysis; risk-rating; prioritisation", "1 week", "Maturity scorecard; gap analysis workbook; risk-rated findings"),
            ("Phase 4 - Reporting & Management Action Plan", "Audit report drafting; management action plan template; stakeholder presentation", "1 week", "Data governance audit report; maturity scorecard; management action plan template"),
        ],
    },
    "Data_Governance_Strategy_and_Framework_Development": {
        "methodology": [
            "Phase 1 - Discovery & Current State Assessment: SecureITLab assesses the organisation's current data governance maturity, data landscape, regulatory obligations, and strategic data priorities through stakeholder interviews and documentation reviews.",
            "Phase 2 - Strategy & Framework Design: A data governance strategy is developed setting out vision, principles, and objectives. The governance framework is designed covering operating model, committee structures, policies, standards, and processes.",
            "Phase 3 - Governance Operating Model Development: The governance operating model is elaborated, including council/committee charters, data domain accountabilities, decision rights, and escalation mechanisms. A data governance roadmap is produced.",
            "Phase 4 - Roadmap Finalisation & Stakeholder Presentation: The strategy, framework, and roadmap are finalised following stakeholder feedback. A formal presentation is made to the data governance council or senior leadership.",
        ],
        "timeline": [
            ("Phase 1 - Discovery & Current State Assessment", "Stakeholder interviews; maturity assessment; data landscape review; regulatory mapping", "2 weeks", "Current state assessment; maturity findings; discovery report"),
            ("Phase 2 - Strategy & Framework Design", "Strategy development; framework design; operating model; policy architecture", "3 weeks", "Data governance strategy document; framework design"),
            ("Phase 3 - Governance Operating Model Development", "Council charter; domain accountabilities; decision rights; escalation model; roadmap", "2 weeks", "Council/committee charter; governance roadmap; operating model"),
            ("Phase 4 - Roadmap Finalisation & Stakeholder Presentation", "Stakeholder review; final revisions; presentation to governance council", "1 week", "Approved data governance strategy; final framework; governance roadmap; presentation deck"),
        ],
    },
    "Data_Governance_Training_and_Change_Management": {
        "methodology": [
            "Phase 1 - Training Needs Analysis & Stakeholder Mapping: SecureITLab conducts a training needs analysis to identify knowledge gaps across data governance roles (data owners, stewards, custodians, executives) and maps stakeholder groups requiring tailored training.",
            "Phase 2 - Training Material Development: Role-based training programmes are designed and developed, including workshops, e-learning modules, quick-reference guides, and case studies. An awareness campaign pack is produced.",
            "Phase 3 - Delivery & Facilitation: Training sessions are delivered to targeted stakeholder groups in the agreed format (workshops, webinars, or self-paced). Attendance and completion are tracked.",
            "Phase 4 - Evaluation & Change Management Follow-Up: Training effectiveness is evaluated through assessments and feedback. A change management follow-up plan is produced to sustain behaviour change and embed governance practices.",
        ],
        "timeline": [
            ("Phase 1 - Training Needs Analysis & Stakeholder Mapping", "Training needs analysis; knowledge gap assessment; role mapping; learning objectives", "1 week", "Training needs analysis report; stakeholder and role map"),
            ("Phase 2 - Training Material Development", "Role-based content development; workshop design; e-learning modules; awareness pack", "2 weeks", "Role-based training materials; awareness campaign pack"),
            ("Phase 3 - Delivery & Facilitation", "Training session delivery; attendance tracking; facilitation; Q&A management", "2 weeks", "Delivered training sessions; attendance register; completion records"),
            ("Phase 4 - Evaluation & Change Management Follow-Up", "Post-training assessment; feedback analysis; effectiveness report; change management plan", "1 week", "Training effectiveness report; change management follow-up plan"),
        ],
    },
    "Data_Lifecycle_and_Retention_Management": {
        "methodology": [
            "Phase 1 - Discovery & Regulatory Mapping: SecureITLab maps existing data assets, storage locations, and processing activities. Applicable retention obligations from regulatory frameworks (GDPR, local laws, sector requirements) are identified and documented.",
            "Phase 2 - Retention Schedule Design: A comprehensive data retention schedule is designed covering all data categories, defining retention periods, legal bases, review triggers, and accountable owners for each data type.",
            "Phase 3 - Lifecycle Workflow & Disposal Procedures: Data lifecycle workflows are designed covering creation, storage, use, archival, and secure disposal stages. Secure disposal procedures (including third-party disposal requirements) are documented.",
            "Phase 4 - Documentation, Review & Handover: All lifecycle and retention artefacts are finalised and reviewed with legal, compliance, and IT stakeholders. A handover session is conducted with implementation guidance.",
        ],
        "timeline": [
            ("Phase 1 - Discovery & Regulatory Mapping", "Data asset mapping; storage location inventory; regulatory retention obligations review", "2 weeks", "Data inventory; regulatory retention mapping; current state assessment"),
            ("Phase 2 - Retention Schedule Design", "Retention period definition; legal basis mapping; owner assignment; schedule drafting", "2 weeks", "Data retention policy; retention schedule"),
            ("Phase 3 - Lifecycle Workflow & Disposal Procedures", "Lifecycle stage design; archival workflow; disposal procedure development; third-party requirements", "2 weeks", "Lifecycle workflow designs; secure disposal procedures"),
            ("Phase 4 - Documentation, Review & Handover", "Stakeholder review; final revisions; compliance mapping; handover session", "1 week", "Approved retention policy and schedule; disposal procedures; compliance mapping"),
        ],
    },
    "Data_Quality_Management": {
        "methodology": [
            "Phase 1 - Data Profiling & Quality Assessment: SecureITLab profiles priority data sets to assess current quality across dimensions (accuracy, completeness, consistency, timeliness, uniqueness, validity). A data quality assessment report is produced identifying key quality issues.",
            "Phase 2 - Quality Rules & Dimension Definition: Data quality rules and measurement criteria are defined for each data domain and dimension. Quality thresholds and tolerance levels are agreed with data owners and stewards.",
            "Phase 3 - Remediation Planning & Framework Development: A data quality remediation action plan is developed, assigning ownership, priority, and timelines to each identified quality issue. A data quality management framework is produced.",
            "Phase 4 - Measurement Design & Handover: A data quality measurement approach is designed including automated monitoring, reporting dashboards, and escalation procedures. The framework is formally handed over with implementation guidance.",
        ],
        "timeline": [
            ("Phase 1 - Data Profiling & Quality Assessment", "Data profiling; quality dimension assessment; issue identification; current state report", "2 weeks", "Data quality assessment report; profiling results"),
            ("Phase 2 - Quality Rules & Dimension Definition", "Quality rule definition; dimension criteria; threshold agreement with data owners", "2 weeks", "Quality dimension definitions; data quality rules catalogue"),
            ("Phase 3 - Remediation Planning & Framework Development", "Remediation action plan; ownership assignment; framework development; stakeholder review", "2 weeks", "Data quality management framework; remediation action plan"),
            ("Phase 4 - Measurement Design & Handover", "Monitoring design; dashboard specification; escalation procedures; handover session", "1 week", "Quality measurement methodology; dashboard specification; handover package"),
        ],
    },
    "Data_Stewardship_and_Ownership_Services": {
        "methodology": [
            "Phase 1 - Current State Assessment & Role Inventory: SecureITLab assesses the existing data accountability structure, identifying where data ownership and stewardship roles exist, are undefined, or are unclear across business units and data domains.",
            "Phase 2 - Stewardship Model Design: A data stewardship operating model is designed, defining the roles of Data Owner, Data Steward, and Data Custodian, their accountabilities, authority levels, and interaction model.",
            "Phase 3 - Role Profiling & RACI Development: Detailed role profiles are produced for each stewardship role. A RACI matrix is developed across data governance activities to clarify accountability at the domain level.",
            "Phase 4 - Onboarding Materials & Handover: Steward and owner onboarding materials are produced including training content, checklists, and reference guides. A handover session is conducted with the data governance team.",
        ],
        "timeline": [
            ("Phase 1 - Current State Assessment & Role Inventory", "Accountability review; role inventory; gap identification; domain mapping", "1 week", "Current state assessment; role inventory; accountability gap register"),
            ("Phase 2 - Stewardship Model Design", "Operating model design; role definition; authority levels; interaction model", "2 weeks", "Stewardship operating model; role definition document"),
            ("Phase 3 - Role Profiling & RACI Development", "Role profile development; RACI matrix across governance activities and domains", "1 week", "Role profiles (Owner, Steward, Custodian); stewardship RACI matrix"),
            ("Phase 4 - Onboarding Materials & Handover", "Onboarding pack development; training content; checklists; handover session", "1 week", "Steward and owner onboarding materials; training content; handover record"),
        ],
    },
    "Master_Data_Management_(MDM)": {
        "methodology": [
            "Phase 1 - MDM Discovery & Business Case Development: SecureITLab assesses the organisation's data landscape to identify master data domains (customer, product, employee, supplier, etc.), evaluates data quality and duplication issues, and develops an MDM business case.",
            "Phase 2 - Data Domain Definition & Modelling: Master data domains are formally defined, logical data models are developed for each domain, and data attributes, hierarchies, and relationships are documented.",
            "Phase 3 - Golden Record Design & Integration Planning: Golden record definitions are established for each domain, including survivorship rules and data matching criteria. Integration architecture with source systems is designed.",
            "Phase 4 - Platform Recommendations & Roadmap: Vendor-agnostic MDM platform recommendations are produced, and a phased implementation roadmap with priorities, resources, and investment estimates is delivered.",
        ],
        "timeline": [
            ("Phase 1 - MDM Discovery & Business Case Development", "Data landscape assessment; domain identification; quality review; business case development", "2 weeks", "MDM discovery report; MDM business case"),
            ("Phase 2 - Data Domain Definition & Modelling", "Domain definition; logical data modelling; attribute and hierarchy documentation", "3 weeks", "Master data domain definitions; logical data models"),
            ("Phase 3 - Golden Record Design & Integration Planning", "Survivorship rules; matching criteria; golden record design; integration architecture", "3 weeks", "Golden record design; integration architecture; survivorship rules"),
            ("Phase 4 - Platform Recommendations & Roadmap", "Vendor assessment; platform recommendations; implementation roadmap; investment estimate", "2 weeks", "MDM platform recommendations; phased implementation roadmap"),
        ],
    },
    "Data_Mapping_and_Inventory": {
        "methodology": [
            "Phase 1 - Scoping & Stakeholder Engagement: SecureITLab defines the scope of the data mapping exercise, identifies data custodians and process owners across business units, and designs the data collection approach including interview guides and inventory templates.",
            "Phase 2 - Data Discovery & Interviews: Structured interviews and workshops are conducted with process owners across all in-scope business units to discover personal data processing activities, data types, sources, recipients, and retention periods.",
            "Phase 3 - Flow Mapping & RoPA Development: Personal data flows are mapped and validated. Records of Processing Activities (RoPA) are populated for each processing activity, including legal bases, third-party transfers, and security measures.",
            "Phase 4 - Review, Validation & Handover: The RoPA and data flow diagrams are reviewed with data protection and legal stakeholders, validated, and formally handed over with maintenance guidance.",
        ],
        "timeline": [
            ("Phase 1 - Scoping & Stakeholder Engagement", "Scope definition; data custodian identification; interview guide and template design", "1 week", "Scoping document; stakeholder map; data collection templates"),
            ("Phase 2 - Data Discovery & Interviews", "Stakeholder interviews; processing activity discovery; data type and flow identification", "2 weeks", "Interview records; processing activity inventory; preliminary data flows"),
            ("Phase 3 - Flow Mapping & RoPA Development", "Data flow diagram development; RoPA population; legal basis mapping; third-party register", "2 weeks", "Records of Processing Activities (RoPA); data flow diagrams; third-party sharing register"),
            ("Phase 4 - Review, Validation & Handover", "Stakeholder review; validation; legal review; maintenance guidance; handover", "1 week", "Approved RoPA; validated data flow diagrams; personal data inventory; handover guide"),
        ],
    },
    "Data_Privacy_Assessment_and_Gap_Analysis": {
        "methodology": [
            "Phase 1 - Regulatory Scoping & Framework Selection: SecureITLab confirms the applicable privacy regulations and standards (GDPR, PDPA, and others) and selects the assessment framework. Assessment criteria and evidence requirements are defined.",
            "Phase 2 - Current State Assessment & Evidence Collection: The organisation's privacy practices (notices, consent, data subject rights, DPO appointment, data mapping, breach procedures) are assessed against each requirement through document review and interviews.",
            "Phase 3 - Gap Analysis & Risk Rating: Identified gaps are documented, risk-rated by regulatory exposure and operational impact, and prioritised for remediation.",
            "Phase 4 - Reporting & Remediation Roadmap: A privacy assessment report with risk-rated findings, gap analysis, and a prioritised remediation roadmap with ownership and timelines is produced and presented.",
        ],
        "timeline": [
            ("Phase 1 - Regulatory Scoping & Framework Selection", "Regulatory confirmation; assessment framework selection; criteria and evidence requirements definition", "1 week", "Regulatory applicability matrix; assessment framework; evidence requirements list"),
            ("Phase 2 - Current State Assessment & Evidence Collection", "Privacy practice review; document and policy review; stakeholder interviews; evidence collection", "2 weeks", "Evidence log; current state assessment notes; practice review workbook"),
            ("Phase 3 - Gap Analysis & Risk Rating", "Gap identification; regulatory exposure assessment; risk-rating; remediation prioritisation", "1 week", "Gap analysis workbook; risk-rated findings; prioritised gap register"),
            ("Phase 4 - Reporting & Remediation Roadmap", "Assessment report drafting; roadmap development; ownership assignment; stakeholder presentation", "1 week", "Privacy assessment report; gap analysis; risk-rated findings; remediation roadmap"),
        ],
    },
    "Data_Privacy_Audits_and_Compliance_Monitoring": {
        "methodology": [
            "Phase 1 - Audit Planning & Programme Development: SecureITLab develops the privacy audit programme, defining audit scope, objectives, control framework, evidence requirements, and the compliance monitoring schedule and cadence.",
            "Phase 2 - Compliance Evidence Review & Testing: Privacy compliance evidence (policies, notices, consent records, DSAR logs, DPIAs, breach records, vendor DPAs) is collected and tested against regulatory requirements. Control operating effectiveness is assessed.",
            "Phase 3 - Findings Analysis & Dashboard Design: Audit findings are consolidated, risk-rated, and summarised. A compliance monitoring dashboard is designed to enable ongoing visibility of compliance posture.",
            "Phase 4 - Reporting & Monitoring Framework Handover: A privacy audit report and quarterly compliance summary reporting template are produced. The monitoring framework and dashboard are handed over with operational guidance.",
        ],
        "timeline": [
            ("Phase 1 - Audit Planning & Programme Development", "Audit scope; control framework; evidence requirements; monitoring schedule and cadence design", "1 week", "Privacy audit programme; monitoring schedule; evidence requirements list"),
            ("Phase 2 - Compliance Evidence Review & Testing", "Evidence collection; control testing; policy and notice review; consent and DSAR record review", "2 weeks", "Evidence pack; control testing workbook; compliance testing notes"),
            ("Phase 3 - Findings Analysis & Dashboard Design", "Finding consolidation; risk-rating; compliance dashboard design; reporting template", "1 week", "Findings register; compliance monitoring dashboard design"),
            ("Phase 4 - Reporting & Monitoring Framework Handover", "Audit report; quarterly summary template; monitoring framework handover; operational guidance", "1 week", "Privacy audit report; compliance monitoring dashboard; quarterly summary template; monitoring guide"),
        ],
    },
    "Data_Privacy_Training_and_Awareness_Programs": {
        "methodology": [
            "Phase 1 - Training Needs Analysis & Role Mapping: SecureITLab conducts a training needs analysis, mapping knowledge gaps to specific roles (HR, marketing, IT, legal, general staff) and defining learning objectives for each audience group.",
            "Phase 2 - Content Development & Material Design: Role-based training content is developed including e-learning modules, workshop presentations, quick-reference guides, and awareness campaign assets (posters, intranet content, email campaigns).",
            "Phase 3 - Delivery & Facilitation: Training sessions are delivered to target audiences in agreed formats (live workshops, webinars, or self-paced e-learning). Facilitators manage Q&A and attendance tracking.",
            "Phase 4 - Assessment, Reporting & Awareness Follow-Up: Knowledge assessments are administered post-training. A training completion and effectiveness report is produced. A follow-up awareness campaign schedule is provided.",
        ],
        "timeline": [
            ("Phase 1 - Training Needs Analysis & Role Mapping", "Training needs analysis; role group mapping; knowledge gap assessment; learning objectives", "1 week", "Training needs analysis report; role and audience map"),
            ("Phase 2 - Content Development & Material Design", "Role-based e-learning/workshop development; awareness campaign asset design", "2 weeks", "Role-based training materials; e-learning modules; awareness campaign assets"),
            ("Phase 3 - Delivery & Facilitation", "Live training delivery; webinar facilitation; attendance tracking; Q&A management", "2 weeks", "Delivered training sessions; attendance register; completion records"),
            ("Phase 4 - Assessment, Reporting & Awareness Follow-Up", "Knowledge assessments; completion reporting; effectiveness analysis; follow-up schedule", "1 week", "Training completion and effectiveness report; awareness follow-up campaign schedule"),
        ],
    },
    "Data_Subject_Rights_Management": {
        "methodology": [
            "Phase 1 - Requirements Gathering & Process Mapping: SecureITLab reviews applicable DSR obligations (access, rectification, erasure, portability, objection, restriction) and maps the organisation's current handling processes to identify gaps and inefficiencies.",
            "Phase 2 - Workflow Design & Template Development: End-to-end DSR handling workflows are designed for each right type, including intake, identity verification, response drafting, and escalation steps. Templates for request intake, tracking, and responses are developed.",
            "Phase 3 - Tool Configuration & Integration: DSR management tooling is configured (or manual processes are established) to support request tracking, response deadline monitoring, and audit logging. Integration with relevant systems is planned.",
            "Phase 4 - Testing, Training & Handover: Workflows are tested with sample requests. Staff handling DSRs are trained on procedures. The complete DSR management solution is formally handed over with operational documentation.",
        ],
        "timeline": [
            ("Phase 1 - Requirements Gathering & Process Mapping", "DSR obligation review; current process mapping; gap identification; requirements definition", "1 week", "DSR requirements document; current state process map; gap register"),
            ("Phase 2 - Workflow Design & Template Development", "DSR workflow design per right type; intake, verification, and response templates; escalation procedures", "2 weeks", "DSR process workflows; request intake templates; response templates; tracking log template"),
            ("Phase 3 - Tool Configuration & Integration", "Tool setup; deadline monitoring; audit log configuration; system integration planning", "1 week", "Configured DSR tool or tracking system; integration plan; audit log design"),
            ("Phase 4 - Testing, Training & Handover", "Workflow testing; staff training; operational documentation; formal handover", "1 week", "Test results; trained staff records; DSR log and register; operational procedures"),
        ],
    },
    "Privacy_Incident_and_Breach_Management": {
        "methodology": [
            "Phase 1 - Current State Review & Gap Assessment: SecureITLab reviews the organisation's existing incident and breach management procedures, benchmarking against GDPR Article 33/34 obligations and sector-specific requirements. Gaps in detection, notification, and response capabilities are identified.",
            "Phase 2 - Incident Response Plan Design: A privacy incident response plan is designed, covering detection and triage, severity classification, containment, internal escalation, regulatory notification procedures, and data subject communication.",
            "Phase 3 - Notification Procedures & Log Design: Detailed regulatory notification procedures (72-hour GDPR notification, data subject notifications) are drafted. An incident log template is designed for evidence retention and regulatory demonstration.",
            "Phase 4 - Tabletop Exercise & Handover: A tabletop exercise is facilitated using a realistic breach scenario to test the incident response plan. Post-exercise findings are incorporated and the full package is formally handed over.",
        ],
        "timeline": [
            ("Phase 1 - Current State Review & Gap Assessment", "Existing procedure review; regulatory obligation mapping; detection and response gap assessment", "1 week", "Current state assessment; regulatory gap register"),
            ("Phase 2 - Incident Response Plan Design", "IRP design; severity classification framework; containment procedures; escalation matrix", "2 weeks", "Privacy incident response plan; escalation matrix; severity classification framework"),
            ("Phase 3 - Notification Procedures & Log Design", "Regulatory notification procedures; data subject communication templates; incident log design", "1 week", "Breach notification procedures; data subject notification templates; incident log template"),
            ("Phase 4 - Tabletop Exercise & Handover", "Exercise scenario design; tabletop facilitation; findings incorporation; formal handover", "1 week", "Tabletop exercise scenario pack; post-exercise findings; updated incident response plan"),
        ],
    },
    "Privacy_Policy_Development_and_Implementation": {
        "methodology": [
            "Phase 1 - Regulatory Review & Policy Inventory: SecureITLab reviews applicable privacy regulations and conducts an inventory of existing privacy policies, notices, and consent mechanisms to identify gaps and outdated content.",
            "Phase 2 - Policy & Notice Drafting: External privacy policies, internal data handling policies, layered privacy notices, and cookies/tracking notices are drafted to comply with applicable regulations and communicate processing practices clearly.",
            "Phase 3 - Stakeholder Review & Consent Framework: Draft policies and notices are reviewed with legal, compliance, marketing, and IT stakeholders. A data subject consent framework covering consent capture, management, and withdrawal is developed.",
            "Phase 4 - Finalisation & Implementation Guidance: Approved policies and notices are version-controlled and formatted. Implementation guidance covering website publication, staff communication, and consent mechanism deployment is provided.",
        ],
        "timeline": [
            ("Phase 1 - Regulatory Review & Policy Inventory", "Regulatory review; existing policy inventory; gap identification; drafting scope", "1 week", "Regulatory review notes; policy inventory; gap register"),
            ("Phase 2 - Policy & Notice Drafting", "External and internal policy drafting; layered privacy notice; cookies notice drafting", "2 weeks", "Draft privacy policy; draft data handling policy; draft privacy notices"),
            ("Phase 3 - Stakeholder Review & Consent Framework", "Stakeholder review cycles; feedback incorporation; consent framework development", "1 week", "Reviewed and revised policies and notices; consent framework design"),
            ("Phase 4 - Finalisation & Implementation Guidance", "Final formatting; version control; implementation guidance; website and deployment guidance", "1 week", "Final privacy policy (external and internal); privacy notice templates; consent framework; implementation guidance"),
        ],
    },
    "Privacy_by_Design_and_Data_Minimization": {
        "methodology": [
            "Phase 1 - Discovery & PbD Maturity Assessment: SecureITLab assesses the organisation's current approach to privacy by design across product development and data management processes, identifying where privacy considerations are absent or insufficient.",
            "Phase 2 - PbD Framework & Checklist Design: A Privacy by Design framework aligned to the seven foundational principles is developed. PbD checklists for project initiation, design review, and launch sign-off are produced for use by product, development, and PM teams.",
            "Phase 3 - Data Minimisation Guidelines Development: Practical data minimisation guidelines are produced, covering collection limitation principles, purpose specification, retention defaults, and anonymisation and pseudonymisation techniques.",
            "Phase 4 - Training Material Development & Handover: Training materials for developers, product managers, and data teams are developed to embed PbD practices. The complete framework is handed over with SDLC integration guidance.",
        ],
        "timeline": [
            ("Phase 1 - Discovery & PbD Maturity Assessment", "Current process review; PbD maturity assessment; gap identification; stakeholder interviews", "1 week", "PbD maturity assessment; gap register"),
            ("Phase 2 - PbD Framework & Checklist Design", "Framework design aligned to PbD principles; project and design review checklists", "2 weeks", "Privacy by Design framework; PbD checklist for projects"),
            ("Phase 3 - Data Minimisation Guidelines Development", "Minimisation principles; collection limitation guidelines; anonymisation and pseudonymisation guidance", "1 week", "Data minimisation guidelines; anonymisation and pseudonymisation reference guide"),
            ("Phase 4 - Training Material Development & Handover", "Developer and PM training materials; SDLC integration guidance; formal handover", "1 week", "Developer and PM training materials; SDLC integration guide; handover package"),
        ],
    },
    "Third_Party_Risk_and_Vendor_Management": {
        "methodology": [
            "Phase 1 - Vendor Inventory & Risk Classification: SecureITLab works with procurement, legal, and IT teams to build or validate the organisation's vendor inventory, classify vendors by data access and processing risk level, and define the risk-tiering approach.",
            "Phase 2 - Due Diligence Framework & Questionnaire Design: A third-party privacy risk assessment framework is designed, including a tiered due diligence approach and a vendor privacy questionnaire aligned to data processing obligations and regulatory requirements.",
            "Phase 3 - DPA Review & Vendor Assessment: Existing Data Processing Agreements (DPAs) are reviewed for compliance with applicable privacy regulations. Priority vendors are assessed using the designed questionnaire and a risk scorecard is produced.",
            "Phase 4 - Risk Register & Monitoring Framework Handover: A vendor risk register is populated with assessment findings. A monitoring and review framework covering reassessment triggers and ongoing oversight is established and formally handed over.",
        ],
        "timeline": [
            ("Phase 1 - Vendor Inventory & Risk Classification", "Vendor inventory; data access and risk classification; tiering model definition", "1 week", "Vendor inventory; risk classification matrix; tiering model"),
            ("Phase 2 - Due Diligence Framework & Questionnaire Design", "Framework design; tiered due diligence approach; vendor privacy questionnaire", "2 weeks", "Third-party risk assessment framework; vendor privacy questionnaire"),
            ("Phase 3 - DPA Review & Vendor Assessment", "DPA compliance review; priority vendor assessment; risk scorecard population", "2 weeks", "DPA review findings; vendor risk scorecards; assessment reports"),
            ("Phase 4 - Risk Register & Monitoring Framework Handover", "Risk register population; monitoring and review framework; reassessment triggers; handover", "1 week", "Vendor risk register; monitoring framework; DPA review checklist; handover package"),
        ],
    },
    "Network_Operation_Center_(NOC)": {
        "methodology": [
            "Phase 1 - Onboarding & Infrastructure Discovery: SecureITLab conducts a comprehensive discovery of the client's network infrastructure, devices, and services to be monitored. Monitoring scope, SLA parameters, escalation contacts, and communication channels are formally agreed.",
            "Phase 2 - Monitoring Configuration & Tool Integration: Network monitoring tools are configured to collect metrics, alerts, and events from all in-scope infrastructure components. SNMP traps, syslog forwarding, API integrations, and alerting thresholds are established.",
            "Phase 3 - Service Transition & SLA Validation: The NOC service is transitioned from setup to live operations. SLA performance is validated during a hypercare period, incident response procedures are rehearsed, and knowledge transfer is completed.",
            "Phase 4 - BAU Operations & Monthly Reporting: Full NOC operations commence under agreed SLAs. Incidents are monitored, triaged, and escalated according to defined procedures. Monthly NOC performance reports are delivered to the client.",
        ],
        "timeline": [
            ("Phase 1 - Onboarding & Infrastructure Discovery", "Infrastructure discovery; scope agreement; SLA definition; escalation contact registration", "2 weeks", "Infrastructure inventory; scope document; SLA agreement; escalation matrix"),
            ("Phase 2 - Monitoring Configuration & Tool Integration", "Monitoring tool configuration; SNMP/syslog setup; alerting thresholds; API integration", "2 weeks", "Configured monitoring platform; alert threshold documentation; integration records"),
            ("Phase 3 - Service Transition & SLA Validation", "Live transition; hypercare monitoring; SLA validation; procedure rehearsal; knowledge transfer", "2 weeks", "Service transition record; SLA validation report; knowledge transfer documentation"),
            ("Phase 4 - BAU Operations & Monthly Reporting", "24x7 network monitoring; incident triage and escalation; change support; monthly reporting", "Ongoing", "Network monitoring dashboard; monthly NOC performance reports; incident records"),
        ],
    },
    "Security_Operation_Center_(SOC)": {
        "methodology": [
            "Phase 1 - SOC Onboarding & Log Source Integration: SecureITLab onboards the client environment into the managed SOC, integrating log sources (endpoints, servers, firewalls, cloud services, applications) into the SIEM platform and validating data ingestion and parsing.",
            "Phase 2 - Use-Case Configuration & Playbook Setup: Detection use-cases are configured in the SIEM aligned to the client's threat landscape and MITRE ATT&CK. Incident response playbooks are established for priority threat scenarios and analyst workflows are defined.",
            "Phase 3 - Service Transition & Hypercare: The SOC service transitions from setup to live 24x7 operations. A hypercare period allows fine-tuning of use-cases, alert thresholds, and escalation procedures with direct client engagement.",
            "Phase 4 - BAU Operations & Monthly Reporting: Full SOC operations commence with 24x7 threat monitoring, alert triage, incident escalation, and response. Monthly threat and incident reports are delivered to the client.",
        ],
        "timeline": [
            ("Phase 1 - SOC Onboarding & Log Source Integration", "Log source inventory; SIEM integration; data ingestion validation; parsing configuration", "3 weeks", "Log source integration record; SIEM onboarding confirmation; data validation report"),
            ("Phase 2 - Use-Case Configuration & Playbook Setup", "Detection use-case configuration; ATT&CK mapping; playbook development; workflow definition", "3 weeks", "Configured detection use-cases; incident response playbooks; analyst workflow guide"),
            ("Phase 3 - Service Transition & Hypercare", "Live transition; hypercare monitoring; use-case tuning; escalation rehearsal; knowledge transfer", "2 weeks", "Service transition record; hypercare review findings; tuned use-cases"),
            ("Phase 4 - BAU Operations & Monthly Reporting", "24x7 monitoring; alert triage; incident escalation and response; monthly reporting", "Ongoing", "24x7 SOC service; monthly threat and incident reports; annual SOC review"),
        ],
    },
    "Take_Down_Services": {
        "methodology": [
            "Phase 1 - Threat Intelligence Setup & Monitoring Configuration: SecureITLab configures threat intelligence monitoring to continuously scan for phishing sites, fraudulent social media accounts, counterfeit applications, and brand-abuse domains targeting the client.",
            "Phase 2 - Initial Threat Landscape Assessment: An initial sweep of the client's digital footprint is conducted to identify existing threats and establish a baseline of detected abuse. Priority threats are identified for immediate takedown action.",
            "Phase 3 - Takedown Operations & Escalation Management: Confirmed threats are escalated through formal takedown channels including registrar abuse desks, hosting providers, social media platforms, and app store operators. Progress is tracked until resolution.",
            "Phase 4 - Ongoing Monitoring & Monthly Reporting: Continuous threat intelligence monitoring is maintained. Newly detected threats are processed through the takedown workflow. Monthly takedown activity reports are delivered to the client.",
        ],
        "timeline": [
            ("Phase 1 - Threat Intelligence Setup & Monitoring Configuration", "Monitoring keyword and brand configuration; intelligence feed setup; alert threshold definition", "1 week", "Monitoring configuration record; alert setup confirmation"),
            ("Phase 2 - Initial Threat Landscape Assessment", "Digital footprint sweep; existing threat identification; baseline establishment; priority triage", "1 week", "Initial threat landscape report; prioritised takedown list"),
            ("Phase 3 - Takedown Operations & Escalation Management", "Takedown request submission; registrar and hosting provider escalation; platform notifications; resolution tracking", "Ongoing", "Takedown request logs; resolution records; escalation correspondence"),
            ("Phase 4 - Ongoing Monitoring & Monthly Reporting", "Continuous monitoring; new threat detection; monthly reporting; client review sessions", "Ongoing", "Monthly takedown activity report; threat intelligence monitoring alerts"),
        ],
    },
    "Vulnerability_Management": {
        "methodology": [
            "Phase 1 - Asset Discovery & Scan Configuration: SecureITLab performs or validates asset discovery across the client environment, configures authenticated scanning profiles for all asset classes, and establishes scan schedules aligned to the client's change management cadence.",
            "Phase 2 - Initial Scan & Baseline Assessment: An initial credentialed scan is conducted across all in-scope assets. Scan results are triaged, false positives removed, and a risk-based vulnerability baseline is established.",
            "Phase 3 - Risk-Based Prioritisation & Remediation Tracking: Vulnerabilities are prioritised using CVSS scores, asset criticality, and exploit availability. A remediation tracking dashboard is established and SLA performance is monitored against agreed targets.",
            "Phase 4 - Ongoing Scanning, Reporting & Management Reviews: Recurring scans are executed on the agreed schedule. Monthly vulnerability management reports and management reviews are conducted to assess programme effectiveness and track remediation progress.",
        ],
        "timeline": [
            ("Phase 1 - Asset Discovery & Scan Configuration", "Asset discovery; scan profile configuration; credential provisioning; schedule definition", "2 weeks", "Asset inventory; scan configuration documentation; scanning schedule"),
            ("Phase 2 - Initial Scan & Baseline Assessment", "Credentialed scanning; result triage; false positive removal; risk-based baseline", "1 week", "Initial scan reports; baseline vulnerability register; risk-rated findings"),
            ("Phase 3 - Risk-Based Prioritisation & Remediation Tracking", "CVSS and criticality-based prioritisation; remediation dashboard setup; SLA monitoring", "Ongoing", "Prioritised vulnerability dashboard; remediation SLA tracking register"),
            ("Phase 4 - Ongoing Scanning, Reporting & Management Reviews", "Recurring scanning; monthly reports; management review sessions; programme effectiveness assessment", "Ongoing", "Monthly vulnerability management reports; management review records; trend analysis"),
        ],
    },
}
