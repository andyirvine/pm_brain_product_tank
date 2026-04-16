# Tax & Compliance: Customer Segments

**PM Owner**: Marcus | **Area**: Tax & Compliance
**Updated**: Apr 2024
**Based on**: Interviews 011–020

---

## Segmentation Framework

TC customers vary along two primary dimensions:

**Dimension 1 — Income Predictability**: Stable/predictable vs. Variable/seasonal
**Dimension 2 — Tax Complexity**: Single stream vs. Multiple streams / entity transitions

These produce four segments with meaningfully different pain profiles, activation paths, and WTP.

---

## Segment A — The Variable-Income Solo

**"My income changes every month. I can never figure out what I'm supposed to pay each quarter."**

### Profile
- **Archetype**: Carlos (Interview 014) — seasonal contractor; Emma (Interview 011) — freelance consultant
- **Business size**: 1 person
- **Revenue model**: Project-based; highly variable by month, quarter, or season
- **Annual revenue**: $40K–$120K; wide variance within year
- **Income pattern**: 50–70% of income may arrive in 1–2 quarters; off-season quarters are near-zero
- **Current approach**: Divides last year's total tax by 4; consistently under- or over-pays

### Top Pain Points
1. Static quarterly estimates are almost always wrong — too high in slow quarters, too low in good ones
2. IRS underpayment penalties in high-earning quarters; large refunds (wasted float) in slow ones
3. No intuitive way to know "how much should I save from this project?"

### Jobs Hired For
- Pay correct quarterly estimates without manual calculation
- Know how much to set aside from each payment received
- Avoid IRS penalties while not overpaying unnecessarily

### Needs
- Dynamic quarterly estimate that recalculates as income arrives
- Per-project or per-payment "set aside X%" suggestion
- Clear indication of whether current payments are on track for the year

### Willingness to Pay
- **$25–$40/month** — WTP driven by penalty avoidance; one avoided penalty ($200–$2,000+) easily justifies annual cost
- Annual plan preferred — tax planning is year-round

### Activation Pattern
- "Tell us about your income pattern — we'll calculate exactly what to pay each quarter"
- First value moment: first dynamically adjusted quarterly estimate that accounts for current-year income

### Retention Risk
- Low if estimates are accurate — users see immediate, concrete value
- High churn if estimates are wrong — trust collapses quickly for this segment

### Interview Evidence
- 014 (Carlos): Primary archetype — seasonal contractor; explicit underpayment + penalty history
- 011 (Emma): Variation — freelance consultant; income varies by project pipeline; wants guidance not outsourcing

---

## Segment B — The High-Earner Who Got Surprised

**"I had a great year. I just didn't realize how great until I got my tax bill."**

### Profile
- **Archetype**: Vikram (Interview 012); Rachel (Interview 013)
- **Business size**: 1–5 people
- **Revenue model**: Consulting, agency, or service business; income growing or recently spiked
- **Annual revenue**: $150K–$500K+
- **Income pattern**: Generally more consistent than Segment A, but growing YoY — prior year estimates significantly understate current liability

### Top Pain Points
1. Relied on prior year return as estimate; income grew significantly; discovered the gap in April
2. Large, unexpected tax bills ($20K–$50K range) created financial hardship or forced emergency borrowing
3. No ongoing visibility into cumulative tax liability throughout the year

### Jobs Hired For
- Never be surprised by the tax bill again
- Know current tax position at any point in the year ("how much do I owe right now, if I filed today?")
- Build savings habits based on real-time liability visibility

### Needs
- Year-round tax liability dashboard: "Based on your YTD income, your estimated annual tax is $X"
- Monthly income reconciliation to keep estimate current
- "Set aside" suggestion that accounts for growth ("you earned 40% more than last year — here's the adjusted estimate")

### Willingness to Pay
- **$35–$60/month** — highest WTP in TC segments; acutely aware of the cost of NOT having this
- Motivated by the memory of the surprise; strongest emotional hook in the product

### Activation Pattern
- "What did you owe last April? Let's make sure that never happens again."
- First value moment: first time they see their current estimated liability and recognize it's higher than they expected — but now they know in advance

### Retention Risk
- Very low — once the habit of checking the dashboard is formed, switching cost is high
- Churn trigger: if Ledger's estimate is significantly wrong, trust evaporates (high stakes segment)

### Interview Evidence
- 012 (Vikram): Primary archetype — $40K surprise; now sets aside 30% per month proactively
- 013 (Rachel): Variation — $35K surprise; "my accountant should have warned me, but they didn't"

---

## Segment C — The Multi-Stream Juggler

**"I have freelance income, a W-2 job, and I sold an online course this year. I have no idea how to think about taxes."**

### Profile
- **Archetype**: Nathan (Interview 016); Leo (Interview 020)
- **Business size**: 1 person
- **Revenue model**: 2–4 income streams; mix of W-2, 1099 consulting, digital products, investments
- **Annual revenue**: $80K–$300K combined across streams; self-employment income typically 40–70% of total
- **Tax complexity**: Different tax treatment per stream; SE tax applies to some but not others; multiple estimated payment calculations needed

