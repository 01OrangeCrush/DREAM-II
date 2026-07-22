# DREAM Part II: Combined LLM Evaluator Script

Single self-contained script. Paste Turn 1 first and confirm the fidelity check passes before sending any artifact. Paste artifacts one at a time, in this order, as separate turns in the same session (temperature 0, zero-retention). Run the Step 4 midpoint re-check where marked, between Artifact E and Artifact F.

## Randomization key (seed 2026)

| Run Order | Artifact Letter | Catalog ID | Title |
|---|---|---|---|
| 1 | Artifact A | P03 | Security Training Project |
| 2 | Artifact B | P10 | Lab 1 Infection |
| 3 | Artifact C | P06 | Ukraine Student Activities |
| 4 | Artifact D | P07 | Capstone Summative Part 2 |
| 5 | Artifact E | P12 | Securing E-Commerce Solutions (Course Curriculum) |
| 6 | Artifact F | P08 | Policies and Compliance |
| 7 | Artifact G | P11 | Case Study |
| 8 | Artifact H | P13 | SEED Secret-Key Encryption Lab |
| 9 | Artifact I | P09 | Soft PLC Lab |
| 10 | Artifact J | P04 | CyberEthics Presentation (position paper assignment) |

---

## TURN 1: Frozen evaluator prompt (paste this first, alone)

You are scoring one undergraduate cybersecurity assignment prompt using a single published rubric. Use only the rubric provided below. Do not substitute, supplement, or reconstruct an alternative framework, even if you believe it would be more complete or better suited to the artifact. If the artifact seems to require dimensions outside this rubric, note that in your rationale, but still score only on the five dimensions given.

### Step 1: Fidelity check (required before any scoring)

Before scoring anything, list the five dimensions you will use, in the exact order given below. Do not proceed until this list is produced and matches the published list verbatim. Then stop and wait, I will send you artifacts one at a time.

### The rubric (McCauley et al., 2025)

Each dimension is scored 1 (not addressed), 2 (partially addressed), or 3 (fully addressed).

1. Authenticity. Does the task mirror a real-world cybersecurity problem with realistic constraints? Strong assessments use concrete scenarios, stakeholders, and artifacts, such as logs or configurations, rather than vague, generic prompts.
2. Process Transparency. Are students required to make their thinking visible throughout the task? Effective designs include draft submissions, peer feedback logs, or screencasts, and grade the process as well as the end product.
3. Ethical GenAI Use. Are students prompted to disclose and justify any AI assistance? Assignments can include a short reflection section where students document what tools were used, why, and how outputs were verified.
4. Interactive Verification. Does the task include components that confirm authorship and understanding? Oral defenses, live demonstrations, or structured peer reviews provide checkpoints that confirm comprehension and discourage outsourcing.
5. Evaluative Judgment. Does the assessment require students to critique, compare, or make trade-offs? Tasks that ask students to evaluate alternatives, critique AI outputs, or justify design choices emphasize decision-making rather than rote output.

Threshold: A total score below 10 of 15 flags the task for revision to include more transparency, interaction, or evaluative elements.

### Step 2 and 3: For each artifact I send

For each of the five dimensions, assign a score of 1, 2, or 3, write a one to three sentence rationale, and in the rationale cite the specific anchor language above that drove your score. Do not invent new criteria not present in the anchor text.

Return your response in this exact structure:

Artifact ID: [as provided]

Authenticity: [score] - [rationale citing anchor language]
Process Transparency: [score] - [rationale citing anchor language]
Ethical GenAI Use: [score] - [rationale citing anchor language]
Interactive Verification: [score] - [rationale citing anchor language]
Evaluative Judgment: [score] - [rationale citing anchor language]

Total: [sum]/15
Threshold decision: [Pass, at or above 10] or [Flag for revision, below 10]

Confirm you understand, then run the Step 1 fidelity check now.

---

## TURN 2 onward: artifacts, one per turn, in order

### Artifact A (run position 1, catalog P03)

Paste this as its own turn:

```
Artifact ID: A

Many IT projects fail because end users do not receive the training and support, they need to use new technology effectively. Your end users may need to incorporate new technology and software into their day-to-day job duties, but they can't do this effectively without the right preparation. Training for the end user is one of the most important steps for a successful system implementation. A comprehensive and proactive end user training program sells employees on the benefits of new systems, minimizes productivity impact during the transition period, and cuts down on help desk tickets.

For this project, you will plan, prepare, and present a video of a training module. Assume you are training users who have no previous knowledge of security. 

Select a security awareness topic for your module.

Some possible topics include:

- Social Engineering

- Data Storage and Handling

- Phishing

- Ransomware

- USB Device Safety

- Mobile Device Security

- Mobile App security

- Physical Security

- Password Security

- Safe internet use

Your module should include:

- A Training Plan

- Identify the training need

- Analyze the skills required

- Analyze who you will be training

- Set learning outcomes (minimum of 3)

Your training plan can be for a course of any length (15 minutes to multi day). However, your video presentation will be limited to 15 minutes.

- A Training Manual

Design a training manual. The manual should include an introduction, body and summary (see Chapter 3, A Guide to Computer User Support for Help Desk and Support 6th Edition by: Fred Beisse for writing tips). This manual should also be uploaded with your training plan. 

- Supporting Materials

- Design support materials for use during training. This could be a handout, activity or PowerPoint presentation. These materials should also be uploaded with your manual and training plan. 

- Create a training assessment method. This could be a pre and post-quiz or an activity.

Presentation:

Deliver your training to end users. 

- You will present your training session to the class using a video. Presentations should be no longer than 15 minutes and no less than 10 minutes. Videos will be shared with the class via the discussion forum. You may use the video tool in Canvas or share an unlisted YouTube video link in the forum.  You can be as creative as you would like with the production of your video.

- You must respond to each post and ask at least one follow-up question.  Appendix C in the textbook provides guidelines on preparing slides to aid in a presentation activity. 

Points:

Training Plan - 100

Training Manual - 100

Training Materials - 100

Presentation - 200 (these points are assigned in the discussion post grade.)

Total – 500

Helpful Resources:

Community Tool Box Chapter 12. Providing Training and Technical Assistance: [https://ctb.ku.edu/en/table-of-contents/structure/training-and-technical-assistance](https://ctb.ku.edu/en/table-of-contents/structure/training-and-technical-assistance)
```

### Artifact B (run position 2, catalog P10)

Paste this as its own turn:

