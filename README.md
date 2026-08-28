# Ministry AI Skills 🕊️

> **An open-source, platform-agnostic library of reusable AI skills, prompts, workflows, guardrails, and examples for churches, ministries, and faith-based organizations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Platform Agnostic](https://img.shields.io/badge/Platform-Agnostic-orange.svg)](#-platform-compatibility)
[![Ministry AI](https://img.shields.io/badge/Ministry-AI%20Skills-purple.svg)](docs/project-positioning.md)

---

## 🎯 Mission & Core Conviction

Ministry teams—from solo pastors and bi-vocational leaders to large church staffs and faithful volunteers—often struggle under heavy administrative loads, communication bottlenecks, and burnout. 

**Ministry AI Skills** provides an open, trusted, modular collection of AI skills tailored specifically for real-world ministry workflows. 

> ### 🕊️ Core Conviction
> **AI assists ministry; it never replaces pastors, church leadership, prayer, spiritual discernment, Scripture, accountability, or real human care.**

---

## 👥 Who This Is For

- **Solo & Bi-Vocational Pastors**: Quickly draft exegetical research scaffolds, illustration brainstorms, and sermon discussion questions without losing hours of study time.
- **Church Administrative Staff & Communicators**: Turn raw event notes into synchronized stage announcements, bulletin blurbs, email newsletters, and presentation slide copy in minutes.
- **Ministry Directors & Event Coordinators**: Generate minute-by-minute run-of-show schedules, volunteer matrices, promotional timelines, and safety checklists.
- **Hospitality & Connections Teams**: Craft warm, respectful, multi-channel first-time visitor follow-up sequences that honor personal privacy.
- **Media & Creative Volunteers**: Produce prompt recipes for Midjourney/DALL-E, Instagram carousels, slide copy, and video hooks aligned with sermon themes.
- **Christian Technologists & Developers**: Build custom agents, n8n automations, Custom GPTs, or ChMS integrations on top of validated, open-source prompts and JSON schemas.

---

## 🛑 What This Is Not

- **NOT a replacement for pastoral care**: AI cannot visit hospital beds, counsel grieving families, baptize believers, or offer spiritual fatherhood.
- **NOT an authoritative biblical interpreter**: AI outputs are research and drafting aids; pastoral oversight, prayerful discernment, and Scripture verification are mandatory.
- **NOT a tool for manipulative fundraising**: We strictly prohibit prompts that generate guilt-based appeals or prosperity promises. Generosity must be cheerful and biblical.
- **NOT a closed commercial product**: This repository is 100% open-source under the MIT License.
- **NOT a data harvester**: We do not collect, store, or train on church data. All workflows emphasize anonymization and zero data retention.

---

## 📦 Skill Anatomy (The Standard 6-File Format)

Instead of building one giant, unpredictable chatbot, this repository organizes AI capabilities into **discrete, modular skills**. Each skill represents a specific ministry workflow and lives in its own folder under `skills/`:

```text
skills/skill-name/
├── README.md             # Overview, purpose, target audience, and output formats
├── prompt.md             # The reusable, production-ready system/task prompt template
├── inputs.schema.json    # Standard JSON Schema (draft-07) defining inputs & types
├── workflow.md           # Step-by-step human + AI execution process & handoffs
├── guardrails.md         # Ethical, theological, safety, and privacy boundaries
└── examples.md           # Realistic sample inputs and validated example outputs
```

Every skill is designed to work standalone in a chat window (ChatGPT, Claude) or programmatically via AI agent frameworks and automation tools.

---

## 🚀 Starter Skills Included

| Skill | Category | Description | Primary Users |
|---|---|---|---|
| [**Weekly Announcements**](skills/weekly-announcements/) | Communication | Transforms raw ministry notes into bulletin copy, stage scripts, email digests, and slides. | Church Admins, Stage Hosts, Media Teams |
| [**Sermon Prep Support**](skills/sermon-prep-support/) | Teaching & Discipleship | Contextual research, exegetical outlines, Greek/Hebrew term spotlights, illustrations, and small group questions. | Pastors, Preachers, Bible Teachers |
| [**Church Event Planning**](skills/church-event-planning/) | Operations | Complete event run-of-show, promotion schedule, volunteer staffing matrix, and safety checklists. | Event Coordinators, Ministry Directors |
| [**First-Time Guest Follow-Up**](skills/first-time-guest-follow-up/) | Hospitality & Care | Multi-channel, warm, low-pressure follow-up sequences (Day 0 SMS, Day 2 pastoral email, card scripts). | Welcome Teams, Assimilation Pastors |
| [**Church Media Pack**](skills/church-media-pack/) | Creative & Media | Generates slide copy, social captions, AI image generation prompts (Midjourney/DALL-E), and video hooks. | Media Teams, Graphic Designers |

---

## 🛡️ Responsible Use & Ministry Boundaries

All skills in this repository are engineered with strict boundary principles:

1. **Theological Humility & Scripture Verification**: All biblical references and doctrinal claims must be reviewed by church leadership against Scripture. AI has no spiritual authority.
2. **Confidentiality & Privacy**: Never enter real personal details, counseling notes, unvetted prayer requests, financial giving records, or children's names into commercial AI tools without zero-data-retention agreements.
3. **Pastoral Discretion in Care**: High-sensitivity pastoral care, grief counseling, and crisis intervention must be handled directly by qualified human leaders.
4. **Biblical Generosity Over Manipulation**: Giving copy must focus on joyful discipleship and biblical stewardship, never guilt, pressure, or transactional promises.
5. **Human-in-the-Loop Always**: AI drafts; human ministry leaders discern, edit, and approve before anything is shared.

For detailed guidelines, see [`docs/theological-and-ethical-framework.md`](docs/theological-and-ethical-framework.md) and [`docs/privacy-and-data-handling.md`](docs/privacy-and-data-handling.md).

---

## ⚡ Quick Start for Churches (No Code)

You do not need to be a programmer to use these skills in your church:

1. **Pick a Skill**: Browse the `skills/` directory above and choose the workflow you need (e.g., [`weekly-announcements`](skills/weekly-announcements/)).
2. **Copy the Prompt**: Open `prompt.md` and copy the entire text.
3. **Paste into Your AI Tool**: Paste it into [ChatGPT](https://chat.openai.com), [Claude](https://claude.ai), [Gemini](https://gemini.google.com), or Microsoft Copilot.
4. **Provide Your Details**: Fill in your church's specific information where indicated.
5. **Review & Refine**: Review the draft, customize the voice, and apply pastoral discernment before publishing.

---

## 🛠️ Quick Start for Contributors & Developers

Developers and integrators can use the schemas and prompts to build automations, agentic workflows, or new skills:

### 1. Clone the Repository
```bash
git clone https://github.com/asjames18/ministry-ai-skills.git
cd ministry-ai-skills
```

### 2. Validate All Skills
Run the built-in validator to verify that all skill folders meet the 6-file standard and match `catalog.json`:
```bash
python scripts/validate_skills.py
```

### 3. Create a New Skill
Use our standard template to contribute a new skill:
```bash
cp -r templates/skill-template skills/your-new-skill-name
```
Then author the 6 files following our [Skill Authoring Guide](docs/skill-authoring-guide.md) and update [`skills/catalog.json`](skills/catalog.json).

---

## 💻 Platform Compatibility

Ministry AI Skills are **100% platform-agnostic**. You can use them with:

- **Direct Chat**: Copy and paste into [ChatGPT](https://chat.openai.com), [Claude](https://claude.ai), [Gemini](https://gemini.google.com), or Microsoft Copilot.
- **Custom Assistants**: Build Custom GPTs, Claude Projects, or Poe Bots.
- **Workflow Automation**: Integrate with [n8n](https://n8n.io), [Make](https://make.com), or Zapier.
- **AI Agent Frameworks**: Implement via [LangChain](https://www.langchain.com/), [CrewAI](https://www.crewai.com/), [OpenAI Agents SDK](https://github.com/openai/openai-agents-python), [Dify](https://dify.ai/), or custom web applications.

Check out our [Platform Integration Guides](docs/platform-guides.md) for tutorials and snippets.

---

## 📁 Repository Structure

```text
.
├── LICENSE                        # MIT License
├── README.md                       # Project overview and catalog
├── AGENTS.md                       # AI coding agent instructions & repo rules
├── CONTRIBUTING.md                 # Contributor guidelines
├── CODE_OF_CONDUCT.md              # Community standards & behavioral expectations
├── ROADMAP.md                      # Strategic vision & planned skill releases
├── SECURITY.md                     # Data privacy & security policy
├── .gitignore                      # Git exclusion rules
├── .github/                        # GitHub issue & PR templates
│   ├── ISSUE_TEMPLATE/
│   │   ├── config.yml              # Issue template configuration
│   │   ├── bug_report.md
│   │   └── skill_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── scripts/                        # Repository tooling
│   └── validate_skills.py          # Zero-dependency skill & catalog linter
├── docs/                           # Extended documentation
│   ├── project-positioning.md      # Plain-language project vision & ecosystem context
│   ├── launch-checklist.md         # GitHub launch & release checklist
│   ├── getting-started.md          # Guide for non-technical leaders & developers
│   ├── theological-and-ethical-framework.md # Theological safety & ethics
│   ├── privacy-and-data-handling.md# Handling sensitive church data
│   ├── platform-guides.md          # How to connect skills to various AI tools
│   └── skill-authoring-guide.md    # How to create new skills
├── templates/                      # Standardized boilerplate
│   └── skill-template/             # Starter template for new skill contributions
│       ├── README.md
│       ├── prompt.md
│       ├── inputs.schema.json
│       ├── workflow.md
│       ├── guardrails.md
│       └── examples.md
└── skills/                         # Modular skill directory
    ├── catalog.json                # Machine-readable skill index
    ├── weekly-announcements/
    ├── sermon-prep-support/
    ├── church-event-planning/
    ├── first-time-guest-follow-up/
    └── church-media-pack/
```

---

## 🌐 Ecosystem Note

**Ministry AI Skills** is designed as a standalone, vendor-neutral library. In the future, community platforms such as *OpenChurch AI* and various church management systems may build tools, web interfaces, and agent integrations powered by these open skills.

---

## 🤝 Contributing & Community

We welcome contributions from pastors, ministry leaders, church communicators, prompt engineers, and software developers!

- 📖 **How to Contribute**: Read our [Contributing Guide](CONTRIBUTING.md) and [Skill Authoring Guide](docs/skill-authoring-guide.md).
- 📜 **Code of Conduct**: Review our community guidelines in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- 🔒 **Security & Privacy Policy**: Review our data protection guidelines in [SECURITY.md](SECURITY.md).
- 🗺️ **Roadmap**: See our planned skills and milestones in [ROADMAP.md](ROADMAP.md).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free for churches, non-profits, commercial tools, and open-source contributors to use, modify, and distribute.

Copyright (c) 2026 Antonio James and Ministry AI Skills Contributors.
