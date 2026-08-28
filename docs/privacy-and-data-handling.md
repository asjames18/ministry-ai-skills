# Privacy & Data Handling Guidelines

Churches hold a sacred trust with their members and community. Protecting personal information, confidential prayer requests, and pastoral counseling notes is both a spiritual and legal responsibility.

---

## 🔒 The Golden Rule of Church AI Privacy

> **Never feed un-redacted personal, medical, financial, counseling, or minor information into public AI models.**

---

## 🛑 Categories of Sensitive Data

### Tier 1: Highly Confidential (DO NOT input into general cloud AI)
- **Pastoral Care & Counseling Records**: Session notes, marital conflict, addictions, spiritual struggles.
- **Mental Health & Crisis Situations**: Grief, suicidal ideation, abuse disclosures.
- **Financial Giving Records**: Specific donor dollar amounts, pledging history, tithing records.
- **Minors / Children & Youth Details**: Full names, birthdates, allergy records, school names, photos connected to names.
- **Church Discipline & Staff HR**: Personnel evaluations, conflict resolution, termination discussions.

### Tier 2: Semi-Confidential (Must be Anonymized / Redacted)
- **Prayer Requests**: Many prayer requests contain personal medical diagnoses ("Mary has stage 3 cancer"), family troubles, or legal battles.
  - *Correct Approach*: Anonymize before processing. (e.g., "Pray for a member recovering from surgery" instead of full name and private medical history).
- **Guest Follow-Up Data**: Only use first names or placeholder variables when generating template drafts.

### Tier 3: Public / Low Risk (Safe for AI processing)
- Public sermon transcripts.
- Approved event details, dates, times, locations.
- Ministry descriptions and general church website copy.
- Approved public prayer list items that have already been cleared for the weekly bulletin.

---

## 🛡️ Best Practices for Churches Using AI

1. **Use Enterprise / Zero-Data-Retention (ZDR) APIs where possible**: If integrating AI into your church management system (ChMS), use commercial API tiers that contractually guarantee user data is not used for model training.
2. **Train Volunteers**: Ensure media and admin volunteers know not to copy-paste private member emails or sensitive messages into consumer AI chat windows.
3. **Anonymization Checklist**:
   - Replace member names with `[Member A]` or `[First Name]`.
   - Remove phone numbers, addresses, and email addresses.
   - Remove specific medical facility names or legal identifiers.
