# Skill Authoring Guide

This guide walks you through creating a high-quality, standardized skill for the **Ministry AI Skills** repository.

---

## 🏗️ The 6 Required Files

Every skill directory in `skills/<skill-name>/` must contain:

```text
skills/your-skill-name/
├── README.md             # Overview, target roles, inputs, and outputs
├── prompt.md             # The reusable, production-ready system prompt
├── inputs.schema.json    # JSON Schema definition of inputs
├── workflow.md           # Operational steps (input -> AI -> human review -> delivery)
├── guardrails.md         # Ethical, theological, privacy, and tone boundaries
└── examples.md           # Realistic input and output examples
```

---

## 📝 Step-by-Step Instructions

### Step 1: Copy the Template
Copy the folder `templates/skill-template/` to `skills/<your-skill-name>/`.
Use lowercase alphanumeric characters with hyphens (e.g., `prayer-request-routing` or `small-group-curriculum`).

### Step 2: Write `README.md`
- Explain the real ministry problem this skill addresses.
- Define who the primary user is (e.g., Senior Pastor, Youth Director, Church Administrator).
- Summarize the inputs required and the output formats generated.

### Step 3: Define `inputs.schema.json`
- Use [JSON Schema Draft-07](https://json-schema.org/).
- Include clear descriptions and specify which fields are required.
- Add realistic default values or enum options where appropriate.

### Step 4: Craft `prompt.md`
- Start with a clear persona (e.g., "You are an expert church communications director...").
- Detail the exact formatting requirements for each section of the output.
- Enforce tone, style, and clarity.
- Embed instructions for error handling or missing variables.

### Step 5: Outline `workflow.md`
- Break down the workflow into sequential steps:
  1. Input Gathering (forms, meeting notes, etc.)
  2. Prompt Execution (LLM call or chat)
  3. **Human Review & Pastoral Verification** (crucial!)
  4. Final Publishing/Distribution

### Step 6: Define `guardrails.md`
- State explicit boundaries: What must the AI NEVER do in this skill?
- Specify privacy rules, theological considerations, and emotional safety rules.

### Step 7: Provide Realistic `examples.md`
- Include at least 2 complete examples.
- Include the JSON input payload and the resulting formatted markdown output.
- Ensure all personal names and contact information are fictional.