```
Artifact ID: B

Lab 1: Infection

**CLARK**

Ransomware: Detection, Response, and Prevention

Lab 1: Infection

Table of Contents

	Disclaimer	3

	Lab topology	3

	Lab configuration	3

	How to take screenshots	3

	How to transfer data between the host computer and VMs	3

	How to access tools	3

	Introduction	5

	Learning outcomes	5

	Section 1: Download the ransomware via a phishing website	6

	Section 2: Review files prior to infection	9

	Section 3: Execute the ransomware	11

	Section 4: Decrypt your files	12

	Learning and reflection	14

# Disclaimer

Please be aware that you will access real ransomware in this lab. It is essential to exercise caution and follow proper procedures when dealing with potentially harmful software and to avoid removing any executable files associated with this software from their designated virtual lab environment. Doing so may trigger alerts within security systems and result in the files being quarantined by antivirus software.

Additionally, please note that the software in this lab is intended for educational purposes only and should not be used to harm others. Misusing the software for any malicious activity could result in legal consequences, and we strongly advise against engaging in any illegal activities. Thank you for your cooperation.

# Lab topology

# Lab configuration

| **Virtual Machine**** (VM)** | **Network Configuration**** (Manual)** | **User Account Information** |
| --- | --- | --- |
| Windows 10 **(****Targeted**** computer****)** | IP address: 192.168.93.1 Netmask: 255.255.255.0 (/24) | Username: jsmith (if needed) Password: Passw0rd! |
| Kali Linux **(Ransomware ****c****ommand****-and-c****ontrol ****s****erver)** | IP address: 192.168.93.132 Netmask: 255.255.255.0 (/24) | Username: kali Password: kali |

# How to take screenshots

**Windows 10 VM:**** **If needed, use the Snipping Tool; the shortcut is placed on the Desktop.

**Kali Linux:** If needed, use the Screenshot utility; the shortcut is placed on the Desktop.

# How to transfer data between the host computer and VMs

**Clipboard items:** Copy and paste clipboard items (screenshots and texts) between the host machine and VMs; they share the same clipboard. 

**Files:** Use a USB flash drive to transfer the files between the host machine and VMs. 

# How to access tools

	You have three options to access the tools specified in lab instructions: 

	- Tools folder on the Desktop

	- Start Menu

	- Taskbar

# Introduction

Ransomware is a type of malware programmed to encrypt the victim's files, rendering the files unusable until a ransom is paid to the attacker. The most common way ransomware infects a network or computer is through phishing emails that trick the recipient into clicking on a malicious link or downloading an infected attachment. Additionally, ransomware can be spread through phishing websites or social engineering attacks. Once the ransomware is executed, it encrypts the victim's files. The attacker then demands a ransom payment, typically in the form of cryptocurrency, in exchange for providing the victim with the decryption key to decrypt their files. In this lab, you will assume the role of a negligent computer user clicking the link on a phishing email, downloading the ransomware, and running it. 

# Learning outcomes

At the end of this lab, you will be able to 

- Identify the primary tactics of ransomware from delivery to decryption

- Analyze the ransom note dropped by ransomware actors

- Discuss the justifications and implications of paying ransom to ransomware actors 

- Identify how ransomware actors store passphrases on their systems 

# Section 1: Download the ransomware via a phishing website

Assume that you (Jesse Smith) are working for Acme Company. Today was ordinary for you until you opened a phishing email pretending to be from the HR department. Follow the steps below to explore how attackers may approach victims and how they might lure their victims into clicking a malicious link.

- Log in to Windows 10.

- Launch Mail application.

- Confirm that you received an email from the “HR department”. Open the email.

- Review the email. Click the link in the email message.

- Review the phishing website pretending to be a part of the HR internal web portal. Click on "this link" to download the ransomware.

A file named "payroll.exe" will be downloaded to the "C:\Users\jsmith\Downloads" folder, as shown in the screenshot below. Copy this file to Desktop for convenience. 

According to the scenario described in the phishing website, you expect to download a program to help you connect to the HR database and see the so-called important information about your payroll update and promotion. Chrome browser shows the file extension as ".exe", as shown below.

Malicious actors usually trick users into clicking the files by changing their icons. In this example, the payroll.exe has a commonly used PDF file icon. Having a PDF icon is not essential for the scenario in this lab as the phishing website mentions "a payroll application"; however, assuming that the same malicious actors might be using another attack vector for which having a PDF icon might improve the odds of executing the ransomware. An example might be delivering ransomware with a USB flash drive. Especially for operating systems that hide the file extension, like the Windows 10 VM, the icon trick can trap many users. 

**Answer the following question****s****:**

- Does your computer hide the file extensions? If you are using a Windows computer, share a screenshot of the configuration by which you can hide or show the extensions of known file types. 

- "What is the advantage of showing known file types in the Windows operating system to help protect against malicious files?"

- What might be the reasons behind the default setting of hiding the extension of known file types?

# Section 2: Review files prior to infection

In this section, you will review the files and confirm they are not encrypted. Follow the steps:

- Open the “Files” folder on the Desktop and confirm that there are four files in this folder. 

- Check the file types (extensions) by right-clicking on each file and then opening Properties. 

- Open each file with the associated applications and review their content. 

- Close files.

# Section 3: Execute the ransomware

In Section 3, you will run the ransomware and observe the change in your files. 

- While the "Files" folder is open, run payroll.exe and simultaneously observe the changes in file names.

- Try to open files with the ".locked" extension by double-clicking on them. (Windows does not hide the "locked" extension as it is not a known file type.)

- Run HxD Hex Editor.

- Open “text1.txt.locked” using the hex editor. Confirm that the content is encrypted.

- Browse to the "Files-backup" folder to access the copies of the original files. Open the “text1" on the Hex editor. Confirm that it is plaintext. Compare "text1.txt.locked" and "text1" in a text editor. 

**Bonus question:** Compare the sizes of “text1.txt.locked” and “text1.txt”. Why are their sizes different? 

- A text file named "!!!! READ_ME !!!!” should have been created by ransomware under the "Files" folder. It is the letter left by malicious actors for victims to read and take action. Review the “!!!! READ_ME !!!!” file created by the payroll.exe. 

**Note:** If you want to run the payroll.exe several times, delete the files with the "locked" extension and copy the plain files under the "Files-backup" folder to the "Files" folder. 

**Answer the following questions:**

- Provide a screenshot of the ransom note created by the ransomware.

- Analyze the language malicious actors used in their ransom note to influence the victim’s decision-making process for their advantage. (Persuasive, threatening, credibility, etc.) 

- From the ransomware actor’s perspective, what are the “must-have” pieces of information that every ransom note should have?

- Paying ransom to malicious actors is a controversial issue, and its legality can vary depending on the laws and policies of the country in question. Governments and law enforcement agencies generally advise against paying ransom to cyber criminals as it may encourage further attacks and criminal activity. Search the Internet to provide an answer on the lawfulness of paying ransoms by government organizations in the US.

- **Fact:** There is no guarantee that paying the ransom will result in the delivery of the keys required for decryption, and criminals may still use the stolen information for illicit purposes. 

**Scenario:** Assume that you are a victim of a ransomware attack. You decide to pay the ransom after carefully considering the potential risks and benefits and with the involvement of the legal expert and law enforcement agency. 

- The encrypted information is critical and necessary. There is no backup, and it is urgently needed for an upcoming merger operation. 

- All other options for recovering the data have been exhausted. 

**Question:** You want to ensure ransomware developers send encryption keys. What would be your possible next steps?

# Section 4: Decrypt your files

In this section, you will acquire the passphrase[^1] by the decryption application. Assume that you sent the ransom to the Bitcoin wallet given in the ransom note.

Typically, ransomware developers send the passphrase to the victim's email or a helpdesk/IT-affiliated email address after the ransom has been paid or decryption operation is performed as a service over the C&C server. In this lab, you will acquire the passphrase by accessing the command-and-control server (C&C server) that is in control of ransomware developers. Follow the steps below:

- Log in to Kali Linux (C&C server). 

- Open a Terminal.

- Type the following command in the terminal window and hit enter.

cd /var/www/html

- Type the following command to see the content of data.txt.

cat data.txt

“data.txt” is used by ransomware developers to store keys used for decryption. Ransomware (payroll.exe) sends the passphrase to the C&C server once the victim has executed it. Each execution of ransomware creates a new line in “data.txt”. 

**Answer ****the ****question:**** **

- Paste the last line of data.txt below or share a screenshot. Each line has three important pieces of information. Identify each piece of information; show them on your pasted text or screenshot. 

**Continue your lab:**

- Copy the passphrase from the last line of “data.txt” to the clipboard. (**Hint:** the last 15 characters of the line belong to the passphrase) (**Note:** Linux Terminal Emulation will allow you to select the text and copy it)

At this point, you need the Decrypter program that will use this passphrase to decrypt your files. Again, assume that you paid the ransom and the ransomware developer sends you a link by email. Follow the steps below: 

- Switch back to Windows 10 VM.

- Open Chrome browser.

- Navigate to this URL: [www.acmepayrollupdate.com/decrypter.exe](http://www.acmepayrollupdate.com/decrypter.exe). Your browser will automatically download the “decrypter.exe” program.

- Switch to your Downloads folder.

- Run the Decrypter application. The application will ask for the passphrase. 

- Paste the passphrase you copied to the clipboard in Step 5 to the Decrypter application's password field. 

- Before you click the “Decrypt My Files” button, open the “Files” folder to be able to observe the decryption operation on file.

- Click on the Decrypt My Files button.

- Open decrypted files to confirm that they are decrypted.

# Learning and reflection 

In two to three paragraphs, using APA style citations if needed, summarize and interact with the content covered in this lab. Summarize what you did as a computer user assuming the role of a victim. In particular, highlight what surprised, enlightened, or otherwise engaged you. You should think and write critically, not just about what was presented but also about the new concepts and tools you learned in this lab.

List a chronological order of major events you observed/did in this lab. Review the tactics of the MITRE ATT&CK Enterprise Matrix on this page ([https://attack.mitre.org/tactics/enterprise](https://attack.mitre.org/tactics/enterprise)). Then, map at least one event in your list to the “Initial Access” tactic and do the same for the “Execution” tactic.

2

[^1]: . The term "passphrase" is used knowingly; it is not the decryption key but the string used to generate the decryption key
```

### Artifact C (run position 3, catalog P06)

Paste this as its own turn:

```
Artifact ID: C

Ukraine Student Activities

**LO1 – Apply ****&**** Analyze: ICS Kill Chain ****&**** Attack Mechanics**

**Activity 1 – ****2016 CRASHOVERRIDE / Industroyer Technical Evolution**

Students focus on the 2016 attack and CRASHOVERRIDE/Industroyer:

- Summarize how CRASHOVERRIDE differs from the 2015 playbook:

- Protocol-aware modules (e.g., IEC 60870-5-104) to directly issue control commands to IEDs.

- A modular, extensible framework vs. primarily manual HMI takeover.

- A data-wiping component to disrupt recovery.

- Analyze why protocol-aware malware is such a big step for ICS security:

- Lower reliance on human-in-the-loop operations.

- Potential for faster and broader impact.

- Difficulty of defending purely with IT-style controls.

Deliverable:

- A 2–3 page technical brief titled *“From BlackEnergy to CRASHOVERRIDE: Evolution of Grid-Focused Malware”*, highlighting:

- Key technical shifts between 2015 and 2016.

- 4–6 ICS-specific defensive measures (e.g., protocol-aware anomaly detection, engineering change control, ICS network baselining, secure remote operations) that become more important in light of CRASHOVERRIDE.

**LO2 – ****Evaluate ****&**** Synthesize: Resilience, Governance ****&**** Policy**

**Activity ****2**** – ****Lessons for Grid Resilience ****&**** U.S. Susceptibility**

Students read the MIT paper and NERC / other lessons-learned materials (LO2 sources) and discuss:

- What do these reports identify as the **biggest lessons** from the Ukraine incidents (segmentation, training, manual operations, backup procedures, etc.)?

- How do they evaluate the **susceptibility** of other grids (e.g., U.S.) to similar attacks?

- What’s the role of:

- Regulatory frameworks (e.g., NERC CIP)?

- Information sharing (ISACs, ICS-CERT/CISA)?

- Exercises and red teaming in improving resilience?

Students then:

- Create a table with **“Lesson from Ukraine” → “Implication for our utility / national grid.”**

**Deliverable:**

- A 1–2 page **“Ukraine Lessons Learned for Our Grid”** summary or slide deck mapping:

- At least 5 key lessons.

- How they would apply in your regional context.

- Whether existing controls (e.g., NERC CIP) fully address them or leave gaps.
```

### Artifact D (run position 4, catalog P07)

Paste this as its own turn:

