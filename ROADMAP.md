# Ministry AI Skills Roadmap 🗺️

This document outlines the strategic direction, planned skill expansions, community tooling, and architectural goals for **Ministry AI Skills**.

---

## 🎯 Vision

To build the world's most trusted, modular, and practical open-source library of AI skills, workflows, and guardrails for local churches, ministry teams, and Christian non-profits worldwide.

---

## 📅 Milestones & Planned Releases

### Phase 1: Core Foundation & Starter Skills (Current)
- [x] Establish modular repository architecture (`README`, `AGENTS.md`, `CONTRIBUTING.md`, `LICENSE`, `SECURITY.md`).
- [x] Deliver standard 6-file skill template (`templates/skill-template/`).
- [x] Complete comprehensive documentation (`docs/`).
- [x] Launch 5 flagship starter skills:
  - [x] `weekly-announcements` (Communication)
  - [x] `sermon-prep-support` (Teaching & Discipleship)
  - [x] `church-event-planning` (Operations)
  - [x] `first-time-guest-follow-up` (Hospitality & Care)
  - [x] `church-media-pack` (Creative & Social)
- [x] Machine-readable `skills/catalog.json` index.

---

### Phase 2: Care, Discipleship & Administration Skills (Next Up)
- [ ] **`prayer-request-routing`**: Safe, anonymized categorization and notification dispatch for pastoral prayer teams.
- [ ] **`small-group-curriculum`**: Transform sermon notes or passage themes into 4-6 week small group discussion guides with leader notes.
- [ ] **`volunteer-scheduling-comms`**: Polite, encouraging volunteer reminder texts, sub requests, and appreciation messages.
- [ ] **`pastoral-care-drafter`**: Compassionate, unhurried message drafts for hospital visits, condolences, and member check-ins.
- [ ] **`kids-ministry-activity-pack`**: Age-appropriate object lessons, crafts, games, and volunteer lesson plans.
- [ ] **`youth-ministry-discussion-guide`**: Relatable cultural engagement discussions and small group prompts for middle/high schoolers.
- [ ] **`church-meeting-agenda-minutes`**: Format elder, deacon, committee, and staff meeting agendas and action item summaries.
- [ ] **`biblical-stewardship-comms`**: Transparent, non-manipulative giving campaign communications and quarterly financial updates.
- [ ] **`community-outreach-planner`**: Neighborhood service project coordination, supply lists, and volunteer briefing sheets.
- [ ] **`church-website-content-writer`**: Clear, seeker-friendly "What to Expect", "About Us", and ministry department web copy.

---

### Phase 3: Platform Adapters & Community Tooling
- [ ] **JSON Schema Validation CI Workflow**: GitHub Actions workflow to automatically validate `inputs.schema.json` files on every PR.
- [ ] **No-Code Web Directory**: Simple searchable web interface for pastors and volunteers to copy prompts without touching GitHub.
- [ ] **1-Click Custom GPTs & Claude Artifacts**: Pre-packaged links to import skills directly into ChatGPT and Claude Projects.
- [ ] **n8n & Make Automation Blueprints**: Downloadable workflow JSON files connecting Planning Center, Google Forms, and Mailchimp.
- [ ] **LangChain / LangGraph & CrewAI Reference Packages**: Python/TypeScript reference implementations for multi-agent ministry coordination.

---

### Phase 4: Multilingual & Internationalization
- [ ] Spanish localization for all core skills.
- [ ] Portuguese localization.
- [ ] French and German translations.
- [ ] Cross-cultural ministry communication adaptations.

---

## 🤝 How to Suggest or Champion a Skill

1. Check our [Skill Authoring Guide](docs/skill-authoring-guide.md).
2. Open a [Skill Request Issue](.github/ISSUE_TEMPLATE/skill_request.md).
3. Submit a Pull Request following our [Contributing Guide](CONTRIBUTING.md).
