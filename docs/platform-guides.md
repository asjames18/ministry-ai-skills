# Platform Integration Guides

Ministry AI Skills are designed to be **100% platform-agnostic**. You can use them directly in web chatbots or wire them into complex automation pipelines.

Below are practical implementation recipes for popular platforms.

---

## 1. OpenAI ChatGPT (Custom GPTs)

To create a Custom GPT for your church staff:
1. Go to [ChatGPT](https://chat.openai.com) > **Explore GPTs** > **Create a GPT**.
2. In the **Configure** tab:
   - **Name**: e.g., "Grace Church Communications Assistant"
   - **Instructions**: Copy and paste the contents of `prompt.md` from the desired skill (e.g., [`skills/weekly-announcements/prompt.md`](../skills/weekly-announcements/prompt.md)).
   - **Knowledge**: Upload your church's style guide, statement of faith, or ministry calendar.
3. Share the Custom GPT link with your ministry staff and volunteers.

---

## 2. Anthropic Claude (Projects)

To set up a Claude Project:
1. Open [Claude.ai](https://claude.ai) and click **Projects** > **New Project**.
2. Set the Project name (e.g., "Sermon Study & Research Assistant").
3. Under **Project Instructions**, paste the contents of [`skills/sermon-prep-support/prompt.md`](../skills/sermon-prep-support/prompt.md).
4. Under **Project Knowledge**, add your church's preferred commentaries, preaching calendar, or doctrinal statement.

---

## 3. Workflow Automation with n8n

You can automate weekly communications (e.g., triggering every Tuesday morning from a Google Form or Planning Center / Church Community Builder):

```text
[Webhook / Schedule Trigger]
            │
            ▼
[Extract Church Event Data]
            │
            ▼
[OpenAI / Claude Node] ──> Uses `skills/weekly-announcements/prompt.md`
            │
            ▼
[Send Draft to Staff Slack / Email for Approval]
            │
            ▼ (On Human Approval)
[Push to Mailchimp / Planning Center / Website]
```

---

## 4. LangChain (Python)

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import json

# Read system prompt template
with open("skills/church-event-planning/prompt.md", "r") as f:
    system_template = f.read()

prompt = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("human", "{event_input_json}")
])

llm = ChatOpenAI(model="gpt-4o", temperature=0.3)
chain = prompt | llm

input_data = {
    "event_name": "Community Harvest Festival",
    "target_date": "October 31, 2026",
    "goals": "Build relationship with unchurched local neighborhood families",
    "budget": "$1,500"
}

response = chain.invoke({"event_input_json": json.dumps(input_data)})
print(response.content)
```

---

## 5. CrewAI (Multi-Agent Ministry Team)

```python
from crewai import Agent, Task, Crew, Process

# Media Director Agent
media_director = Agent(
    role="Church Media Director",
    goal="Generate engaging, Christ-centered media assets and social copy for Sunday",
    backstory="You are a skilled church creative who crafts visual and written ministry assets with excellence.",
    verbose=True
)

# Load skill prompt as task description
with open("skills/church-media-pack/prompt.md", "r") as f:
    task_instructions = f.read()

media_task = Task(
    description=task_instructions,
    expected_output="Complete media pack with slide copy, image prompts, and social captions.",
    agent=media_director
)

crew = Crew(
    agents=[media_director],
    tasks=[media_task],
    process=Process.sequential
)
```
