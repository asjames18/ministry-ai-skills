# Contributing to Ministry AI Skills

Thank you for your interest in contributing to **Ministry AI Skills**! 

This project exists to equip local churches, ministries, and faith-based organizations with high-quality, ethically grounded, and practically useful AI workflows.

Whether you are a pastor, a church volunteer, a ministry communicator, an AI engineer, or a technical developer, your contributions are welcome.

---

## 🕊️ Our Core Principles for Contributions

Before contributing, please keep these core tenets in mind:

1. **Ministry First, Tech Second**: Skills should solve genuine ministry friction, not just demonstrate AI novelties.
2. **Humility & Theological Respect**: Maintain neutrality across orthodox Christian traditions unless creating a tradition-specific module. Avoid divisive arguments.
3. **Ironclad Privacy**: Never include personal, sensitive, or identifying real-world data in examples or tests.
4. **Simplicity & Portability**: Keep skills platform-agnostic so any church can use them regardless of their tech stack.

---

## 🛠️ Ways You Can Contribute

1. **Author a New Skill**: Have a workflow for youth retreats, prayer chains, or budget reviews? Build a new skill using our template.
2. **Improve Existing Skills**: Enhance prompts, add richer examples, refine JSON schemas, or sharpen guardrails.
3. **Create Integrations & Adapters**: Build examples for n8n, LangChain, CrewAI, Dify, or custom platforms in `docs/platform-guides.md`.
4. **Fix Typos & Refine Documentation**: Clarity and ease-of-use are critical for non-technical ministry workers.

---

## 📁 Skill Structure Requirements

Every skill must be added under `skills/<skill-name>/` and contain the following 6 mandatory files:

| File | Purpose |
|---|---|
| `README.md` | Skill summary, target ministry role, prerequisites, and expected outputs. |
| `prompt.md` | The core prompt template with placeholders (`{{variable}}`). |
| `inputs.schema.json` | Valid JSON Schema (draft-07) documenting all input properties. |
| `workflow.md` | Human + AI step-by-step procedure from raw input to final human approval. |
| `guardrails.md` | Explicit boundaries on theology, safety, confidentiality, and tone. |
| `examples.md` | At least 2 realistic end-to-end examples with inputs and sample outputs. |

> 💡 **Tip**: Copy from [`templates/skill-template/`](../templates/skill-template/) when starting a new skill.

---

## 🚀 Step-by-Step Contribution Workflow

### 1. Fork & Clone the Repository
```bash
git clone https://github.com/asjames18/ministry-ai-skills.git
cd ministry-ai-skills
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/add-small-group-skill
```

### 3. Build or Modify Your Skill
- Create your skill folder under `skills/<skill-name>/`.
- Use lowercase alphanumeric characters and hyphens for folder names (kebab-case).
- Validate your `inputs.schema.json` with any standard JSON schema validator.

### 4. Review Quality Checklist
Before submitting a pull request, ensure:
- [ ] The skill includes all 6 standard files (`README.md`, `prompt.md`, `inputs.schema.json`, `workflow.md`, `guardrails.md`, `examples.md`).
- [ ] Added/updated entry in [`skills/catalog.json`](skills/catalog.json).
- [ ] No real church members' personal data (emails, phone numbers, counseling notes, medical prayer requests) is included in examples.
- [ ] Theological guardrails specify human pastoral review and Scripture verification.
- [ ] Prompts do not generate manipulative financial appeals or claim infallible biblical authority.
- [ ] Markdown is cleanly formatted with clear headers and bullet points.

### 5. Submit Your Pull Request
- Provide a clear PR title (e.g., `feat(skills): add volunteer-scheduling skill`).
- Describe the ministry problem solved and provide a quick summary of the workflow.

---

## 💬 Questions & Community Support

Have an idea for a skill or want to discuss ministry AI ethics? Open an Issue or start a Discussion on GitHub. We look forward to building together!