```
Artifact ID: D

Capstone

**Summative assessment Part 2**

# Regional HOpital Cybersecurity Threat

Regional Hospital is a 500-bed tertiary hospital facility located in northeastern Kentucky. The hospital has been providing high quality care for patients in the Kentucky, Ohio, and West Virginia tri-state area since 1968. Comprehensive patient services include heart and stroke care, women’s health, mother and baby care, cancer care, orthopedics, neurology, and rehabilitation services.

U.S. News and World Report recently named Regional Hospital a 2021-22 High Performing Hospital for orthopedic care for the fifth straight year.

Regional Hospital has been designated as a Five-Start Hospital by the Centers for Medicare and Medicaid Services (CMS) for the quality of patient care in 2020 and 2021.

## Part 1

Scenario: It’s the Friday afternoon before a three-day weekend. A network intrusion alert warns of increased network activity related to the electronic medical records (EMR) system as well as other servers and devices on the network. 

Many systems are down across the network. Employees are reporting that they are unable to access the electronic medical records system. Patients are contacting the IT Helpdesk with complaints that the patient portal is not accessible. 

The readme.txt file shown below is discovered in file folders throughout the organization.

The IT department believes that a Ryuk ransomware attack involving electronic medical records is underway and has notified all offices and facilities to switch to downtime procedures immediately. Please read this [article ](https://www.csoonline.com/article/3541810/ryuk-explained-targeted-devastatingly-effective-ransomware.html)on Ryuk. 

Questions: 

After you have reviewed Part 1, take some time to answer the attached questions. [Expected response length: 2 Paragraphs]

- Is this considered a HIPAA breach? If unable to determine this yet, what additional information is needed to determine this? HIPAA reference: [https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html) 

- Who needs to be notified regarding the incident at this point [Incident Response (IR) team, EMR vendor, law enforcement, etc.]?

## Part 2

Scenario: The IT department has verified the Ryuk signature from the attack. 

IT has confirmed that this is indeed a Ryuk ransomware attack. Initial infection appears to be from a VP’s computer but has spread beyond EMR to operations systems (building access control, etc.). Increased outgoing network traffic is consistent with ongoing exfiltration.

At this point of time, there are a few options to consider:

- Backups: Unable to perform restoration from backups as yet. Need to check the backup sites, and this might take time. Also need to verify if backup sites have also been infected before considering restoration.

- Disaster recovery: Need to check DR site’s availability at secondary site (e.g. cloud provider). Also need to verify if that site has been infected.

- Restoration: Any machine infected might have to be completely rebuilt from a backup. This is important to be assured that all the malware has been removed during the rebuild process. But the process will take time. 

Questions:

After you have reviewed Part 2, take some time to answer the attached questions. [Expected response length: 3-4 Paragraphs]

During the time it takes to plan actions, the following question needs to be addressed:

- Should an outside forensics firm be engaged?

- Should the FBI be called in at this time? Consider the pros and cons of calling them in or not.

## Part 3

Scenario: The initial forensics analysis indicates that offsite backups of Regional Hospital systems are intact, but local backups have been encrypted by the ransomware and so cannot be used to restore systems.

The last backup successfully transferred offsite is from six hours before the ransomware attack was initiated. 

At this time, it is unknown if the malware hooks were already embedded in files that were captured as part of those last backups, but the offsite backups are accessible (they have not been encrypted by the ransomware). 

Available threat intelligence indicates that this particular ransomware actor has a history of exfiltration of data for a secondary extortion option and a reputation for providing a valid decryption key upon payment of the ransom.

See:

[CISA Alert AA20-302A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-302a)

[Threat Actors Targeting Hospitals with Double Extortion Ransomware](https://healthitsecurity.com/news/threat-actors-targeting-hospitals-with-double-extortion-ransomware)

Questions:

After you have reviewed Part 3, take some time to answer the attached questions. [Expected response length: 3-4 Paragraphs]

Should the organization just pay the ransom? Explain, addressing:

- Is this legal?

- Is this ethical? If your answers to these questions differ, explain.

- Who do you think should be involved in approval (or disapproval) of such payment?

- What if the attacker doesn’t provide the decryption key/protocol after payment?

See: [Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments](https://home.treasury.gov/system/files/126/ofac_ransomware_advisory_10012020_1.pdf) – from Treasury Department

## Part 4

Scenario: The leadership team of Regional Hospital has authorized a restoration attempt of systems from the last offline backup. Recall, the last backup successfully transferred offsite is from 6 hours before the ransomware attack was initiated. 

Questions:

After you have reviewed Part 4, take some time to answer the attached questions. [Expected response length: 5 Paragraphs]

- How do you ensure the backups aren’t also infected?

- How can you make sure the unauthorized actor isn’t in your system anymore?

- What are the general steps for recovery from backup? Explain in terms of data recovery objectives as defined in NIST SP 800-34 Rev. 1 (addressed in Practitioner level Knowledge Area Information Security Business Impact Analysis section).

- Based on the information above, what is the minimum value possible for offsite backup's Recovery Point Objective (RPO)? Explain how you arrived at this value.

- Discuss whether beginning restoration of systems at this time (52 hours after the ransomware encrypted systems) should be within the Maximum Tolerable Downtime (MTD) for Regional Hospital.

- How can you restore systems without destroying evidence for the forensic firm? In other words, what steps must be taken to preserve the evidence from systems before they are restored?

## Part 5

Scenario: The following forensics report has been provided by experts on the attack.

[Forensic Report](https://dcidt.louisville.edu/programs/cybersecurity/capstone/CapstoneRyukReport.pdf)

The forensic analysis determines the source of the initial intrusion was a malware infected document sent via a phishing email to an employee and that the unauthorized actor moved laterally throughout your environment after entering through the malware dropped by the phishing message. 

The good news is the EMR and other systems are back up and running. The forensic analysis confirmed the unauthorized actor is no longer in your environment.

The bad news is the forensic analysis has confirmed the ransomware was a variant with data exfiltration capabilities, which potentially accessed your entire patient data base, including medical information and Social Security numbers.

Questions:

After you have reviewed Part 5, take some time to answer the attached questions. [Expected response length: 2 Paragraphs]

- Who must be notified and when? [The patient or their personal representative, HHS, consumer reporting agencies, the media, etc.? State data breach requirements can require more but not less than the Federal requirements.] Hint: You get these numbers from the [forensics report](https://dcidt.louisville.edu/programs/cybersecurity/capstone/CapstoneRyukReport.pdf).

- Note: Acquisition, access, use, or disclosure of unsecured protected health information in a manner not permitted under the HIPAA Privacy Rule is presumed to be a breach unless the Covered Entity or Business Associate can demonstrate that there is a low probability that the PHI has been compromised based on a risk assessment. Unfortunately, “compromise” is not well defined.

- [https://www.hhs.gov/sites/default/files/RansomwareFactSheet.pdf](https://www.hhs.gov/sites/default/files/RansomwareFactSheet.pdf) 

- For more information on breach notifications: [https://www.bakerlaw.com/BreachNotificationLawMap](https://www.bakerlaw.com/BreachNotificationLawMap) 

## Part 6

Scenario: The Chief Information Security Officer (CISO) of Regional Hospital has asked you to help prepare a set of recommendations to use in the Lessons Learned meeting as part of NIST’s recommended Post-Incident Activity (see [NIST SP 800-61 Rev. 2, Section 3.4](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)).

Specifically, the CISO asks that you consider all the details that have come to light about this incident and general understanding of ransomware, security principles, best practices, etc. 

Questions:

After you have reviewed Part 6, take some time to answer the attached questions. [Expected response length: At least 2 pages]

- What are 5 recommendations (in priority order) that you would suggest the organization take to avoid/mitigate similar attacks and why?

- Which area(s) of the[ NIST Cybersecurity Framework ](https://csrc.nist.gov/Projects/cybersecurity-framework/nist-cybersecurity-framework-a-quick-start-guide)(CSF) do you think needs to be reinforced and why?

			 Page |  

		  This document is licensed with a Creative Commons Attribution 4.0 International License ©2017 Catalyzing Computing and Cybersecurity in Community Colleges (C5). 

		

			 Page |  

			 

  This document is licensed with a Creative Commons Attribution 4.0 International License ©2017
```

### Artifact E (run position 5, catalog P12)

Paste this as its own turn:

```
Artifact ID: E

Course Curriculum
Securing E-Commerce Solutions
Course Description
This course covers emerging online technologies and trends and their influence on the electronic commerce
marketplace. Students will learn various revenue models and how to market on the Web. Next, the course covers
online auctions and various legal and ethical issues. Students will learn about important security issues, such as
spam and phishing, their role in organized crime and terrorism, identity theft, and online payment fraud. Finally,
students learn how to plan for and secure electronic commerce. Students will gain skills to implement a secure ecommerce site with exposure to marketing, entrepreneurship, advertising, business, fulfillment, software
development and payment gateways. This course will cover the following topics:
•
•
•
•
•
•
•

Electronic commerce technology
E-commerce models and issues
Principles and case studies of electronic commerce
Introduction to security architectures for electronic commerce, including digital signatures
Certificates, and public key infrastructure (PKI)
Legal and national policy electronic commerce issues
Policy and planning

This course will require additional outside lab time.

Course Value
Business and industry needs require the training and skills related to electronic commerce security that this
course will provide.

Course Objectives/Outcomes
Students will:
•
•
•
•
•
•
•
•
•
•
•
•
•

Understand ethical, social and legal concerns in e-commerce
Understand various forms of intellectual property
Understand basic concepts of privacy and information rights
Understand the relationship between internet technology and business
Identify economic and business forces driving e-commerce
Describe types of e-commerce
Describe e-commerce business models
Describe how internet and Web features and services support e-commerce
Explain the process and considerations when building an e-commerce solution
Understand e-commerce crime and security problems
Identify security threats in the e-commerce environment
Identify methods to protect online privacy
Describe technology to secure Internet communications and protect networks, servers and clients

Textbook and Other Required Materials Textbook:
Internet Security: How to Defend Against Attackers on the Web, 2nd Edition
Mike Harwood
ISBN-13: 9781284090550 (Print)
© 2016 Jones & Bartlett Learning
Ebook: https://www.vitalsource.com/referral?term=9781284104301
Class Methods/Strategies
The method of instruction will include lecture, demonstrations, case studies, required lab
assignments and projects.
Assessment
Students will work as a team to develop an e-commerce solution. Individual performance will be based
on presentations at mid-term and final, feedback from team members, quizzes and results contributed
to the site.
The Live Case Project will consist of a strategy paper, an e-commerce website and a presentation. Each
team member will have a role(s) on the team. The roles include Project Manager, Security,
Payment/Cart, Database/Backup, Business and Graphics. Milestones are listed in weekly assignments.
The purpose of the Milestones is to track the expected progress the team should be making toward
project completion. A Milestone presentation will be presented at midterm to review the progress of
the project. The strategy paper should document the company information considerations; e-commerce
strategy selected; reasons for the selection of infrastructure, design, payment system and security
features; security threats that could impact the site; marketing strategy; issues integrating business
strategy and technology and problems encountered during the project. The final project presentation
will be presented on the date of the scheduled final for the course. The presentation should
demonstrate the site and present the content of your strategy paper.

Course Schedule
Week
1

2

3

4
5
6
7

8

Discussion
Syllabus, Introductions, Project
Chapter 1: From Mainframe to
Client/Server to WWW
Supplemental Material: ECommerce Introduction and
Business Models
Chapter 2: Security
Considerations for Small
Business
Chapter 3: Security
Considerations for Home and
Personal Online Use
Chapter 4: Mitigating Risk When
Connecting to the Internet
Chapter 5: Mitigating Web Site
Risks, Threats, and
Vulnerabilities
Chapter 6: Web Application
Security Consortium
Chapter 7: Securing Web
Applications

Assignment
Syllabus Quiz, Milestone 1

Client Meeting and Q & A, Quiz 1

Milestone 2: Business Model for Project

Milestone 3: Marketing and Advertising Strategy

Milestone 4: Infrastructure Selection
Quiz 2
Milestone 5: Web Platform Selection

Mid-Term Progress Presentation

9

Chapter 8: Mitigating Web
Application Vulnerabilities

Milestone 6: Payment System Selection

10

Chapter 9: Maintaining PCI-DSS
Compliance for E-Commerce
Web

Milestone 7: Content and Design Layout

11

Chapter 10: Testing and Quality
Assurance for Web Sites

Quiz 3

12

Chapter 11: Web Site
Vulnerability and Security
Assessment

13

Chapter 13: Securing Personal
and Business Communications

Milestone 8: Risk Assessment

14

Project Work Days

15

Project Work Days

Final

Project Presentation

Live Case Project
Assignment:
Students are assigned to a team that will be responsible for the development of a “live case”
project. The objective of the assignment is to help you put all the different aspects of the
course together into a comprehensive overview of a client’s comprehensive physical and
Internet-enabled strategy. Your assignment is (1) a team project strategy paper, (2) an
executive presentation of the team paper that discusses the company’s strategic combined
physical and digital strategy for both competitive advantages as well as consumer value, and (3)
an e-commerce website for the client.
Each team member will have a role(s) on the team. The roles include Project Manager,
Security, Payment/Cart, Database/Backup, Business and Graphics. Milestones are listed in
weekly assignments; they are not graded or turned in individually but will be part of the total
project. The purpose of the Milestones is to track the expected progress the team should be
making toward project completion.
A Milestone presentation will be presented at midterm to review the progress of the project.
The strategy paper should document the company information considerations; e-commerce
strategy selected; reasons for the selection of infrastructure, design, payment system and
security features; security threats that could impact the site; marketing strategy; issues
integrating business strategy and technology and problems encountered during the project.
Paper maximum length: 10 pages – there can be an appendix. It is not to serve to get around
the 10-page limit but provide reference information to support the paper when desired.
When organizing the structure of the paper, consider the items below to assist in the paper
structure, presentation organization and thinking on the development of your site. Some of the
issues you will discuss in your paper will not be incorporated into your actual working website.
The paper includes the course content as it relates to:
1. Company Information considerations: Description of the organization's information
culture (attitudes towards information, information sharing, information load,
information politics, and information norms). Definition of the primary audience and
whether there are potential secondary users. Understandable demographics of the
audience (age, sex, location if regional) o Psychographics (metrics, like behaviors or
psychological aspects of consumers). Primary user of the product or service. Company
strategic positioning for consumers and against present and future competitors.
2. Infrastructure considerations: What are the physical and Internet aspects of the firm and
how do these interrelate to accomplish the company’s overall strategy? The
infrastructure issues relating to "back office" applications, such as security issues,
personal information database collection, storage and use, cookie management, and
shopping cart needs. You will want to include a discussion of the platform the site may
be primarily viewed on (PC, netbook, phone, etc.).

3. Discussion of supply chain activities and product distribution. Marketing considerations sales & consumer interactions. Types of advertising being considered.
4. How the website is designed to meet the company’s objectives and strategy. The
purpose of the site and how it is organized to assist with the accomplishment of the
overall company strategy. The paper should underscore how the site has been designed
to enhance the consumer/viewer relationship/interaction.
5. Supporting Internet communication activities: Such as social networks and relationship
building with the consumer.
6. Company Physical and Internet integrated strategy issues both current and future. This
is a central issue to your paper as it relates to the current and future competitiveness of
the firm as well as the company’s attractiveness to consumers. Who are competitors
and how are they positioned? What are the future activities for competitiveness: how
will the firm be structured and what activities will be important to maintain or achieve
competitiveness?
Teams need to note which team member was responsible for what specific tasks. This must
be clear in the paper and presentation.
Assure that the paper’s structure is logical, clear, and well-aligned with the information
covered in the course.
The final project presentation will be presented on the date of the scheduled final for the
course. The presentation should demonstrate the site and present the content of your
strategy paper. The presentation should be approached as if you were presenting the
website to a client, so you want the presentation to be professional, concise and without
technical problems. During the presentation, each team member is expected to be active in
the discussion of the page they designed as well as in the overall business strategy
discussion. Presentations will be graded for thoughtfulness, coverage of the lecture
material, as well as their website content, format, layout, and consistency as it relates to
addressing the overall strategy of the company. Presentation length: 15 minute minimum 1.5 hour maximum, with 5 additional minutes for questions
This is a significant project, so be sure to manage the progress and provide a comfortable
margin. The milestones will state where the team’s progress should be. Keeping on track is
your responsibility.
The team will not be penalized if the site is not complete. However, reasons for not
completing the project should be documented in the strategy paper.
The project will be worth 1000 points:
Strategy Paper – 500
Presentations – 200
Teammate reviews – 300

Notes:
This course uses entrepreneurial learning as a capstone to simulate a real-world project team. The students
are a mixture of majors in the Computer Information Systems program. It can be easily adapted for
undergraduate or graduate programs. The "client" for the project in this course was a non-profit or small
business in need of a digital platform making this course suitable for service learning.
```

