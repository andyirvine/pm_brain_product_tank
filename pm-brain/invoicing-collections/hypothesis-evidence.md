# Invoicing & Collections: Hypothesis-Evidence Tracking

**PM Owner**: Claire | **Area**: Invoicing & Collections
**Updated**: Apr 2024
**Purpose**: Track what we believe, what we've tested, and what the evidence says — specifically for the IC product area

---

## H1: Automated Reminders Reduce DSO by 20–30%

**Hypothesis**: Owners who enable automated payment reminders will see Days Sales Outstanding drop from ~45 days to ~30 days, because reminders surface the invoice at the right moment without requiring owner action.

### Status: ✅ VALIDATED (Concept) | 🔄 PENDING (Quantified post-launch)

### Evidence Supporting
- **Interview 002 (Raj)**: "DSO dropped from 65 to 35 days when I had visibility and started following up systematically"
- **Interview 007 (Amara)**: "I send reminders manually but always feel bad — if it was automatic, I'd do it every time"
- **Interview 001 (Maya)**: "I don't send reminders because I don't want to seem pushy; if it was automatic, it's not me asking"
- **Industry data**: Atradius reports automated reminder users average 8–12 days faster collection vs. manual

### Evidence Against / Caveats
- **Interview 005 (Lisa)**: Worried automated reminders might feel "spammy" to long-term clients
- Raj's improvement was driven by visibility + manual follow-up, not automation specifically

### Confidence Level: **MEDIUM-HIGH**

### What We're Testing
- Does opt-in rate differ between solopreneurs and agencies?
- Does tone of reminder (formal vs. friendly) affect payment speed?
- A/B test: "Just a reminder" vs. "Your invoice is due" vs. no-message reminder

### Open Questions
- What reminder cadence is optimal? (Day 0, Day 7, Day 14, Day 30?)
- Should reminders be off by default, or opt-out?

### Action Items
- Q2: Launch automated reminders with 3 tone options
- Q2: Measure DSO before/after for users who enable reminders
- Q3: Report actual DSO improvement vs. 20–30% target

---

## H2: Invoice Creation Time < 2 Minutes Increases Invoicing Frequency

**Hypothesis**: Owners who can create and send an invoice in under 2 minutes (using saved templates) will invoice more frequently — reducing the backlog of uninvoiced work.

### Status: ✅ VALIDATED (Concept) | 🔄 PENDING (Product evidence)

### Evidence Supporting
- **Interview 003 (Sarah)**: "I invoice quarterly because it takes too long. If it was quick, I'd invoice weekly."
- **Interview 007 (Amara)**: "Invoice setup takes 15–20 minutes. I batch them once a month because it's a chore."
- **Interview 001 (Maya)**: "I have 3 invoices sitting in my drafts folder right now. Haven't sent them."

### Evidence Against / Caveats
- Delay may also be psychological (fear of asking), not just speed — faster tools alone may not solve this
- Interview 009 (Priya) delayed invoicing due to shame, not time — speed won't help her segment

### Confidence Level: **MEDIUM**

### What We're Testing
- Do users with templates invoice faster? (Track template creation → invoice send time)
- Does invoicing frequency increase after templates are created?
- Is the bottleneck speed, psychology, or both?

### Open Questions
- Should we prompt template creation at onboarding, or let users discover it?
- Is there a "zero-effort invoicing" pattern for recurring clients that removes even the 2-minute step?

### Action Items
- Q1: Ship invoice templates; track creation time
- Q1–Q2: Compare invoicing frequency for template users vs. non-template users
- Q2: If frequency doesn't increase, investigate psychological blockers

---

## H3: Recurring Invoicing Saves Solopreneurs 2–3 Hours/Month

**Hypothesis**: Solopreneurs with ≥ 2 recurring clients will save 2–3 hours/month by automating invoice scheduling, freeing time for billable work.

### Status: ✅ VALIDATED (Concept) | 🔄 PENDING (Quantified post-launch)

### Evidence Supporting
- **Interview 007 (Amara)**: "3–4 recurring clients on different dates; manual invoicing takes 2–3 hours/month"
- **Interview 003 (Sarah)**: "I have 4 recurring VA clients; I send invoices manually every month even though amounts never change"
- **Secondary**: Time-saving estimates assume 15–20 min per invoice × 4–6 recurring clients = 1–2 hours/month

### Evidence Against / Caveats
- Small sample (2 direct mentions); need broader validation
- Time savings assume owners don't re-check or customize recurring invoices — some will

### Confidence Level: **MEDIUM-HIGH**

### What We're Testing
- Post-launch: Survey Amara + similar segment on time saved with recurring invoicing
- Track invoice frequency before and after recurring setup

### Action Items
- Q2: Launch recurring invoicing
- Q2: Survey 20 solopreneurs with recurring clients at 30-day post-launch mark
- Q3: Publish internal case study: "How much time does Ledger save?"

---

## H4: Visibility Into Unpaid Invoices Drives Systematic Follow-Up

**Hypothesis**: When owners can see all outstanding invoices in one dashboard, they follow up proactively — replacing avoidance with action.

### Status: ✅ VALIDATED