### Top Pain Points
1. Can't easily understand which income stream is driving tax liability
2. Self-employment tax on 1099 income is a recurring shock — often not accounted for in mental models
3. Deduction allocation across income streams is a recurring source of uncertainty

### Jobs Hired For
- Understand how each income stream affects total tax liability
- Know how much SE tax to expect from consulting vs. W-2 vs. product income
- Optimize deductions across streams without fear of claiming the wrong thing

### Needs
- Income stream breakdown: "Here's your tax liability by source"
- Clear SE tax visibility: "Your consulting income incurs an additional 15.3% in SE tax — here's what that looks like"
- Deduction suggestions by income type

### Willingness to Pay
- **$30–$50/month** — WTP driven by complexity; this segment has more to gain from clarity
- Most likely to upgrade if decision-making features are bundled (income by stream → pricing and project selection decisions)

### Activation Pattern
- "How many income sources do you have? Let's separate them so you can see the real picture."
- First value moment: first income stream breakdown that shows which source is driving the bulk of tax liability

### Retention Risk
- Medium — if the product doesn't handle multi-stream income well, they'll return to a spreadsheet or accountant
- High upgrade potential — this segment naturally overlaps with Job 3 (cashflow decisions)

### Interview Evidence
- 016 (Nathan): Primary archetype — consulting + W-2 + course sales; explicit confusion about deduction allocation
- 020 (Leo): Variation — project-based consulting; uses profit-by-project to price and set aside taxes per engagement

---

## Segment D — The Delegation Seeker

**"My accountant handles my taxes. I just want to hand them something organized and not embarrass myself."**

### Profile
- **Archetype**: Fiona (Interview 019); partial overlap with Rachel (013) pre-Ledger
- **Business size**: 1–3 people
- **Revenue model**: Service business; relatively stable income; existing CPA relationship
- **Annual revenue**: $80K–$250K
- **Current approach**: Accountant handles everything; owner's job is to gather receipts and records

### Top Pain Points
1. Tax season scramble to gather documents — receipts, bank statements, categorized expenses — all at once
2. Showing up to accountant unprepared wastes time and costs money in CPA hours
3. No real-time visibility; entirely dependent on accountant for any tax question during the year

### Jobs Hired For
- Have organized, accountant-ready records throughout the year (not just in March)
- Get through April without embarrassment or extra accountant hours
- Have a basic sense of tax position without becoming a finance expert

### Needs
- Continuous expense categorization and receipt logging throughout the year
- Year-end tax summary export formatted for CPA handoff
- Basic tax position summary ("here's roughly what you owe") without requiring deep engagement

### Willingness to Pay
- **$20–$35/month** — WTP framed against accountant hourly rate ("one hour of CPA time costs $150–$400; Ledger costs less per month")
- Price-sensitive if they don't perceive Ledger as reducing accountant fees or surprises

### Activation Pattern
- "Be ready for your accountant — year-round. Not just in March."
- First value moment: first time they export a clean, organized expense summary instead of sending a shoebox

### Retention Risk
- Medium — habit formation around expense logging is the retention mechanism; if they don't log regularly, value drops
- Lower WTP limits tolerance for friction — onboarding must be extremely simple for this segment

### Interview Evidence
- 019 (Fiona): Primary archetype — accountant handles everything; wants organized records, not DIY filing
- 013 (Rachel): Partial overlap pre-surprise — she deferred to her accountant until the $35K bill changed her behavior

---

## Segment Comparison Summary

| Dimension | Seg A: Variable-Income Solo | Seg B: High-Earner Surprised | Seg C: Multi-Stream Juggler | Seg D: Delegation Seeker |
|---|---|---|---|---|
| Primary job | Pay the right amount each quarter | Never get surprised again | Understand income by source | Show up organized to my CPA |
| Top pain | Wrong quarterly estimates | April surprise / underpayment | Multi-stream confusion | Disorganized records |
| Key feature | Dynamic quarterly estimator | Year-round liability dashboard | Income stream breakdown | Expense categorization + export |
| WTP | $25–40/mo | $35–60/mo | $30–50/mo | $20–35/mo |
| Activation hook | "Pay the right amount every quarter" | "Never be surprised in April again" | "See your taxes by income source" | "Be ready for your accountant year-round" |
| Churn risk | Low (if estimates accurate) | Very low | Medium | Medium |
| LTV potential | Medium | High | Medium-High | Medium |
| Acquisition channel | SEO ("freelancer quarterly taxes") | Paid / Referral post-April | Community / word of mouth | Accountant referral |

---

## Segment Prioritization for 2024

**Q1–Q2 focus**: Segments A and B — largest pain, clearest value prop, fastest path to NPS signal
**Q3 focus**: Segment C (Multi-Stream Juggler) — highest complexity; requires income stream breakdown feature
**Q4**: Segment D (Delegation Seeker) — accountant integration enables this segment; deferred until Q4 partner program

---

**Related Documents**:
- `/pm-brain/tax-compliance/signals-synthesis.md` — Thematic analysis from TC interviews
- `/pm-brain/tax-compliance/team-okrs.md` — OKRs by segment
- `/jtbd/job-2-file-taxes.md` — Job to Be Done served by all TC segments