### STEP 4 MIDPOINT FIDELITY RE-CHECK (paste as its own turn before Artifact F)

```
Before continuing, repeat the Step 1 fidelity check: list the five rubric dimensions you are using, in order, and confirm they still match the published list verbatim.
```

### Artifact F (run position 6, catalog P08)

Paste this as its own turn:

```
Artifact ID: F

Policies and Compliance

# Synopsis:

You will be selecting a regulated industry and identifying the specific IT requirements expected of an organization within that industry.

# Goal:

You will exercise skills in research and documentation, identifying pertinent requirements for an IT infrastructure. This will be useful in developing and maintaining security for regulated environments in an ever-changing industry.

# Knowledge and Skills:

This assignment will help you become familiar with the IT and security frameworks used in developing security policies and procedures.

You will be able to find and identify relevant regulations and standards when tasked with securing systems within an unfamiliar environment.

# Scenario:

A new organization is starting up. They have secured funding and expertise with regards to the primary business function, but know nothing of IT and IT security. You are interviewing for the position of CISO. If hired, you will be the primary author of the organization's security policy. As part of the interview process, you have been asked to display knowledge of the IT requirements for the organization which will guide the development of this policy.

# Task:

Select a regulated industry with its own IT security requirements.

You may pick any organization that you are interested in, as long as it has relevant requirements for IT.

Example small businesses:

	Dentist / doctor office

	Private school / tutoring center

	Government contractor

	Bank

	Casino

	Restaurant

Research various laws, regulations, and industry standards to identify restrictions and requirements applicable to an organization operating within the selected environment.

Once these restrictions and requirements are identified, develop an outline for a security policy that addresses them. You are encouraged to reference frameworks from the chapter when planning the policy outline.

The policy outline can be either a high-level governing policy, or lower-level technical policy. Make sure to use appropriate language for the target audience of the chosen policy type.

# Rubric:

| Objectives | Needs Improvement | Standard | Excels |
| --- | --- | --- | --- |
| Identifies applicable laws, regulations, and standards | Not identified | Required laws, regulations, and standards identified | Identifies requirements, including optional extras (example – guest network connectivity within a bank, or credit card usage within a doctor’s office) |
| Identifies specific IT requirements (Example: quarterly vulnerability assessment, or administrative access logging) | Not identified | Specific IT requirements identified, but details left out (example – requires vulnerability assessments, but neglect to mention externally provided by accredited company) | Specific requirements identified, including source, location, and timing when applicable |
| Develops security policy outline | Not completed | Outline does not match relevant requirements for environment | Outline provides plan for network design and maintenance in compliance with relevant requirements |
| Writes policy outline for target audience – either governing policy or technical policy | Policy outline not completed, or language not comprehensive for either audience | Language used not appropriate for target audience (either too technical for governing, or not technical enough for technical policy) | Language used in policy outline matches target audience for appropriate level of comprehension |
```

### Artifact G (run position 7, catalog P11)

Paste this as its own turn:

```
Artifact ID: G

Case Study

**CLARK**

Ransomware: Detection, Response, and Prevention

Case Study

Table of Contents

	Learning outcomes	3

	About Decider tool	3

	Install Decider tool on Kali Linux	3

	Review ransomware tactics and techniques	4

	Use Decider tool	5

	Review the tactics and techniques	5

	Submit	5

	References	5

# Learning outcomes

At the end of this case study, you will be able to 

- Install CISA’s Decider tool on Linux

- Extract ransomware behavior and IOCs from a security analysis report prepared by malware researchers 

- Use the Decider tool to identify tactics and techniques of the ransomware 

# About Decider tool

CISA released the Decider tool in March 2023 to help with MITRE ATT&CK mapping. “Decider is a free tool to help the cybersecurity community map threat actor behavior to the MITRE ATT&CK framework” (CISA, 2023). 

Github page: [https://github.com/cisagov/Decider/](https://github.com/cisagov/Decider/)

CISA’s video: [https://www.youtube.com/watch?v=sTrOV4pnbXA](https://www.youtube.com/watch?v=sTrOV4pnbXA)

Fact sheet: [https://www.cisa.gov/sites/default/files/2023-03/decider_fact_sheet_508c.pdf](https://www.cisa.gov/sites/default/files/2023-03/decider_fact_sheet_508c.pdf)

Blog: [https://www.cisa.gov/news-events/news/helping-cyber-defenders-decide-use-mitre-attck](https://www.cisa.gov/news-events/news/helping-cyber-defenders-decide-use-mitre-attck)

# Install Decider tool on Kali Linux

In order to install Decider Tool, you will need to install the Docker first. Make sure that Kali Linux has an Internet connection. Follow the steps below:

- Log in to Kali Linux.

- Open a terminal window. 

- Run the following commands one by one. Type the root password as "kali" without double quotes when prompted.

																sudo apt update && sudo apt -y full-upgrade

																

																sudo apt install curl gnupg2 apt-transport-https software-properties-common ca-certificates

																

																curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg

																

																echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" | sudo tee /etc/apt/sources.list.d/docker.list

																

																sudo apt update

																

																sudo apt install docker-ce docker-ce-cli containerd.io

																

																sudo usermod -aG docker $USER

																

																newgrp docker

																

																systemctl enable docker --now

																

Check this webpage if you see any error messages throughout these steps:

- [https://computingforgeeks.com/install-docker-and-docker-compose-on-kali-linux](https://computingforgeeks.com/install-docker-and-docker-compose-on-kali-linux) 

Now, you can install Decide Tool. Follow the steps below:

- In the same terminal window, type the following commands: 

																

																git clone https://github.com/cisagov/decider.git

																cd decider

																cp .env.docker .env

																

- You will need to modify the .env file. Open the file with your favorite text editor. (mousepad or vi)

- Find the following line in the .env file: 

																	WEB_IP=127.0.0.1

																

- Make the following change:

																	WEB_IP=0.0.0.0

																

- Save the file and exit the text editor. 

- Type the following command in the terminal window:

																	sudo docker compose up

																

- You completed the installation. Open Firefox browser. Navigate to the following address: 

																	http://127.0.0.1:8001/

																

- Type in the following credentials to access the Decider application: 

																user: admin@admin.com

																pass: admin

																

Check this webpage if you see any error messages throughout these steps:

- [https://github.com/cisagov/decider](https://github.com/cisagov/decider) 

# Review ransomware tactics and techniques

The following list provides analysis reports for nine different ransomware families. Choose one or search the Internet for others. 

- LockBit: [https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)

- DarkSide: [https://blog.qualys.com/vulnerabilities-threat-research/2021/06/09/darkside-ransomware](https://blog.qualys.com/vulnerabilities-threat-research/2021/06/09/darkside-ransomware) 

- Emotet: [https://www.cisa.gov/news-events/alerts/2018/07/20/emotet-malware](https://www.cisa.gov/news-events/alerts/2018/07/20/emotet-malware)

- Ryuk: [https://www.cisa.gov/sites/default/files/publications/202104081030%20Ryuk%20Variant%20TLP%20White.pdf](https://www.cisa.gov/sites/default/files/publications/202104081030%20Ryuk%20Variant%20TLP%20White.pdf)

- Maze: [https://www.hhs.gov/sites/default/files/maze-ransomware.pdf](https://www.hhs.gov/sites/default/files/maze-ransomware.pdf)

- KeRanger: [https://www.bitdefender.com/blog/businessinsights/technical-advisory-why-lockbit-ransomware-on-macos-is-not-a-significant-threat-yet](https://www.bitdefender.com/blog/businessinsights/technical-advisory-why-lockbit-ransomware-on-macos-is-not-a-significant-threat-yet)

- REvil: [https://cybersecurity.att.com/blogs/labs-research/revils-new-linux-version](https://cybersecurity.att.com/blogs/labs-research/revils-new-linux-version)

- Avoslocker: [https://blogs.vmware.com/security/2022/02/avoslocker-modern-linux-ransomware-threats.html](https://blogs.vmware.com/security/2022/02/avoslocker-modern-linux-ransomware-threats.html)

- ESXiArgs: [https://www.bleepingcomputer.com/news/security/massive-esxiargs-ransomware-attack-targets-vmware-esxi-servers-worldwide](https://www.bleepingcomputer.com/news/security/massive-esxiargs-ransomware-attack-targets-vmware-esxi-servers-worldwide)

Carefully review, inspect, and take note of ransomware tactics and techniques.

# Use Decider Tool

Use Decider Tool to find and select the tactics and techniques of the ransomware of your selection. 

At the end of the selection process, export your selection to a Microsoft Word document and a JSON file for MITRE ATT&CK Navigator. 

# Review the tactics and techniques

Open the Word file and review it.

Open the JSON file on MITRE ATT&CK Navigator and review the techniques you added. 

# Submit 

Submit both files to your instructor. 

# References

CISA. (2023, March 1). CISA Releases Decider Tool to Help with MITRE ATT&CK Mapping. https://www.cisa.gov/news-events/alerts/2023/03/01/cisa-releases-decider-tool-help-mitre-attck-mapping

2
```