### Evidence Supporting
- **Interview 002 (Raj)**: "When I see 5 invoices in 'overdue', I follow up. When it's scattered, I don't."
- **Interview 006 (James)**: "Dashboard tells me which phase we're in and whether payment came in; I use it before every project kickoff"
- **Interview 010 (David)**: "Accountants recommend Ledger because clients finally know what's outstanding — changes behavior"
- **General pattern**: 4/10 IC interviews cite visibility as the core mechanism for behavioral change

### Confidence Level: **HIGH**

### What We're Testing
- Does weekly active dashboard use correlate with lower DSO? (Cohort analysis)
- Does adding a "follow-up due" indicator further improve action rates?

### Action Items
- Q1: Launch dashboard with "overdue" / "due soon" / "paid" segmentation
- Q2: Analyze cohort: dashboard users vs. non-users → DSO difference

---

## H5: Professional Invoice Tone Increases Client Payment Speed

**Hypothesis**: Professional, well-designed invoices (clear branding, specific due date, one-click payment) are paid faster than informal payment requests (PayPal links, Venmo requests, emailed PDF).

### Status: 🔄 BACKLOG (Plausible; not directly tested)

### Evidence Supporting
- **Interview 005 (Lisa)**: Uses Stripe links, not invoices; clients pay late because "there's no urgency"
- **Interview 009 (Priya)**: "If my invoice looks polished, clients take it more seriously"
- **Secondary**: Studies show invoices with embedded payment links paid 7–14 days faster (FreshBooks Industry Report 2023)

### Confidence Level: **MEDIUM**

### What We're Testing
- Compare DSO for users who use professional templates vs. basic invoices
- A/B test: Invoice with payment button embedded vs. invoice with bank transfer instructions

### Action Items
- Q1–Q2: Track DSO by invoice type (branded template vs. plain)
- Q3: Report results internally

---

## H6: Accountants Are a Distribution Channel (IC-Specific)

**Hypothesis**: Accountants who use Ledger with their own clients will recommend it to new clients, acting as a low-cost, high-trust referral channel for Ledger.

### Status: 🟡 PARTIALLY VALIDATED | Needs scale testing

### Evidence Supporting
- **Interview 010 (David)**: "I recommend Ledger to every client who asks how to manage invoicing; I use it too"
- **Interview 001 (Maya)**: "My accountant suggested I get more organized; I'd try whatever they recommended"

### Evidence Against / Caveats
- Only 1 direct accountant interview; can't extrapolate distribution model from 1 person
- Accountant recommendation behavior varies widely by firm type

### Confidence Level: **LOW-MEDIUM**

### What We're Testing
- Q3: Build accountant read-only view; offer to David and 5 other accountants
- Measure: Do they actively recommend Ledger? Track referral codes by accountant

### Action Items
- Q3: Reach out to David (Interview 010) for accountant view beta
- Q4: Launch accountant partner program; track referral conversion

---

## H7 (Challenged): One-Click Invoicing Is Enough for Agencies

**Hypothesis (original)**: Agency users want invoicing to be as simple and fast as solopreneurs.

### Status: ⚠️ CHALLENGED / REJECTED

### Evidence Contradicting
- **Interview 002 (Raj)**: Needs PO numbers, payment terms by client, multi-user approval
- **Interview 006 (James)**: Uses milestone invoicing; needs project-phase tracking
- **Interview 008 (Michael)**: "I need to invoice across 4 systems; speed isn't the problem — sync is"
- **Interview 004 (Tom)**: Needs approval workflow before invoices go out

### What We Learned
- Agencies need **visibility + coordination**, not just speed
- Milestone billing, team permissions, and integration are table stakes for 5+ person teams
- Simple invoicing is a solopreneur solution; agencies need a different product surface

### Implication
- Segment the product more aggressively; don't ship a "one size fits all" invoice UI
- Agency onboarding should default to dashboard + integration setup, not quick-invoice

---

## Summary Table

| Hypothesis | Status | Confidence | Next Action |
|---|---|---|---|
| H1: Reminders reduce DSO 20–30% | ✅ Concept / 🔄 Pending | Medium-High | Launch Q2; measure post-launch |
| H2: < 2 min creation → more frequent invoicing | ✅ Concept / 🔄 Pending | Medium | Ship templates Q1; track frequency |
| H3: Recurring saves 2–3 hrs/month | ✅ Concept / 🔄 Pending | Medium-High | Launch Q2; survey at 30 days |
| H4: Dashboard visibility → systematic follow-up | ✅ Validated | High | Ship dashboard Q1; cohort analysis |
| H5: Professional invoices paid faster | 🔄 Backlog | Medium | A/B test Q1–Q2 |
| H6: Accountants as distribution | 🟡 Partial | Low-Medium | Accountant beta Q3 |
| H7: One-click invoicing suits agencies | ⚠️ Rejected | Medium-High | Segment-specific UX |

---

**Related Documents**:
- `/pm-brain/invoicing-collections/signals-synthesis.md` — Full customer signal analysis
- `/pm-brain/invoicing-collections/team-okrs.md` — Team KRs these hypotheses inform
- `/leadership-brain/hypothesis-evidence.md` — Cross-team strategic bets
