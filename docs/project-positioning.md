# Project Positioning: Ministry AI Skills 🕊️

## Executive Summary

**Ministry AI Skills** is an open-source, platform-agnostic library of structured AI prompts, execution workflows, JSON schemas, and safety guardrails designed specifically for Christian ministries and churches.

It provides practical, tested AI building blocks that local church teams can immediately use in everyday tools (like ChatGPT, Claude, and Copilot) or integrate into custom software, church management systems (ChMS), and automated ministry workflows.

---

## 🎯 The Core Problem

Churches today operate under substantial administrative strain:
- **Bi-vocational and solo pastors** spend 15–20+ hours a week on administration, slide preparation, bulletin writing, and email drafts rather than direct pastoral care and discipleship.
- **Volunteers and administrative assistants** face burnout attempting to produce fresh social content, organize event logistics, and follow up with first-time visitors with limited tools.
- **Commercial AI solutions for churches** are often expensive, proprietary, lock churches into closed platforms, or lack theological care and strict privacy boundaries.
- **Generic AI chatbots** often generate shallow, generic, or theologically questionable outputs when given unguided, one-line prompts.

---

## 💡 The Solution: Modular Skill Architecture

Rather than building a single monolithic chatbot that attempts to do everything, **Ministry AI Skills** organizes ministry capabilities into **discrete, modular skills**.

Each skill solves a single, well-defined ministry task (e.g., preparing weekly announcements, researching sermon context, structuring event run-of-shows, or following up with first-time guests) and provides:
1. **Clear Input Definitions** (`inputs.schema.json`)
2. **Production-Ready Prompts** (`prompt.md`)
3. **Step-by-Step Human + AI Workflows** (`workflow.md`)
4. **Strict Theological & Privacy Guardrails** (`guardrails.md`)
5. **Concrete Ministry Examples** (`examples.md`)

---

## 👥 Who This Is For

- **Solo & Bi-Vocational Pastors**: Reclaim hours spent on repetitive writing tasks without sacrificing quality.
- **Church Administrative Staff & Communicators**: Streamline bulletin blurbs, newsletters, and multi-channel stage announcements.
- **Ministry Team Leads & Volunteers**: Coordinate logistics, volunteer rosters, and event blueprints effortlessly.
- **Christian Technologists & Developers**: Build custom AI tools, n8n automations, Custom GPTs, or ChMS integrations on top of validated, open-source prompts and schemas.

---

## 🛑 What This Is Not

- **Not a replacement for pastoral care**: AI cannot visit the sick, counsel the grieving, baptize believers, pray with discernment, or replace spiritual leadership.
- **Not an authoritative biblical commentator**: AI outputs are research and drafting aids; pastoral review and biblical verification are mandatory.
- **Not a closed commercial product**: This repository is 100% open-source under the MIT License.
- **Not a data harvester**: We do not collect, store, or train on church data. All workflows emphasize anonymization and zero data retention.

---

## 🌐 Ecosystem Context: Ministry AI Skills & OpenChurch AI

- **`ministry-ai-skills`** is the standalone, platform-agnostic open-source library of prompts, workflows, and schemas. It is intentionally simple, accessible directly on GitHub, and usable with zero software installation.
- **OpenChurch AI** represents a vision for a broader future ecosystem of open tools, integrations, and community applications that may build upon or incorporate the Ministry AI Skills library over time.

By keeping the skill library independent, modular, and vendor-neutral, any church, developer, or ministry platform can adopt and contribute to these skills freely.

---

## 📜 Core Guiding Principles

1. **Jesus-Centered & Ministry-Minded**: Technology serves the mission of the church; the church does not serve the technology.
2. **Humility & Denominational Neutrality**: Designed for broad Christian ministry without imposing sectarian doctrines.
3. **Rigorous Privacy & Confidentiality**: Zero exposure of sensitive pastoral, medical, or giving details.
4. **Human-in-the-Loop Always**: AI drafts; ministry leaders review, discern, and approve.