### Artifact H (run position 8, catalog P13)

Paste this as its own turn:

```
Artifact ID: H

SEED Labs – Secret-Key Encryption Lab

1

Secret-Key Encryption Lab
Copyright © 2018 by Wenliang Du.
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
License. If you remix, transform, or build upon the material, this copyright notice must be left intact, or
reproduced in a way that is reasonable to the medium in which the work is being re-published.

1

Overview

The learning objective of this lab is for students to get familiar with the concepts in the secret-key encryption
and some common attacks on encryption. From this lab, students will gain a first-hand experience on
encryption algorithms, encryption modes, paddings, and initial vector (IV). Moreover, students will be able
to use tools and write programs to encrypt/decrypt messages.
Many common mistakes have been made by developers in using the encryption algorithms and modes.
These mistakes weaken the strength of the encryption, and eventually lead to vulnerabilities. This lab
exposes students to some of these mistakes, and ask students to launch attacks to exploit those vulnerabilities.
This lab covers the following topics:
• Secret-key encryption
• Substitution cipher and frequency analysis
• Encryption modes, IV, and paddings
• Common mistakes in using encryption algorithms
• Programming using the crypto library
Readings. Detailed coverage of the secret-key encryption can be found in the following:
• Chapter 21 of the SEED Book, Computer & Internet Security: A Hands-on Approach, 2nd Edition,
by Wenliang Du. See details at https://www.handsonsecurity.net.
Lab Environment. This lab has been tested on our pre-built Ubuntu 20.04 VM, which can be downloaded
from the SEED website.

2

Lab Environment

In this lab, we use a container to run an encryption oracle. The container is only needed in Task 6.3, so you
do not need to start the container for other tasks.
Container Setup and Commands. Please download the Labsetup.zip file to your VM from the lab’s
website, unzip it, enter the Labsetup folder, and use the docker-compose.yml file to set up the lab
environment. Detailed explanation of the content in this file and all the involved Dockerfile can be
found from the user manual, which is linked to the website of this lab. If this is the first time you set up a
SEED lab environment using containers, it is very important that you read the user manual.
In the following, we list some of the commonly used commands related to Docker and Compose. Since
we are going to use these commands very frequently, we have created aliases for them in the .bashrc file
(in our provided SEEDUbuntu 20.04 VM).

SEED Labs – Secret-Key Encryption Lab

$ docker-compose build
$ docker-compose up
$ docker-compose down

2

# Build the container image
# Start the container
# Shut down the container

// Aliases for the Compose commands above
$ dcbuild
# Alias for: docker-compose build
$ dcup
# Alias for: docker-compose up
$ dcdown
# Alias for: docker-compose down

All the containers will be running in the background. To run commands on a container, we often need
to get a shell on that container. We first need to use the "docker ps" command to find out the ID of
the container, and then use "docker exec" to start a shell on that container. We have created aliases for
them in the .bashrc file.
$ dockps
$ docksh <id>

// Alias for: docker ps --format "{{.ID}} {{.Names}}"
// Alias for: docker exec -it <id> /bin/bash

// The following example shows how to get a shell inside hostC
$ dockps
b1004832e275 hostA-10.9.0.5
0af4ea7a3e2e hostB-10.9.0.6
9652715c8e0a hostC-10.9.0.7
$ docksh 96
root@9652715c8e0a:/#
// Note: If a docker command requires a container ID, you do not need to
//
type the entire ID string. Typing the first few characters will
//
be sufficient, as long as they are unique among all the containers.

If you encounter problems when setting up the lab environment, please read the “Common Problems”
section of the manual for potential solutions.

3

Task 1: Frequency Analysis

It is well-known that monoalphabetic substitution cipher (also known as monoalphabetic cipher) is not
secure, because it can be subjected to frequency analysis. In this lab, you are given a cipher-text that is
encrypted using a monoalphabetic cipher; namely, each letter in the original text is replaced by another
letter, where the replacement does not vary (i.e., a letter is always replaced by the same letter during the
encryption). Your job is to find out the original text using frequency analysis. It is known that the original
text is an English article.
In the following, we describe how we encrypt the original article, and what simplification we have made.
Instructors can use the same method to encrypt an article of their choices, instead of asking students to use
the ciphertext made by us.
• Step 1: let us generate the encryption key, i.e., the substitution table. We will permute the alphabet
from a to z using Python, and use the permuted alphabet as the key. See the following program.
#!/bin/env python3
import random

SEED Labs – Secret-Key Encryption Lab

3

s = "abcdefghijklmnopqrstuvwxyz"
list = random.sample(s, len(s))
key = ’’.join(list)
print(key)

• Step 2: let us do some simplification to the original article. We convert all upper cases to lower cases,
and then removed all the punctuations and numbers. We do keep the spaces between words, so you can
still see the boundaries of the words in the ciphertext. In real encryption using monoalphabetic cipher,
spaces will be removed. We keep the spaces to simplify the task. We did this using the following
command:
$ tr [:upper:] [:lower:] < article.txt > lowercase.txt
$ tr -cd ’[a-z][\n][:space:]’ < lowercase.txt > plaintext.txt

• Step 3: we use the tr command to do the encryption. We only encrypt letters, while leaving the space
and return characters alone.
$ tr ’abcdefghijklmnopqrstuvwxyz’ ’sxtrwinqbedpvgkfmalhyuojzc’ \
< plaintext.txt > ciphertext.txt

We have created a ciphertext using a different encryption key (not the one described above). It is included
in Labsetup.zip file, which can be downloaded from the lab’s website. Your job is to use the frequency
analysis to figure out the encryption key and the original plaintext.
We have also provided a Python program (freq.py) inside the Labsetup/Files folder. It reads
the ciphertext.txt file, and produces the statistics for n-grams, including the single-letter frequencies,
bigram frequencies (2-letter sequence), and trigram frequencies (3-letter sequence), etc.
$ ./freq.py
------------------------------------1-gram (top 20):
n: 488
y: 373
v: 348
...
------------------------------------2-gram (top 20):
yt: 115
tn: 89
mu: 74
...
------------------------------------3-gram (top 20):
ytn: 78
vup: 30
mur: 20
...

Guidelines. Using the frequency analysis, you can find out the plaintext for some of the characters quite
easily. For those characters, you may want to change them back to its plaintext, as you may be able to get
more clues. It is better to use capital letters for plaintext, so for the same letter, we know which is plaintext

SEED Labs – Secret-Key Encryption Lab

4

and which is ciphertext. You can use the tr command to do this. For example, in the following, we replace
letters a, e, and t in in.txt with letters X, G, E, respectively; the results are saved in out.txt.
$ tr ’aet’ ’XGE’ < in.txt > out.txt

There are many online resources that you can use. We list some useful links in the following:
• https://en.wikipedia.org/wiki/Frequency_analysis: This Wikipedia page provides frequencies for a typical English plaintext.
• https://en.wikipedia.org/wiki/Bigram: Bigram frequency.
• https://en.wikipedia.org/wiki/Trigram: Trigram frequency.

4

Task 2: Encryption using Different Ciphers and Modes

In this task, we will play with various encryption algorithms and modes. You can use the following
openssl enc command to encrypt/decrypt a file. To see the manuals, you can type man openssl
and man enc.
$ openssl enc -ciphertype -e -in plain.txt -out cipher.bin \
-K 00112233445566778889aabbccddeeff \
-iv 0102030405060708

Please replace the ciphertype with a specific cipher type, such as -aes-128-cbc, -bf-cbc,
-aes-128-cfb, etc. In this task, you should try at least 3 different ciphers. You can find the meaning
of the command-line options and all the supported cipher types by typing "man enc". We include some
common options for the openssl enc command in the following:
-in <file>
-out <file>
-e
-d
-K/-iv
-[pP]

5

input file
output file
encrypt
decrypt
key/iv in hex is the next argument
print the iv/key (then exit if -P)

Task 3: Encryption Mode – ECB vs. CBC

The file pic original.bmp is included in the Labsetup.zip file, and it is a simple picture. We
would like to encrypt this picture, so people without the encryption keys cannot know what is in the picture.
Please encrypt the file using the ECB (Electronic Code Book) and CBC (Cipher Block Chaining) modes,
and then do the following:
1. Let us treat the encrypted picture as a picture, and use a picture viewing software to display it. However, For the .bmp file, the first 54 bytes contain the header information about the picture, we have
to set it correctly, so the encrypted file can be treated as a legitimate .bmp file. We will replace the
header of the encrypted picture with that of the original picture. We can use the bless hex editor
tool (already installed on our VM) to directly modify binary files. We can also use the following
commands to get the header from p1.bmp, the data from p2.bmp (from offset 55 to the end of the
file), and then combine the header and data together into a new file.

SEED Labs – Secret-Key Encryption Lab

5

$ head -c 54 p1.bmp > header
$ tail -c +55 p2.bmp > body
$ cat header body > new.bmp

2. Display the encrypted picture using a picture viewing program (we have installed an image viewer
program called eog on our VM). Can you derive any useful information about the original picture
from the encrypted picture? Please explain your observations.
Select a picture of your choice, repeat the experiment above, and report your observations.

6

Task 4: Padding

For block ciphers, when the size of a plaintext is not a multiple of the block size, padding may be required.
The PKCS#5 padding scheme is widely used by many block ciphers (see Chapter 21.4 of the SEED book
for details). We will conduct the following experiments to understand how this type of padding works:
1. Use ECB, CBC, CFB, and OFB modes to encrypt a file (you can pick any cipher). Please report which
modes have paddings and which ones do not. For those that do not need paddings, please explain why.
2. Let us create three files, which contain 5 bytes, 10 bytes, and 16 bytes, respectively. We can use the
following "echo -n" command to create such files. The following example creates a file f1.txt
with length 5 (without the -n option, the length will be 6, because a newline character will be added
by echo):
$ echo -n "12345" > f1.txt

We then use "openssl enc -aes-128-cbc -e" to encrypt these three files using 128-bit AES
with CBC mode. Please describe the size of the encrypted files.
We would like to see what is added to the padding during the encryption. To achieve this goal, we
will decrypt these files using "openssl enc -aes-128-cbc -d". Unfortunately, decryption
by default will automatically remove the padding, making it impossible for us to see the padding.
However, the command does have an option called "-nopad", which disables the padding, i.e.,
during the decryption, the command will not remove the padded data. Therefore, by looking at the
decrypted data, we can see what data are used in the padding. Please use this technique to figure out
what paddings are added to the three files.
It should be noted that padding data may not be printable, so you need to use a hex tool to display the
content. The following example shows how to display a file in the hex format:
$ hexdump -C p1.txt
00000000 31 32 33 34 35 36 37 38 39 49 4a 4b 4c 0a
$ xxd p1.txt
00000000: 3132 3334 3536 3738 3949 4a4b 4c0a

7

|123456789IJKL.|
123456789IJKL.

Task 5: Error Propagation – Corrupted Cipher Text

To understand the error propagation property of various encryption modes, we would like to do the following
exercise:

SEED Labs – Secret-Key Encryption Lab

6

1. Create a text file that is at least 1000 bytes long.
2. Encrypt the file using the AES-128 cipher.
3. Unfortunately, a single bit of the 55th byte in the encrypted file got corrupted. You can achieve this
corruption using the bless hex editor.
4. Decrypt the corrupted ciphertext file using the correct key and IV.
Please answer the following question: How much information can you recover by decrypting the corrupted file, if the encryption mode is ECB, CBC, CFB, or OFB, respectively? Please answer this question
before you conduct this task, and then find out whether your answer is correct or wrong after you finish this
task. Please provide justification.

8

Task 6: Initial Vector (IV) and Common Mistakes

Most of the encryption modes require an initial vector (IV). Properties of an IV depend on the cryptographic
scheme used. If we are not careful in selecting IVs, the data encrypted by us may not be secure at all, even
though we are using a secure encryption algorithm and mode. The objective of this task is to help students
understand the problems if an IV is not selected properly. The detailed guidelines for this task is provided
in Chapter 21.5 of the SEED book.

8.1

Task 6.1. IV Experiment

A basic requirement for IV is uniqueness, which means that no IV may be reused under the same key. To
understand why, please encrypt the same plaintext using (1) two different IVs, and (2) the same IV. Please
describe your observation, based on which, explain why IV needs to be unique.

8.2

Task 6.2. Common Mistake: Use the Same IV

One may argue that if the plaintext does not repeat, using the same IV is safe. Let us look at the Output
Feedback (OFB) mode. Assume that the attacker gets hold of a plaintext (P1) and a ciphertext (C1) ,
can he/she decrypt other encrypted messages if the IV is always the same? You are given the following
information, please try to figure out the actual content of P2 based on C2, P1, and C1.
Plaintext (P1): This is a known message!
Ciphertext (C1): a469b1c502c1cab966965e50425438e1bb1b5f9037a4c159
Plaintext (P2): (unknown to you)
Ciphertext (C2): bf73bcd3509299d566c35b5d450337e1bb175f903fafc159

If we replace OFB in this experiment with CFB (Cipher Feedback), how much of P2 can be revealed?
You only need to answer the question; there is no need to demonstrate that.
The attack used in this experiment is called the known-plaintext attack, which is an attack model for
cryptanalysis where the attacker has access to both the plaintext and its encrypted version (ciphertext). If
this can lead to the revealing of further secret information, the encryption scheme is not considered as secure.

SEED Labs – Secret-Key Encryption Lab

7

Sample Code. We provide a sample program called sample code.py, which can be found inside the
Labsetup/Files folder. It shows you how to XOR strings (ascii strings and hex strings). The code is
shown in the following:
#!/usr/bin/python3
# XOR two bytearrays
def xor(first, second):
return bytearray(xˆy for x,y in zip(first, second))
MSG
= "A message"
HEX_1 = "aabbccddeeff1122334455"
HEX_2 = "1122334455778800aabbdd"
# Convert ascii/hex string to bytearray
D1 = bytes(MSG, ’utf-8’)
D2 = bytearray.fromhex(HEX_1)
D3 = bytearray.fromhex(HEX_2)
r1 = xor(D1, D2)
r2 = xor(D2, D3)
r3 = xor(D2, D2)
print(r1.hex())
print(r2.hex())
print(r3.hex())

8.3

Task 6.3. Common Mistake: Use a Predictable IV

From the previous tasks, we now know that IVs cannot repeat. Another important requirement on IV is that
IVs need to be unpredictable for many schemes, i.e., IVs need to be randomly generated. In this task, we
will see what is going to happen if IVs are predictable.
Assume that Bob just sent out an encrypted message, and Eve knows that its content is either Yes or
No; Eve can see the ciphertext and the IV used to encrypt the message, but since the encryption algorithm
AES is quite strong, Eve has no idea what the actual content is. However, since Bob uses predictable IVs,
Eve knows exactly what IV Bob is going to use next.
A good cipher should not only tolerate the known-plaintext attack described previously, it should also
tolerate the chosen-plaintext attack, which is an attack model for cryptanalysis where the attacker can obtain
the ciphertext for an arbitrary plaintext. Since AES is a strong cipher that can tolerate the chosen-plaintext
attack, Bob does not mind encrypting any plaintext given by Eve; he does use a different IV for each
plaintext, but unfortunately, the IVs he generates are not random, and they can always be predictable.
Your job is to construct a message and ask Bob to encrypt it and give you the ciphertext. Your objective
is to use this opportunity to figure out whether the actual content of Bob’s secret message is Yes or No. For
this task, your are given an encryption oracle which simulates Bob and encrypts message with 128-bit AES
with CBC mode. You can get access to the oracle by running the following command:
$ nc 10.9.0.80 3000
Bob’s secret message is either "Yes" or "No", without quotations.
Bob’s ciphertex: 54601f27c6605da997865f62765117ce
The IV used
: d27d724f59a84d9b61c0f2883efa7bbc
Next IV

: d34c739f59a84d9b61c0f2883efa7bbc

SEED Labs – Secret-Key Encryption Lab

8

Your plaintext : 11223344aabbccdd
Your ciphertext: 05291d3169b2921f08fe34449ddc3611
Next IV
: cd9f1ee659a84d9b61c0f2883efa7bbc
Your plaintext : <your input>

After showing you the next IV, the oracle will ask you to input a plaintext message (as a hex string).
The oracle will encrypt the message with the next IV, and outputs the new ciphertext. You can try different
plaintexts, but keep in mind that every time, the IV will change, but it is predictable. To simply your job, we
let the oracle print out the next IV. To exit from the interaction, press Ctrl+C.

8.4

Additional Readings

There are more advanced cryptanalysis on IV that is beyond the scope of this lab. Students can read the
article posted in this URL: https://defuse.ca/cbcmodeiv.htm. Because the requirements on IV
really depend on cryptographic schemes, it is hard to remember what properties should be maintained when
we select an IV. However, we will be safe if we always use a new IV for each encryption, and the new IV
needs to be generated using a good pseudo random number generator, so it is unpredictable by adversaries.
See another SEED lab (Random Number Generation Lab) for details on how to generate cryptographically
strong pseudo random numbers.

9

Task 7: Programming using the Crypto Library

This task is mainly designed for students in Computer Science/Engineering or related fields, where programming is required. Students should check with their professors to see whether this task is required for
their courses or not.
In this task, you are given a plaintext and a ciphertext, and your job is to find the key that is used for the
encryption. You do know the following facts:
• The aes-128-cbc cipher is used for the encryption.
• The key used to encrypt this plaintext is an English word shorter than 16 characters; the word can be
found from a typical English dictionary. Since the word has less than 16 characters (i.e. 128 bits),
pound signs (#: hexadecimal value is 0x23) are appended to the end of the word to form a key of
128 bits.
Your goal is to write a program to find out the encryption key. You can download a English word list
from the Internet. We have also included one in the Labsetup.zip file. The plaintext, ciphertext, and IV
are listed in the following:
Plaintext (total 21 characters): This is a top secret.
Ciphertext (in hex format): 764aa26b55a4da654df6b19e4bce00f4
ed05e09346fb0e762583cb7da2ac93a2
IV (in hex format):
aabbccddeeff00998877665544332211

You need to pay attention to the following issues:
• If you choose to store the plaintext message in a file, and feed the file to your program, you need to
check whether the file length is 21. If you type the message in a text editor, you need to be aware that
some editors may add a special character to the end of the file. The easiest way to store the message
in a file is to use the following command (the -n flag tells echo not to add a trailing newline):

SEED Labs – Secret-Key Encryption Lab

9

$ echo -n "This is a top secret." > file

• In this task, you are supposed to write your own program to invoke the crypto library. No credit will
be given if you simply use the openssl commands to do this task. Sample code can be found from
the following URL:
https://www.openssl.org/docs/man1.1.1/man3/EVP_CipherInit.html

• When you compile your code using gcc, do not forget to include the -lcrypto flag, because your
code needs the crypto library. See the following example:
$ gcc -o myenc myenc.c -lcrypto

Note to instructors. We encourage instructors to generate their own plaintext and ciphertext using a different key; this way students will not be able to get the answer from another place or from previous courses.
Instructors can use the following commands to achieve this goal (please replace the word example with
another secret word, and add the correct number of # signs to make the length of the string to be 16):
$ echo -n "This is a top secret." > plaintext.txt
$ echo -n "example#########" > key
$ xxd -p key
6578616d706c65232323232323232323
$ openssl enc -aes-128-cbc -e -in plaintext.txt -out ciphertext.bin \
-K 6578616d706c65232323232323232323 \
-iv 010203040506070809000a0b0c0d0e0f \
$ xxd -p ciphertext.bin
e5accdb667e8e569b1b34f423508c15422631198454e104ceb658f5918800c22

10

Submission

You need to submit a detailed lab report, with screenshots, to describe what you have done and what you
have observed. You also need to provide explanation to the observations that are interesting or surprising.
Please also list the important code snippets followed by explanation. Simply attaching code without any
explanation will not receive credits.

11

Acknowledgment

We would like to acknowledge the contribution made by the following people and organizations:
• Jiamin Shen developed the following: the code running inside the container, and the container version
of the task on predictable IV.
• The US National Science Foundation provided the funding for the SEED project from 2002 to 2020.
• Syracuse University provided the resources for the SEED project from 2001 onwards.
```

