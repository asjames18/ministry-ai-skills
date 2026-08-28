# Weekly Announcements Workflow

This document details the production workflow for church communications teams using this skill.

---

## 📅 Recommended Weekly Timeline

```text
[Monday - Tuesday]  ──> Collect raw submissions from ministry leads
[Wednesday Morning] ──> Run the Weekly Announcements Skill Prompt
[Wednesday Afternoon]─> Communications Review & Edits
[Thursday Morning]  ──> Pastoral Sign-off & Graphic Creation
[Thursday Afternoon]──> Schedule Email Newsletter (Mailchimp/Substack)
[Friday]            ──> Print Bulletins & Build Slide Deck (ProPresenter)
[Sunday Morning]    ──> Stage Host Rehearsal & Live Delivery
```

---

## 📋 Step-by-Step Procedure

### 1. Collect Raw Submissions
- Gather announcement requests from department heads (Youth, Kids, Women, Men, Missions).
- Identify the single **Priority Focus Item** for the week to keep the stage announcement concise.

### 2. Format & Execute the Prompt
- Enter the collected event data into `prompt.md` or invoke the API with the payload conforming to `inputs.schema.json`.

### 3. Review & Edit
- Check that all dates, times, rooms, and web URLs are 100% accurate.
- Practice reading the Stage Host Script aloud to ensure natural cadence and under-90-second duration.

### 4. Deploy Across Channels
- **Print**: Paste into bulletin layout.
- **Email**: Paste into weekly newsletter software and schedule for Friday/Saturday.
- **Slides**: Import slide text into ProPresenter/Proclaim.
- **Social**: Schedule post and graphic for Friday/Saturday promotion.
