# Security & Data Privacy Policy

## 🔒 Commitment to Ministry Data Privacy

The **Ministry AI Skills** project is committed to helping churches, pastors, and faith-based organizations use artificial intelligence without compromising the safety, privacy, and confidentiality of their congregations.

Because church ministry deals with deeply sensitive human concerns—including pastoral counseling notes, personal prayer requests, financial stewardship, and youth ministry records—security and ethical data handling are central to our project's mission.

---

## 🛡️ Supported Versions

As an open-source prompt and workflow library, security updates apply to the main branch of this repository.

| Version / Branch | Supported |
|---|---|
| `main` | :white_check_mark: Yes |
| Historical releases | :x: No (Please update to latest) |

---

## 🛑 Data Privacy Guardrails for Contributors & Users

1. **Zero Real Personal Data**: Never commit or submit pull requests containing real names, real email addresses, phone numbers, giving dollar amounts, private prayer requests, or personal counseling records. All examples must use fictional details.
2. **Local AI / Zero-Data-Retention (ZDR) Recommendations**: When using skills that handle semi-sensitive data (such as guest follow-up or prayer categorization), we strongly recommend using enterprise or zero-retention API endpoints, or locally hosted open models.
3. **No Secrets in Repo**: Never commit API keys, `.env` files, or webhook endpoints into the repository.

---

## 🚨 Reporting a Vulnerability or Security/Privacy Issue

If you discover a security vulnerability, an inadvertent exposure of private data, or a prompt design flaw that violates our safety guardrails:

1. **Do NOT open a public GitHub issue.**
2. Please submit a private security advisory through GitHub's [Security Advisories](https://github.com/asjames18/ministry-ai-skills/security/advisories) feature, or email the maintainers directly at `[TODO: Insert Security Contact Email, e.g., security@yourdomain.org or repository maintainer email]`.
3. Include:
   - A detailed description of the vulnerability or privacy risk.
   - The affected file(s) and skill(s).
   - Steps to reproduce the issue.
   - Proposed mitigation or fix (if available).

We will acknowledge receipt within 48 business hours and provide a timeline for remediation.

---

## 📄 License & Responsible Use

This project is licensed under the MIT License. Users and integrators are responsible for ensuring that their deployment of these skills complies with local privacy regulations (e.g., GDPR, CCPA) and pastoral care obligations.
