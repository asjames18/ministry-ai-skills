# GitHub Launch Checklist: Ministry AI Skills 🚀

This checklist provides everything needed to publish and launch **Ministry AI Skills** publicly on GitHub.

---

## 📌 Repository Identity & Metadata

- **Repository Name**: `ministry-ai-skills`
- **GitHub URL**: `https://github.com/asjames18/ministry-ai-skills`
- **Project Display Name**: Ministry AI Skills
- **Visibility**: Public
- **License**: MIT License
- **Copyright**: `Copyright (c) 2026 Antonio James and Ministry AI Skills Contributors`

### Exact GitHub Description
```text
Open-source, platform-agnostic AI skills, prompts, workflows, and guardrails for churches and Christian ministries.
```

### Exact GitHub Topics (Tags)
```text
church-tech, ministry-ai, christian-ministry, ai-prompts, prompt-engineering, llm-agents, pastoral-care, church-management, melanated-in-tech, open-source
```

---

## 📋 Pre-Flight Launch Checklist

- [x] Standardize repository name (`ministry-ai-skills`) and display name.
- [x] Verify MIT License with copyright notice.
- [x] Validate all 5 starter skills against standard 6-file format (`scripts/validate_skills.py`).
- [x] Verify `skills/catalog.json` schema matches actual folder structure and inputs.
- [x] Configure GitHub issue templates and `.github/ISSUE_TEMPLATE/config.yml`.
- [x] Add clear "Who This Is For", "What This Is Not", and "Responsible Use" sections to README.
- [x] Provide clear instructions for running the validator script.
- [ ] Configure GitHub Repository Settings:
  - [ ] Set GitHub description and website link (if applicable).
  - [ ] Apply all GitHub topics listed above.
  - [ ] Enable GitHub Discussions (Announcements, General, Ideas, Q&A).
  - [ ] Enable GitHub Issues.
  - [ ] Enable GitHub Security Advisories.
- [ ] Update security contact email placeholder in [`SECURITY.md`](../SECURITY.md) to your active email.

---

## 💡 First GitHub Issues to Open (Good First Issues)

1. **`feat(skills): add volunteer-scheduling-comms skill`**
   - *Description*: Create the 6-file package for generating volunteer reminder texts, sub requests, and appreciation notes.
   - *Labels*: `enhancement`, `good first issue`, `skill-contribution`

2. **`feat(skills): add small-group-curriculum generator skill`**
   - *Description*: Create the 6-file package for transforming sermon manuscripts/themes into a 4-week small group discussion guide.
   - *Labels*: `enhancement`, `help wanted`, `skill-contribution`

3. **`ci: add GitHub Action to validate skills and catalog automatically`**
   - *Description*: Set up `.github/workflows/validate.yml` to run `python scripts/validate_skills.py` on all PRs and pushes.
   - *Labels*: `ci/cd`, `good first issue`

4. **`i18n: add Spanish translation support for starter skills`**
   - *Description*: Translate prompts and schemas into Spanish for Spanish-speaking congregations.
   - *Labels*: `internationalization`, `help wanted`

5. **`docs: add n8n automation blueprint for first-time-guest-follow-up`**
   - *Description*: Contribute an exported n8n workflow JSON that triggers the guest follow-up skill via webhook.
   - *Labels*: `documentation`, `integrations`

---

## 💬 First GitHub Discussion Topics

1. **Category: Announcements**
   - **Title**: Welcome to Ministry AI Skills! 🕊️
   - **Body**: Welcome to the Ministry AI Skills open-source community. Introduce yourself, what church or ministry you serve, and how you hope to use AI responsibly in your ministry context.

2. **Category: Ideas**
   - **Title**: Which ministry AI skill should we build next?
   - **Body**: Check out our `ROADMAP.md`. Which workflows or administrative tasks take up the most time in your ministry week? Vote or suggest new ideas.

3. **Category: Q&A**
   - **Title**: Best practices for Zero Data Retention and member privacy in church AI
   - **Body**: A thread to discuss safe AI models, local LLMs (Ollama/LM Studio), and enterprise zero-retention API endpoints for church data.

---

## 🗺️ First 10 Skills Roadmap

| # | Skill Folder | Ministry Focus | Status |
|---|---|---|---|
| 1 | `skills/weekly-announcements` | Communications & Multi-Channel Copy | 🟢 Live |
| 2 | `skills/sermon-prep-support` | Exegetical Research & Homiletic Scaffolding | 🟢 Live |
| 3 | `skills/church-event-planning` | Operations, Run-of-Show & Logistics | 🟢 Live |
| 4 | `skills/first-time-guest-follow-up` | Hospitality & Multi-Touch Welcome | 🟢 Live |
| 5 | `skills/church-media-pack` | Creative, Image Prompts & Slide Copy | 🟢 Live |
| 6 | `skills/prayer-request-routing` | Care Team Categorization & Anonymization | 🟡 Next Up |
| 7 | `skills/small-group-curriculum` | Sermon-to-Curriculum Transformation | 🟡 Next Up |
| 8 | `skills/volunteer-scheduling-comms` | Volunteer Reminders & Encouragement | 🟡 Next Up |
| 9 | `skills/pastoral-care-drafter` | Compassionate Check-in & Condolence Drafts | 🟡 Next Up |
| 10 | `skills/kids-ministry-activity-pack` | Object Lessons, Craft Ideas & Lesson Plans | 🟡 Next Up |

---

## 💻 Git Initialization & First Push Commands

Run the following commands in the project root directory:

```bash
# 1. Initialize git repository (if not already initialized)
git init

# 2. Stage all files
git add .

# 3. Create the initial commit
git commit -m "Initial open-source ministry AI skills library"

# 4. Set default branch to main
git branch -M main

# 5. Add remote GitHub repository
git remote add origin https://github.com/asjames18/ministry-ai-skills.git

# 6. Push to GitHub
git push -u origin main
```
