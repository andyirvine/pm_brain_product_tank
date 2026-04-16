# Tax & Compliance: Hypothesis-Evidence Tracking

**PM Owner**: Marcus | **Area**: Tax & Compliance
**Updated**: Apr 2024
**Purpose**: Track what we believe, what we've tested, and what the evidence says — specifically for the TC product area

---

## H1: Dynamic Quarterly Estimates Reduce Underpayment Anxiety

**Hypothesis**: When quarterly estimates are recalculated each month based on actual YTD income (instead of divided from last year's return), owners will feel significantly more confident about their tax position and stop worrying about underpaying.

### Status: ✅ VALIDATED (Concept) | 🔄 PENDING (Product validation)

### Evidence Supporting
- **Interview 014 (Carlos)**: "My income is seasonal — Q1 is huge, Q4 is slow. Paying the same amount every quarter makes no sense."
- **Interview 012 (Vikram)**: "My income grew 60% last year. My estimates were based on the prior year. I underpaid by $28K."
- **Interview 016 (Nathan)**: "I have three income streams. My accountant gives me one number and I don't know how to adjust it when one stream has a good month."
- **Interview 011 (Emma)**: "If I knew my estimate was based on what I'd actually earned, I'd feel a lot more confident paying it."
- **General pattern**: 8/10 TC users use a static method; all who describe it acknowledge it's imprecise for their income profile

### Evidence Against / Caveats
- **Interview 019 (Fiona)**: "I just pay what my accountant tells me. I don't want to think about it." — not all users want dynamic; some prefer delegation
- Dynamic estimates require accurate income data input — if users don't categorize income promptly, accuracy suffers

### Confidence Level: **HIGH**

### What We're Testing
- Post-Q2 launch: compare confidence ratings for users who use dynamic estimator vs. those who don't
- Post-2024 filing: compare Ledger estimate accuracy to ±15% target
- A/B test: monthly recalculation prompt vs. passive recalculation

### Open Questions
- Should estimates be shown as a range (±10%) or a single number?
- How do we handle users who ignore the estimate and underpay — do we send warnings?
- What's the right algorithm: YTD profit × effective rate vs. annualized income model?

### Action Items
- Q1: Finalize estimate algorithm with CPA input
- Q2: Launch dynamic estimator; send quarterly prompts before each IRS due date
- Q4: Report estimate accuracy for 2024 Q1–Q3 vs. final tax bill

---

## H2: Year-Round Tax Visibility Changes Saving Behavior

**Hypothesis**: Owners who see their estimated tax liability updated monthly will proactively set aside money — rather than scrambling in April — because the obligation is visible rather than abstract.

### Status: ✅ VALIDATED

### Evidence Supporting
- **Interview 012 (Vikram)**: "Now that I see profit monthly, I automatically put 30% in a savings account. Before Ledger, I never did this."
- **Interview 020 (Leo)**: "Seeing tax impact by project tells me how to price. I factor tax into every quote now."
- **Interview 015 (Sophie)**: "Understanding my projected liability helped me decide to go S-Corp. Saved me $14K in SE tax."
- **Interview 011 (Emma)**: "With a rough quarterly estimate, I could decide whether to buy equipment this quarter or next."

### Confidence Level: **HIGH**

### What We're Testing
- Post-launch: survey users on saving behavior change (are they setting money aside more consistently?)
- Track: do TC users have higher average bank balances near Q tax due dates? (possible Plaid integration signal)

### Action Items
- Q2: Launch year-round dashboard; include a "set aside this amount" suggestion based on current liability
- Q3: Re-interview Vikram (012) and Rachel (013) — did Ledger change their behavior?
- Q4: Publish behavioral change case study if evidence is strong

---

## H3: April Surprise is the Acute Pain Event That Drives Acquisition

**Hypothesis**: The primary acquisition trigger for TC users is having been burned by an unexpected tax bill. Ledger should speak directly to this trauma in messaging and onboarding.

### Status: ✅ VALIDATED (Pain) | 🔄 PENDING (Acquisition test)

### Evidence Supporting
- **Interview 012 (Vikram)**: $40K surprise — "That will never happen again." Actively looking for tools.
- **Interview 013 (Rachel)**: $35K surprise — "I called my accountant furious. Then I started looking for a better system."
- **Interview 014 (Carlos)**: Penalty notice from IRS was the trigger for seeking help
- **General pattern**: 5/10 TC users had an acute financial event that made them actively look for a solution

### Confidence Level: **HIGH** (pain validated); **MEDIUM** (acquisition channel pending)

### What We're Testing
- Marketing test: does "Never get surprised by your tax bill again" messaging outperform generic "manage your taxes" messaging?
- SEO: targeting "freelancer underpayment penalty" and "why do I owe so much in April" search queries

### Action Items
- Q2: A/B test landing page messaging (April Surprise framing vs. generic)
- Q3: Create content targeting post-April search behavior ("just got a big tax bill, what now?")

---

## H4: Deduction Tracking Has a Clear Dollar-Value ROI

**Hypothesis**: Small business owners miss 15–25% of eligible deductions on average. A deduction tracker in Ledger can surface and capture these, delivering a clear, quantifiable ROI ("Ledger found you $3,400 in deductions you hadn't logged").

### Status: 🔄 BACKLOG | Plausible; not product-tested

### Evidence Supporting
- **Interview 016 (Nathan)**: "I've never claimed home office deductions because I don't know how to calculate them correctly"
- **Interview 019 (Fiona)**: "My CPA says I'm conservative on deductions. I don't know what I'm missing."
- **Interview 014 (Carlos)**: Misses vehicle mileage regularly; logs it "sometimes"
- **Secondary research**: IRS data suggests self-employed owners underclaim by $4K–$8K annually on average

### Evidence Against / Caveats
- Deduction suggestion accuracy requires industry-specific categorization — engineering complexity is high
- **Interview 017 (Carla)**: "I'd trust Ledger's suggestions more if a CPA reviewed them." — trust bar is higher for tax recommendations than invoicing
- Over-claiming deductions creates audit risk — Ledger must be conservative

### Confidence Level: **MEDIUM** (pain validated; product solution not tested)

### What We're Testing
- Q3: Prototype deduction tracker; interview 5 TC users before building
- Test: Does surfacing "you may be eligible to deduct X" change user logging behavior?

### Open Questions
- How do we handle deduction accuracy — can we build confidently without CPA review?
- Should we show "potential deduction value" before user confirms, or only after they log?
- What's the right deduction list for each business type (service vs. product vs. creator)?

### Action Items
- Q2: Research deduction patterns by business type with external CPA input
- Q3: Build deduction category tracker + suggestions MVP
- Q4: Measure deduction capture before and after (self-reported comparison to prior year)

---

## H5: Multiple Income Streams Require Income-Level Tax Visibility

**Hypothesis**: Users with 2+ income sources (freelance + W-2, consulting + products, etc.) need to see tax liability broken down by stream — because blended views create confusion about which income is driving their tax bill.

### Status: 🔄 BACKLOG | Validated pain; product not built

### Evidence Supporting
- **Interview 016 (Nathan)**: "I can't tell if my tax bill is from consulting or the course I sold. They're taxed differently."
- **Interview 020 (Leo)**: "Profit by project helps me see which clients are actually worth it after taxes."
- **Interview 015 (Sophie)**: S-Corp transition created confusion about W-2 income vs. distributions vs. pass-through

### Confidence Level: **MEDIUM-HIGH** (pain clear; small sample)

### Action Items
- Q3: Design income stream breakdown feature; validate with Nathan (016) and Leo (020) before building
- Q4: Ship if validation is strong; defer to 2025 if not

---

## H6 (Challenged): Users Want Done-For-You Tax Prep

**Hypothesis (original)**: Small business owners prefer to outsource their taxes to a professional rather than manage them with a tool.

### Status: ⚠️ CHALLENGED / REJECTED

### Evidence Contradicting
- **Interview 011 (Emma)**: "I want to file myself, but I need guidance on what things mean"
- **Interview 016 (Nathan)**: "I want to understand my deductions, not just guess what someone else puts down"
- **Interview 020 (Leo)**: "Transparency about profit helps me make decisions. I don't want to outsource that visibility."
- **Interview 015 (Sophie)**: "I want to understand the S-Corp decision myself, not just trust an accountant blindly"
- **General pattern**: 5 of 10 TC interviews explicitly want transparency + understanding, not outsourcing

### What We Learned
- Users want **guided self-service** — they want to understand and own their tax position, with a trusted tool helping them
- Done-for-you appeals to one segment (Fiona, 019) — but it's a minority
- This explains why TaxWise Pro (DIY) has 8K users and Bench (done-for-you bookkeeping) has struggled with retention among solo users

### Implication
- Build transparent, explainable tax features — show the math, not just the number
- Accountant integration should position as "bring your Ledger data to your CPA" not "replace your CPA"
- Feature language should feel empowering ("Here's what you owe and why") not delegating ("We'll handle it")

---

## H7: Estimate Accuracy Is a Trust Prerequisite, Not a Nice-to-Have

**Hypothesis**: If Ledger's quarterly estimate is wrong by more than 20%, users will stop trusting the product — even if all other features work well.

### Status: 🔄 PENDING | Reasonable assumption; needs validation post-launch

### Evidence Supporting
- **Interview 012 (Vikram)**: "If Ledger told me I'd owe $15K and I actually owed $28K, I'd never use it again."
- **Interview 013 (Rachel)**: "The whole point is to not be surprised. If the tool surprises me, that's worse than nothing."
- **General pattern**: TC users have been burned before — their trust bar for accuracy is higher than for other features

### Confidence Level: **MEDIUM-HIGH** (intuitive; not directly tested)

### Action Items
- Q1: Define estimate algorithm with external CPA review; target ±15% accuracy
- Q2: Monitor estimate accuracy from day 1 of launch; alert when deviation > 15%
- Q4: Publish internal estimate accuracy report; adjust algorithm if needed

---

## Summary Table

| Hypothesis | Status | Confidence | Next Action |
|---|---|---|---|
| H1: Dynamic estimates reduce underpayment anxiety | ✅ Concept / 🔄 Pending | High | Launch Q2; post-filing accuracy study |
| H2: Year-round visibility changes saving behavior | ✅ Validated | High | Launch Q2; behavioral survey Q3 |
| H3: April Surprise drives acquisition | ✅ Pain / 🔄 Pending | High / Medium | A/B test messaging Q2 |
| H4: Deduction tracking has clear dollar ROI | 🔄 Backlog | Medium | Prototype Q3; validate before building |
| H5: Multi-stream income needs breakdown view | 🔄 Backlog | Medium-High | Design Q3; validate with Nathan + Leo |
| H6: Done-for-you tax prep is preferred | ⚠️ Rejected | Medium-High | Build transparent self-service; not outsourcing |
| H7: Estimate accuracy is a trust prerequisite | 🔄 Pending | Medium-High | Define algorithm Q1; monitor from day 1 |

---

**Related Documents**:
- `/pm-brain/tax-compliance/signals-synthesis.md` — Full TC customer signal analysis
- `/pm-brain/tax-compliance/team-okrs.md` — Team KRs these hypotheses inform
- `/leadership-brain/hypothesis-evidence.md` — Cross-team strategic bets