### Artifact I (run position 9, catalog P09)

Paste this as its own turn:

```
Artifact ID: I

ICS TECHNOLOGIES

**BASIC ****PLC ****Programming**** anD NETWORKING**

# SOFT PLC LAB SOLUTIONS

**Lab Description:  **In this lab, you will learn to program a software-based programmable logic controller, i.e., *soft PLC*, to control a lamp with multiple control contact switches. You will also learn to analyze industrial network traffic between the PLC and a Human Machine Interface (HMI) system, i.e., the “operator console”.

This lab consists of the following exercises:

- Introduction to ladder logic and MODBUS I/O

- MODBUS TCP/IP messaging

**Lab Environment: **The lab environment requires a Linux host system running the Ubuntu 14.04.4 LTS distribution and the Labtainer framework. The Linux host can be a virtual machine and must have Internet access. The Labtainer framework can be installed and run as described in the Labtainer Student Guide, available at: [https://my.nps.edu/web/cisr/labtainers](https://my.nps.edu/web/cisr/labtainers).

This lab uses the Linux soft PLC that is supported by the open-source OpenPLC project [1]. This soft PLC runs in a Docker container in the Labtainer framework.

In addition to the Labtainer framework, you will need to install the following applications on the Linux host system:

- PLCopen Editor v1.04 for MacOS and Linux. Available at: [http://www.openplcproject.com/plcopen-editor](http://www.openplcproject.com/plcopen-editor). You will use this tool to create ladder logic programs to run on the PLC.

- Radzio! Modbus Master Simulator. Available at: [http://en.radzio.dxp.pl/modbus-master-simulator/](http://en.radzio.dxp.pl/modbus-master-simulator/). This lab is tested with Radzio! version 0.2.2 (build date: February 10, 2017). This tool communicates with the PLC via the MODBUS TCP/IP protocol [2,3]. You will use this tool as the HMI to control the lamp and contact switches. This tool is a Windows program and is to be run with Wine (see below). 

- Wine Windows emulator. Binary package for Ubuntu 14.04.4 LTS can be installed using the *apt-get install* command. This lab is tested with Wine version 1.6.2. You will use this tool to run RadZio.

- Wireshark network protocol analyzer. Binary package for Ubuntu 14.04.4 LTS can be installed using the *apt-get install* command. This lab is tested with Wireshark version 1.12.1. You will use this tool to capture and analyze MODBUS traffic between the PLC and Radzio.

Lab Configuration

Figure 1 shows the software components required by this lab.

Figure 1. Lab configuration

The IP address used to communicate with the soft PLC varies and must be obtained after the lab is started (see section “Starting the Lab” below). 

Lab Installation

To set up this lab, do the following on your host system:

- Install the Labtainer framework. See the Labtainer Student Guide.

- Install the PLCopen Editor tool. Download the ZIP archive from [http://www.openplcproject.com/plcopen-editor](http://www.openplcproject.com/plcopen-editor). Uncompress the ZIP archive (PLCopen Editor v1.04 – Linux.zip) into a permanent directory on your Linux system. The default unzipped directory name is "PLCopen Editor".

- Download the sample Hello World ladder logic program (Hello_World.xml) from [http://www.openplcproject.com/getting-started-linux](http://www.openplcproject.com/getting-started-linux). The program is at the bottom of the page. Copy the file to the directory where the PLCopen Editor tool resides (see step 2 above).

- Install the following Python packages required by PLCopen Editor: *python-wxgtk2.8, pyro, python-numpy, python-nevow, python-matplotlib**,** *and *python-lxml**.* You can use the following command:

sudo apt-get install python-wxgtk2.8, pyro, python-numpy, python-nevow, python-matplotlib and python-lxml

- Install the Wine Windows emulator.

sudo apt-get install wine

- Install the Radzio! Modbus simulator. Download the ZIP archive from [http://en.radzio.dxp.pl/modbus-master-simulator/](http://en.radzio.dxp.pl/modbus-master-simulator/) to a permanent directory on your Linux system, e.g., ~/home/Radzio. Uncompress the ZIP archive (RMMS.zip). 

- Install the Wireshark protocol analyzer. Make sure to enable privileged users to run Wireshark.

sudo apt-get install wireshark

What you need to know to do the lab

This lab assumes the following:

- You have taken TCP/IP networking course(s);

- You are familiar with basic terminology and concepts on ICS, MODBUS, and MODBUS TCP/IP;

- You have hands-on experience with Wireshark. Minimally, the student must know how to filter a particular packet type, customize display columns, etc.

*Note for Instructors*

We suggest that this lab be conducted in a supervised lab environment, and that the following materials be covered at the beginning of the lab session:

- Labtainer installation, including installation of Virtual Box and a Linux VM (if a Linux system is not already available).  Refer to the Labtainer Student User Guide.

- Review of ICS fundamentals.

- Review of the MODBUS and MODBUS TCP/IP protocols.

- Review of tool usage, i.e., PLCopen Editor and Radzio!

Starting the Lab

Read through the entire lab before beginning. 

The lab is started from the Labtainer working directory on your host system. From there, issue the command:

./start.py softplc

The soft PLC automatically runs if the lab is successfully started. 

In the lab's virtual terminal, use the ifconfig command to get the IP address of the eth0 interface.

In the host system, do the following:

- Launch the browser   navigate to http://<eth0 address>:8080/

The Nodejs webserver should report that the PLC is running.

- In the browser, select “View PLC logs” to see the PLC’s log.

- Open a terminal and navigate to the Radzio directory.

- Launch Radzio! (wine RMMS.exe).

- In Radzio, select Connection  Settings. 

- Select Modbus TCP and enter the IP address of the eth0 interface and TCP port number 502 as shown in Figure 2.  Click OK.

Figure 2. Radzio! configuration

- Open another terminal and navigate to the PLCopen Editor directory.

- Launch PLCopen Editor (python PLCOpenEditor.py).

- Launch Wireshark and configure it to capture on the Docker interface (docker0).

OpenPLC I/O mapping

The MODBUS data model [2] consists of four data blocks with different characteristics. Figure 3 shows the data blocks and their corresponding data types. Each block can have up to 65536 data elements that are addressed from 0 to 65535. 

Figure 3. MODBUS Data Model [2]

The mapping between the MODBUS data blocks and the device I/O space is vendor specific [2]. Figure 4 shows the OpenPLC I/O address space [4]. 

Figure 4. OpenPLC I/O address space[4]

This lab only uses the Coil Registers and two MODBUS functions: Read Coils (function code=0x04) and Write Single Coil (function code=0x05). Refer to the MODBUS specification [2] for more details on these functions. Note that the data field of a Read Coils response contains the status of multiple coils, one bit per coil [2].

Radzio!, by default, only queries the statuses of ten coils, numbered from 1 to 10. The MODBUS addresses of these coils are 0x00 through 0x09. 

| Status bit | Coil Number | MODBUS address |
| --- | --- | --- |
| 0 | 1 | 0 |
| 1 | 2 | 1 |
| 2 | 3 | 2 |
| 3 | 4 | 3 |
| 4 | 5 | 4 |
| 5 | 6 | 5 |
| 6 | 7 | 6 |
| 7 | 8 | 7 |
| 8 | 9 | 8 |
| 9 | 10 | 9 |

**Lab Files that are N****eeded: **The sample Hello World program must be downloaded from the OpenPLC project and stored in the same directory where the PLCopen Editor source resides.

### **EXERCISE 1:**** ****Intro To ****LAdder LOGIC and MODBUS ****I/O**

The Hello World program is a simple ladder logic program that uses a button (contact switch) to control a lamp (coil) (Figure 5). The button and lamp are attached to PLC addresses %IX0.0 and %QX0.0, respectively. When the button is pressed and released, the lamp turns on for 2 seconds and then turns off [5].

Figure 5. PCLopen Editor display of Hello World program

The objective of this exercise is to familiarize you with ladder logic programming and MODBUS I/O operations. The Hello World program has a configuration bug that renders the button ineffective. Specifically, the state of the button cannot be changed because the button is located in a read-only area, i.e., the Discrete Input Register area in OpenPLC address space (Figure 4). 

Your task is to fix the bug so that the button can control the lamp and work through the questions below. For the lab report, you need to provide details using screen shots and description of the observed behavior.

**Read through the entire exercise before beginning.**

Activity 1: Fix the bug

In the host system, do the following:

- In the PLCopen Editor, open the Hello World project (Hello_World.xml) stored in the PLCopen Editor directory.

- Expand “Programs” and double-click “My_Program” to display the program in ladder logic.

- Change the location of the button to %QX0.1 (Figure 6).

Figure 6. Modified Hello World program

- Double-click the comment block  enter the following:

“<last name>: <brief statement about this activity>”

- Select File  Save As. Specify <last name>-Hello-World-mod.xml as the file name. Click Save.

- Select File  Generate Program. Specify <last name>-Hello-World-mod.st as the file name, and select “ST files (*.st)” as the file type. Click Save. 

The last step converts a graphical program into a Structured Text (ST) program, i.e., a program written in IEC 61131-3 Structured Text programming language [6]. OpenPLC only accepts input programs written in ST.

Activity 2: Upload the ST program to the PLC

In the host system, do the following:

- In the browser, navigate to the home page.

- Select “Browse”  select the <last name>-Hello-World-mod.st file. Click Open.

- Select “Upload Program”. The status string “Program compiled without errors!” should be returned.

- Navigate back to the home page.

- Select “View PLC logs”.

***Question 1.******1***: What are the last two messages recorded in the “OpenPLC Server” log? 

In the Labtainer virtual terminal, view the Node.js server’s log (nodejs.log) stored in the /var/log directory.

	sudo tail –f /var/log/nodejs.log

***Question 1.2***: What is the last message recorded in nodejs.log? 

Activity 3: Test the modified program

In the host system, do the following:

- In Radzio, select File  New.

- In the “ASCII display” box, click Enable.

- In the “+1” row (MODBUS address 0 which is the output address %QX0.0), enter “lamp” in the Alias cell.

- In the “+2” row (MODBUS address 0 which is the output address %QX0.1), enter “button” in the Alias cell (Figure 7).

Figure 7. Console interface

- Select File  “Save window as...”. Specify Hello-World-mod as the file name. Click Save. This action will create a file named Hello-World-mod.rmf in the Radzio directory.

- Select Connection  Connect. Once connected, Radzio! Starts polling the MODBUS devices. The state of each MODBUS address is reported in the cell next to the Alias cell.

- In the browser, navigate back to the home page.

- Select “View PLC logs”.

- Set the button variable to ON. In the “+2” row, double-click the cell after “button” (in the “0” column). A dialog window will appear. Click On  click Update.

***Question 1.5***: What are the states of the lamp and button?

- Set “button” to OFF.

***Question 1.6***: What are the states of the lamp and button?

***Question 1.******7***: Was the state of the lamp changed immediately after the button is set to OFF? Explain the observed behavior.

- Set “lamp” to ON.

***Question 1.8***: What are the states of the lamp and button? Explain the observed behavior.

- Set “button” to ON.

***Question 1.9***: What are the states of the lamp and button?

- Set “lamp” to OFF. 

***Question 1.10***: What are the states of the lamp and button? Explain the observed behavior.

- Select Connection  Disconnect.

- In the browser, navigate back to the home page.

- Select “View PLC logs”.

***Question 1.11***: What are the new messages recorded in the “OpenPLC Server” log?

 

In the Labtainer virtual terminal, view the syslog file.

	sudo tail –f /var/log/syslog

***Question 1.12***: How many “WriteCoil…” messages are in the syslog? Describe the correlation between the WriteCoil messages and the actions taken in steps 9-13 above.

Deliverables

You need to submit the following files for this exercise:

- A report (in PDF format) with answers to the listed questions. The report should include screen shots and explanation of the observed behavior.

- The programming files:

- <last name>-Hello-World-mod.xml

- <last name>-Hello-World-mod.st

- <last name>-Hello-World-mod.rmf

### **EXERCISE 2****:**** ****MODBUS TCP****/IP**** MESSAGING**

The MODBUS TCP/IP is used to transport MODBUS protocol data across a TCP/IP network. The MODBUS TCP/IP payload inside a TCP/IP packet consists of a MODBUS Application Protocol (MBAP) header and a MODBUS protocol data unit (PDU) [5] as shown in Figure 5 [3].

Figure 8. MODBUS TCP/IP payload format

The objective of this exercise to is to gain basic understanding of the MODBUS TCP/IP protocol. Your task is to create a simple ladder logic program to control a lamp using three contact switches, and use Wireshark to capture and inspect the MODBUS TCP/IP traffic between the Radzio and the PLC. 

For the lab report, you need to provide details using screen shots (including Wireshark displays) and description of the observed behavior.

**Read through the entire exercise before beginning**.

Activity 1: Create a new program

In the host system, do the following:

- Create a program that implements the following logic:

| **Coil/Switch** | **Address** |  |
| --- | --- | --- |
| lamp | %QX0.0 |  |
| master | %QX0.1 |  |
| sw1 | %QX0.3 |  |
| sw2 | %QX0.5 |  |

Set all “Initial Value” to zero.

- Save it as <last name>-three-switches.xml.

- Generate the ST file and name it as <last name>-three-switches.st.

- Upload the ST to the PLC.

- Verify that the program is running on the PLC. 

Activity 2: Test the new program

In the host system, do the following:

- In Wireshark, start capturing packets on the Docker interface (docker0).

- In Radzio, create a new file and program the MODBUS addresses used in your “three switches” program.

- Save the file as <last name>-three-switches.rmf.

- Connect to the PLC.

***Question ******2.1***: What are the states of the lamp and switches?

- Set “master” to ON.

***Question ******2******.2***: What are the states of the lamp and switches? Explain the observed behavior.

 

- Set “sw1” to ON.

***Question ******2.3***: What are the states of the lamp and button? Explain the observed behavior.

- Set “sw2” to ON.

***Question ******2.4***: What are the states of the lamp and button? Explain the observed behavior.

- Set “sw1” to OFF.

***Question ******2.5***: What are the states of the lamp and button? Explain the observed behavior.

- Set “sw2” to OFF. 

***Question ******2.6***: What are the states of the lamp and button? Explain the observed behavior.

- Disconnect Radzio.

- Stop the Wireshark capturing. Save the packet capture to a file named <last name>-three-switches.pcap.

In the Labtainer virtual terminal, view the syslog file.

	sudo tail –f /var/log/syslog

***Question ******2.7***: How many “WriteCoil…” messages are in the syslog? 

Activity 3: Analyze MODBUS TCP/IP traffic

In this activity, you need to analyze the PCAP file and correlate the captured Write Single Coil functions and the actions taken in Activity 2. 

Show your work with screen shots of the PCAP data used to answer the questions.

In the host system, do the following:

- Set Wireshark to use the MODBUS TCP/IP filter, i.e., mbtcp.

- Locate the first Write Single Coil request.

***Question 2.8***: What is the TCP port number used by Radzio to communicate with the PLC?

***Question 2.9***: What are the values of the MBAP header fields?

***Question 2.10***: What are the values of the MODBUS PDU fields?

***Question 2.11***: To which action in Activity 2 does this packet correspond? Describe how the “Reference Number” and “Data” fields relate to this action.

***Question 2.1******2***: What are the values of the data bits returned in the Read Coils response that precedes the Write Single Coil request? Describe how the bit values correspond to this action. 

***Question 2.13***: What are the values of the data bits returned in the Read Coils response that follows the Write Single Coil request? Describe how the bit values correspond to this action. 

- Locate the next Write Single Coil request. 

***Question 2.1******4***: What are the values of the MODBUS PDU fields?

***Question 2.1******5***: To which action in Activity 2 does this packet correspond? Describe how the “Reference Number” and “Data” fields relate to this action.

***Question 2.16***: What are the values of the data bits returned in the Read Coils response that precedes the Write Single Coil request? Describe how the bit values correspond to this action. 

***Question 2.17***: What are the values of the data bits returned in the Read Coils response that follows the Write Single Coil request? Describe how the bit values correspond to this action. 

- Locate the next Write Single Coil request. 

***Question 2.1******8***: What are the values of the MODBUS PDU fields?

***Question 2.******19***: To which action in Activity 2 does this packet correspond? Describe how the “Reference Number” and “Data” fields relate to this action.

***Question 2.20***: What are the values of the data bits returned in the Read Coils response that precedes the Write Single Coil request? Describe how the bit values correspond to this action. 

***Question 2.21***: What are the values of the data bits returned in the Read Coils response that follows the Write Single Coil request? Describe how the bit values correspond to this action. 

- Locate the next Write Single Coil request. 

***Question 2.******22***: What are the values of the MODBUS PDU fields?

***Question 2.******23***: To which action in Activity 2 does this packet correspond? Describe how the “Reference Number” and “Data” fields relate to this action.

***Question 2.24***: What are the values of the data bits returned in the Read Coils response that precedes the Write Single Coil request? Describe how the bit values correspond to this action. 

***Question 2.25***: What are the values of the data bits returned in the Read Coils response that follows the Write Single Coil request? Describe how the bit values correspond to this action. 

- Locate the next Write Single Coil request. 

***Question 2.******26***: What are the values of the MODBUS PDU fields?

***Question 2.******27***: To which action in Activity 2 does this packet correspond? Describe how the “Reference Number” and “Data” fields relate to this action.

***Question 2.28***: What are the values of the data bits returned in the Read Coils response that precedes the Write Single Coil request? Describe how the bit values correspond to this action. 

***Question 2.29***: What are the values of the data bits returned in the Read Coils response that follows the Write Single Coil request? Describe how the bit values correspond to this action. 

- In the browser, navigate back to the home page.

- Select “Stop” to stop the PLC.

Deliverables

You need to submit the following files for this exercise:

- A report (in PDF format) with answers to the listed questions. The report should include screen shots and explanation of the observed behavior.

- The programming files

- <last name>-three-switches.xml

- <last name>-three-switches.st

- <last name>-three-switches.rmf

- The PCAP file <last name>-three-switches.pcap.

## What to submit 

When you have completed the lab, run the following command from the Labtainer workspace directory:

	./stop.py softplc

Submit the resulting ZIP file along with a ZIP archive containing all deliverables listed in each exercise above.

## References

[1] 	The OpenPLC project. [http://www.openplcproject.com/](http://www.openplcproject.com/)

[2] 	Modbus Organization, “MODBUS Application Protocol Specification V1.1b3,” April 26, 2012. [http://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf](http://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf)

[3] 	Modbus Organization, “MODBUS Messaging on TCP/IP Implementation Guide V1.0b,” October 24, 2006. [http://www.modbus.org/docs/Modbus_Messaging_Implementation_Guide_V1_0b.pdf](http://www.modbus.org/docs/Modbus_Messaging_Implementation_Guide_V1_0b.pdf)

[4] 	The OpenPLC Project, “SCADA Supervisory Software”. [http://www.openplcproject.com/scada](http://www.openplcproject.com/scada)

[5]	The OpenPLC Project, “Running the first project”. http://www.openplcproject.com/getting-started-linux

[6]	PLCopen, “Introduction into IEC 61131-3 Programming Languages”. http://www.plcopen.org/pages/tc1_standards/iec_61131_3/

This lab was developed by the Center for Cybersecurity and Cyber Operations at the Naval Postgraduate School in Monterey California by Thuy D Nguyen.

	 Page | 19 

  This document is licensed with a Creative Commons Attribution 4.0 International License ©2017 Catalyzing Computing and Cybersecurity in Community Colleges (C5). 

	 Page | 1 

  This document is licensed with a Creative Commons Attribution 4.0 International License ©2017
```

