# AI & Payload Generation 🤖 💻 
This repository is a collection of markdown file generated with AI about payload generation. The content of the files was generated only for **educational purposes** 
for my thesis and should not be used for malicious purposes. The objective of this study is to explore how AI can be used for payload generation and how cybersecurity tools can be integrated with LLMs.

## List of tools used :space_invader: 
- [Metasploit](https://github.com/rapid7/metasploit-framework)
- [Covenant](https://github.com/cobbr/Covenant)
- [Pupy](https://github.com/n1nj4sec/pupy)
- [Sliver](https://github.com/BishopFox/sliver)
- [Empire](https://github.com/BC-SECURITY/Empire)

## How it works 💡
The system works by taking a prompt input from the user and, through the RAG (Retrieval Augmented Generation) system, gathers the necessary information to provide a response. The output from the RAG is then fed into an LLM, which generates the final response for payload generation.

![schema](https://github.com/user-attachments/assets/3d6f9946-b520-42ac-8793-8ff7a1fe4e08)

## Example of usage 💻 
This example uses a DLL payload generated with the LLM built into this repository. The attack follows these steps:
- Malicious archive: The goal is to launch the DLL without the victim being aware. For this reason we use a `SFX archive` which opens a pdf and launches a `poweshell` script that modifies the windows registry and downloads the DLL from the attacker machine.
- Compromised website: This component is the most important in the attack because that is the point where the victim downloads the malicious archive with the launcher. This component can also be used for phishing.
- Second powershell script: This script will be created if the SFX archive extracts itself, and it will be launched at the victim's logon to the operating system.

