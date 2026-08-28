# Getting Started with Ministry AI Skills

Welcome to **Ministry AI Skills**! This guide helps pastors, church staff, volunteer teams, and software developers quickly put these skills to work.

---

## 🧭 Which Path Are You On?

- **[I am a Pastor or Church Leader](#-for-pastors--ministry-leaders)**: You want to save hours on administration, communication, and planning while keeping Jesus at the center.
- **[I am a Media or Communications Volunteer](#-for-church-media--communications-teams)**: You need quick, high-impact copy, announcements, social posts, and graphics concepts.
- **[I am a Developer or Automation Builder](#-for-developers--technical-teams)**: You want to integrate these skills into n8n, LangChain, Custom GPTs, or custom web apps.

---

## 🕊️ For Pastors & Ministry Leaders

You don't need any coding experience to use this library.

### 3-Step Quick Start:
1. **Browse the Skills**: Look in the [`skills/`](../skills/) directory and find the folder matching your need (e.g., [`sermon-prep-support`](../skills/sermon-prep-support/)).
2. **Copy the Prompt**: Open `prompt.md` inside that skill directory and copy the contents.
3. **Run in Your Favorite AI Tool**:
   - Open ChatGPT, Claude, Microsoft Copilot, or Google Gemini.
   - Paste the prompt.
   - Fill in the bracketed variables (like Scripture passage, series theme, target audience).
   - Press Enter!

### 💡 Best Practice for Leaders
Always remember the **Human-in-the-Loop** rule: Treat AI as a creative brainstorming partner, research assistant, or first-draft copywriter. Never preach or publish AI text without prayerful discernment and review.

---

## 🎨 For Church Media & Communications Teams

1. **Weekly Announcements**: Use [`weekly-announcements`](../skills/weekly-announcements/) on Monday/Tuesday to turn raw ministry bullet points into bulletin copy, stage announcement scripts, and weekly email blasts in minutes.
2. **Media Packs**: Use [`church-media-pack`](../skills/church-media-pack/) on Wednesday/Thursday to get Midjourney/DALL-E image prompts, YouTube titles, Instagram carousel outlines, and sermon slide summaries.
3. **Guest Follow-Up**: Use [`first-time-guest-follow-up`](../skills/first-time-guest-follow-up/) to prepare personalized text messages and welcome emails for Sunday visitors.

---

## 💻 For Developers & Technical Teams

Each skill includes an `inputs.schema.json` compliant with JSON Schema Draft-07. This makes programmatic execution trivial.

### Simple Python Integration Example
```python
import json
from openai import OpenAI

client = OpenAI()

# Load Prompt
with open("skills/weekly-announcements/prompt.md", "r") as f:
    system_prompt = f.read()

# Load Inputs
user_payload = {
    "church_name": "Grace Community Church",
    "announcements": [
        {
            "title": "Fall Family Picnic",
            "date_time": "Sunday, Oct 12 at 4:00 PM",
            "location": "Oak Ridge Park Pavilion",
            "description": "BBQ provided, bring a side dish or dessert to share.",
            "action_item": "RSVP on church app by Wednesday",
            "target_audience": "Families and all members"
        }
    ],
    "tone": "Warm and inviting",
    "requested_formats": ["stage_script", "bulletin_blurb", "social_post"]
}

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": json.dumps(user_payload)}
    ]
)

print(response.choices[0].message.content)
```

For more architectures (LangChain, CrewAI, n8n, OpenAI Assistants), see the [Platform Guides](platform-guides.md).