### Artifact J (run position 10, catalog P04)

Paste this as its own turn:

```
Artifact ID: J

## Slide 1

Cyber Ethics

A Capstone CCL

## Slide 2

Learning Objectives

Upon completion of this CCL: 
Students will be able to define cyber ethics.   
Students will be able to explain the significance of cyber ethics in the areas of privacy, security, and other areas of ethical concern. 
Students will create a position paper/video/debate which states a position and presents evidence supporting their assumptions.

## Slide 3

How digital (cyber) technology enhances our lives…

Digital technology is routinely used to enhance pre-digital technological products and processes.
It has also given rise to brand-new products and processes that have made it possible for new products, processes, and activities to exist. These include:
Computers
Software
The Internet and the World Wide Web     

## Slide 4

What is unique about cyber technology’s capabilities?

The speed with which all these technologies perform their functions.   
The scope of technologies that support communication and data transfer.
The impact of these technologies malfunctioning. 
The ease of access to information that is provided by many of these technologies.    

## Slide 5

Cyber ethics

We define cyber ethics as the ethical issues that arise in these phases of a cyber technology product, system or process: 
Development
Deployment 
Implementation 

## Slide 6

Stakeholders

These are the people, organizations, and societies that are impacted by an incident.
Stakeholders may have a variety of values at stake.
Let’s brainstorm what kinds of stakeholder values can be vulnerable to security lapses in any situation.

## Slide 7

Accountability

When security problems arise, accountability must be assigned. Why?
Identify what responsibility (if any) the stakeholders deserve for the security breach. 

## Slide 8

What position will you defend?

So, now what? We have examined the errors made, identified the stakeholders, and assigned accountability.
Each person should construct a just and practical position for the future. 

## Slide 9

Examination of Question & Position

Choose a question from the list.
State your position at the outset
Summarize the problem as you see it
Based on the summary, organize and outline your viewpoint on the issue
In your position paper, you should present the opposing sides including factual knowledge, statistical evidence, authoritative testimony, etc., and refute the opposition as a way of strengthening your position
Present your approach to solving a problem
Refer to those who agree with your position to assist you in developing your argument
Let your passion be demonstrated in the force of your argument rather than in the use of emotional terms

## Slide 10

Outline of Paper (2-3 pages)	

Introduction of Your Position:
Start with a topic sentence or two that attracts attention and summarizes the issue
Inform the reader of your point of view
Development of Your Position:
Focus on three-four main points that support your position.  These are both positive claims about who you think is to blame and what should be done as well as negative claims countering opposing views.  Each point is developed with
a general statement of the position
an elaboration that references documents and source data
past experiences and authoritative testimony
conclusion restating the position

## Slide 11

Establish Flow of the Paper

Keep your voice active
Quote sources to establish authority
Stay focused on your point of view throughout the essay
Focus on logical arguments
Don't lapse into summary
in the development--wait for the conclusion

## Slide 12

Conclusion

Summarize, then conclude, your argument
Refer to the first paragraph/opening statements
as well as the main points
Does the conclusion restate the main ideas?
Reflect the succession and importance of the arguments
Logically conclude their development?
Grading of the Position Paper will follow the rubric.

## Slide 13
```
