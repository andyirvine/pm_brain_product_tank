# Product Brain Prototype: Ledger

## What is this?

This is a working prototype of **Product Brain**—a persistent, queryable intelligence layer that connects customer signals, research, strategic intent (OKRs), and hypothesis-evidence pairings in a structured git repository.

For a 3-person seed-stage fintech startup called **Ledger**, this brain organizes:
- **20 customer interviews** across 2 product areas
- **Secondary research** on small business finance pain points
- **3 Jobs to Be Done** (JTBDs) that thread through the product strategy
- **Company OKRs** (leadership brain)
- **Team OKRs** (PM brains) that align to company goals
- **Hypothesis-evidence pairings** showing what we know, what we're testing, and what's on the backlog

---

## The Fractal Structure

This brain has two layers:

### **Leadership Brain** (`/leadership-brain`)
Synthesizes across product areas. Answers: "What are our key strategic bets this year, and what customer evidence supports them?"

- Company-level OKRs
- Cross-team hypothesis-evidence
- How PM signals roll up

### **PM Brain** (`/pm-brain`)
Individual product areas (Invoicing & Collections, Tax & Compliance). Answers: "What do our customers need, what are we building, and how will we know it works?"

- Team OKRs
- Customer signals synthesis
- Team-specific hypothesis-evidence

---

## How to Navigate This

**Start here if you want to understand:**

1. **The overall strategy** → `/leadership-brain/company-okrs.md`
2. **What we're solving for** → `/jtbd/` (3 Jobs to Be Done)
3. **What customers actually told us** → `/research/primary-research/customer-interviews/interview-log.md`
4. **How a PM uses this brain** → `/pm-brain/invoicing-collections/signals-synthesis.md`
5. **What we're betting on (and testing)** → `/leadership-brain/hypothesis-evidence.md`

---

## The Customer Research

- **20 semi-structured interviews** across 2 product areas (10 per area)
- Mix of **current Ledger users** and **non-users** (competitors or manual processes)
- Different customer segments (solopreneurs, agencies, service businesses)
- Interviews organized by area with thematic synthesis
- Secondary research on the small business finance landscape

---

## The Jobs to Be Done

Three core jobs thread through this brain:

1. **"Get paid by my clients"** — The practical & emotional challenge of invoicing, chasing payments, and managing cash flow uncertainty
2. **"File my taxes without stress"** — Compliance, preparation, and the anxiety of missing deadlines or owing unexpected amounts
3. **"Make confident cashflow decisions"** — Understanding where money is, where it's going, and whether the business is sustainable

Each job has:
- **Functional needs** (what success looks like)
- **Emotional & social needs** (how it feels to have the job done well)
- **Circumstances** (when the job emerges, what constraints exist)
- **Steps** (how people currently solve it, solution-independent)

---

## Hypothesis-Evidence Pairing

This brain doesn't claim certainty. Instead, it tracks:

- **Validated hypotheses** — Customer evidence confirms our assumption
- **Backlog hypotheses** — Assumptions we haven't tested yet, or evidence contradicts them

Examples:
- ✅ **Validated**: "Small business owners dread invoicing because chasing payments feels uncomfortable" (evidenced in 8 interviews)
- 🔄 **Backlog**: "Automated payment reminders reduce Days Sales Outstanding by 20%" (hypothesis, not yet tested)
- ⚠️ **Challenged**: "All small businesses want automated tax prep" (evidence shows solopreneurs prefer DIY, while agencies want done-for-you)

---

## How to Use This in a Client Conversation

This prototype is designed to show:

1. **We listen systematically** — 20 interviews aren't anecdotes; they're the foundation of strategy
2. **We connect evidence to decisions** — Every OKR traces back to customer needs
3. **We're disciplined about what we don't know** — Hypothesis-evidence pairings show intellectual honesty
4. **We scale insight across the organization** — Both PMs see the same research, aligned to the same jobs
5. **It's persistent and queryable** — "Which customers told us X?" "Which OKRs serve Job #2?" "What contradicts our assumption about Y?"

---

## File Structure at a Glance

```
product-brain-prototype/
├── README.md (you are here)
├── research/
│   ├── secondary-research/
│   │   └── market-analysis-2024.md
│   └── primary-research/
│       └── customer-interviews/
│           ├── interview-log.md
│           └── interview-001.md through interview-020.md
├── jtbd/
│   ├── job-1-get-paid.md
│   ├── job-2-file-taxes.md
│   └── job-3-cashflow-decisions.md
├── leadership-brain/
│   ├── company-okrs.md
│   ├── hypothesis-evidence.md
│   └── synthesis.md
└── pm-brain/
    ├── invoicing-collections/
    │   ├── signals-synthesis.md
    │   ├── hypothesis-evidence.md
    │   ├── team-okrs.md
    │   └── customer-segments.md
    └── tax-compliance/
        ├── signals-synthesis.md
        ├── hypothesis-evidence.md
        ├── team-okrs.md
        └── customer-segments.md
```

---

## The Company: Ledger

**Stage**: Seed-funded, 3 founders  
**Problem**: Small businesses suffer through fragmented finance—invoicing scattered across email, tax prep is chaotic, and they have zero confidence in their cashflow  
**Vision**: A single source of truth where small business owners feel *in control* of their money  

**Founding insight**: The problem isn't software. It's that small business owners are drowning in *anxiety* because they don't have a clear picture. Ledger removes the stress, not just the admin.

---

## Notes for Using This Prototype

- This is a **working example**, not a template. Adapt the structure to your company's shape.
- The interviews are **realistic but fictional** — based on common patterns in small business finance, but names and details are synthesized.
- The OKRs, hypotheses, and evidence are **interconnected**. Follow the links to see how a customer insight becomes a strategic bet.
- This brain lives in **git**, so it's version-controlled, collaborative, and auditable. "Who said this, when, and what evidence backs it up?" is always answerable.

---

**Ready to explore?** Start with the JTBD section, then jump to the research to see how customer voices inform strategy.
