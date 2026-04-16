# Leadership Brain: Hypothesis-Evidence Tracking

**Purpose**: Track strategic bets across both PM areas. Show what we know, what we're testing, and what contradicts our assumptions.

**Updated**: Apr 2024 | **Format**: Organized by Bet (strategic hypothesis) + Status + Evidence

---

## Bet 1: Consolidation Beats Best-of-Breed

**Strategic Hypothesis**: Small business owners prefer one integrated tool (invoicing + taxes + cashflow) over three specialized tools.

### Status: VALIDATED

### Evidence Supporting
- **Interview 002 (Raj)**: "With 50 clients, invoicing + payment tracking in one place reduced admin by 3-4 hours/month"
- **Interview 010 (David)**: "I recommend Ledger because it consolidates; Wave + Quickbooks + Stripe is chaos"
- **Interview 008 (Michael)**: "FreshBooks is good, but having to sync with Asana + Quickbooks is a constant friction"
- **Interview 020 (Leo)**: "Using Ledger for invoicing + tax visibility; wouldn't want to go back to Stripe + spreadsheet"
- **General pattern**: 8/10 interviews mention fragmentation as pain; 7/20 use 3+ tools

### Confidence Level
**HIGH** — Multiple segments and use cases confirm this

### What We're Testing
- **Expansion features**: Can we consolidate more into Ledger without overwhelming users?
- **Integration APIs**: Can we reduce fragmentation by syncing with Stripe, Quickbooks, bank accounts?

### Questions
- Does consolidation create switching costs (good retention) or lock-in risk?
- At what point does feature bloat hurt UX?

---

## Bet 2: Emotion > Features

**Strategic Hypothesis**: Reducing anxiety and shame is more valuable to owners than adding advanced features.

### Status: VALIDATED

### Evidence Supporting
- **Interview 001 (Maya)**: "I don't want to be the person who nags people for money; if it's automated, it's okay"
- **Interview 003 (Sarah)**: "If the system handled it automatically, I'd invoice weekly instead of quarterly"
- **Interview 005 (Lisa)**: "No invoicing system because it feels pretentious; wants something simple, not formal"
- **Interview 009 (Priya)**: "I want to feel professional; Wave feels like accounting software, which intimidates me"
- **Interview 011 (Emma)**: "I'm anxious about taxes; want clarity, not features"
- **General pattern**: 5+ solopreneurs mention shame/anxiety as blocker; automation solves psychology

### Confidence Level
**HIGH** — Core barrier for solopreneur segment is emotional, not functional

### What We're Testing
- **Tone/psychology testing**: Does reminder phrasing matter? (Professional vs. casual vs. friendly)
- **Default settings**: Should we ship with "helpful tone" as default vs. letting owners configure?

### Questions
- Does emotion matter as much for agency owners (higher stakes)?
- Can we measure "reduced anxiety" as a product metric?

---

## Bet 3: Accountants Are Distribution Channel

**Strategic Hypothesis**: Accountants recommending Ledger to clients is more efficient (and more trusted) than direct sales.

### Status: MEDIUM VALIDATION (Need More Data)

### Evidence Supporting
- **Interview 010 (David)**: "As an accountant, I recommend Ledger to my clients because I use it myself"
- **Interview 013 (Rachel)**: "My CPA is my trusted advisor; if they suggested Ledger, I'd try it"
- **Interview 019 (Fiona)**: "My accountant handles everything; if they recommended a tool, I'd use it"
- **General pattern**: 3/20 mention accountant recommendation would influence them

### Confidence Level
**MEDIUM** — Only 1 direct validation (David); 2+ indirect signals. Need more research.

### What We're Testing
- **Accountant view MVP**: Can we build read-only dashboard for accountants?
- **Referral tracking**: Do accountant referrals have different LTV/retention?
- **Partner program**: Do accountants actively recommend if we incentivize/train them?

### Questions
- How do we acquire first 10 accountants?
- Do accountants prefer us as a referral partner or as a compliance tool?
- What's the deal structure that makes sense?

### Action Items
- **Immediate**: Reach out to David (Interview 010) to understand his recommendation workflow
- **Q2**: Design accountant view (read-only access for clients)
- **Q3**: Launch partner program; recruit 10 accountant pilots

---

## Bet 4: Decision-Making is Our Differentiator

**Strategic Hypothesis**: Competitors own compliance; we own decision-making (hiring, pricing, growth). This is where we win.

### Status: VALIDATED (Concept), UNTESTED (Product)

### Evidence Supporting
- **Interview 012 (Vikram)**: "Profit visibility by month tells me whether to expect tax bill; changed my savings behavior"
- **Interview 020 (Leo)**: "Profit by project helps me set pricing for future work"
- **Interview 002 (Raj)**: "Seeing unpaid invoices motivated me to systematically follow up"
- **Interview 015 (Sophie)**: "Ledger helped me model S-Corp decision"
- **Interview 011 (Emma)**: "With quarterly estimates, I could decide whether to invest in tools"
- **General pattern**: 7/20 mention making conservative decisions due to uncertainty; 5+ want help deciding

### Confidence Level
**MEDIUM-HIGH** — Concept validated; feature validation pending

### What We're Testing
- **Hiring calculator MVP**: Owner inputs "hire someone at $5K/mo"; see impact on profit
- **Pricing benchmark**: Owner sees how pricing affects revenue; tests impact
- **Cashflow forecasting**: Owner sees 60-day forecast; validates usefulness for planning

### Questions
- Do owners actually use decision-making features, or are they "nice to have"?
- What's the minimum feature set for decision-making (don't want to over-engineer)?
- Is decision-making valuable enough to charge premium pricing?

### Action Items
- **Q3**: Launch simple hiring impact calculator; measure adoption
- **Q3**: Launch pricing benchmark feature; track usage
- **Collect case studies**: "Business decisions enabled by Ledger" (to prove value)

---

## Bet 5: Year-Round Tax Visibility Reduces April Surprises

**Strategic Hypothesis**: Owners who see tax liability throughout the year (not just in April) will save proactively and reduce stress.

### Status: VALIDATED

### Evidence Supporting
- **Interview 012 (Vikram)**: "Last year surprised with $40K tax bill; this year planning ahead because I see profit monthly"
- **Interview 020 (Leo)**: "Using profit visibility to set aside $20K/quarter; would have panicked in April otherwise"
- **Interview 015 (Sophie)**: "Seeing profit helps me plan; makes strategic decisions (S-Corp) based on data"
- **Interview 013 (Rachel)**: "Owed $35K in April; couldn't believe it; would have saved differently if I saw it coming"
- **General pattern**: 8/10 tax interviews mention April surprise; all mention year-round visibility would help

### Confidence Level
**HIGH** — Multiple segments confirm this; behavioral change documented

### What We're Testing
- **Quarterly estimate accuracy**: Does our estimate match actual tax bill? (Validate model)
- **Behavioral change**: Do owners actually save proactively, or do estimates not change behavior?

### Questions
- Should we emphasize quarterly estimates or monthly profit visibility?
- What estimate algorithm is most accurate? (YTD profit × tax rate? Historical rates by segment?)

---

## Bet 6: Recurring Invoicing Saves Solopreneurs Time

**Strategic Hypothesis**: Solopreneurs with recurring clients will save 2-3 hours/month using automated recurring invoices.

### Status: VALIDATED (Concept), PENDING (Quantified Product Validation)

### Evidence Supporting
- **Interview 007 (Amara)**: "3-4 recurring clients on different invoice dates; manual invoicing = 2-3 hours/month"
- **Interview 003 (Sarah)**: "If invoicing was automatic, I'd invoice weekly instead of quarterly"
- **General pattern**: 3/10 IC interviews mention recurring invoicing saves time

### Confidence Level
**MEDIUM-HIGH** — Concept validated; need to measure actual time saved post-launch

### What We're Testing
- **Time savings measurement**: Does Amara actually save 2-3 hours/month with recurring invoicing?
- **Frequency change**: Does Sarah invoice weekly instead of quarterly when automatic?

### Questions
- Do owners actually prefer weekly recurring invoices, or monthly?
- Do we need per-client customization (different billing dates, amounts), or can we simplify?

### Action Items
- **Q2**: Launch recurring invoicing feature
- **Post-launch**: Survey Amara + similar segment on time savings
- **Track**: Invoice frequency trends (do owners invoice more when it's automatic?)

---

## Bet 7: Solopreneurs and Agencies Need Different Product

**Strategic Hypothesis**: Solopreneurs prioritize simplicity + emotion; agencies prioritize visibility + integration. One product can serve both, but defaults/onboarding should differ.

### Status: VALIDATED

### Evidence Supporting
- **Solopreneur findings** (Maya, Sarah, Lisa, Priya, Amara, Emma, Rachel, Olivia, Nathan):
  - Want simplicity, speed, emotional relief
  - Avoid complexity
  - Need automation to overcome anxiety

- **Agency findings** (Raj, James, Tom, Michael, Vikram, Carlos, Sophie, Marcus, Fiona):
  - Want visibility, integration, team features
  - Can handle complexity
  - Need data consolidation

### Confidence Level
**VERY HIGH** — Clear pattern across 20 interviews

### What We're Testing
- **Segment-specific onboarding**: Does simplified onboarding for solopreneurs vs. rich setup for agencies improve NPS?
- **Feature defaults**: Do different default settings improve activation by segment?

### Questions
- How do we avoid "two products" complexity in engineering?
- Should pricing differ by segment?

### Action Items
- **Q1-Q2**: Design segment-specific onboarding
- **Q2**: A/B test simplified vs. full UI by segment
- **Measure**: NPS + activation time by segment + onboarding path

---

## Bet 8 (Challenged): "Most Small Business Owners Want Done-For-You Tax Prep"

**Strategic Hypothesis**: Owners prefer outsourcing taxes to professionals vs. DIY.

### Status: ⚠️ CHALLENGED/REJECTED

### Evidence Contradicting
- **Interview 011 (Emma)**: "I want to file myself, but I need guidance"
- **Interview 016 (Nathan)**: "I want to understand my deductions, not just guess"
- **Interview 020 (Leo)**: "Transparency about profit helps me make decisions; I don't want to outsource"
- **Interview 015 (Sophie)**: "I want to understand my S-Corp decision, not just trust an accountant"
- **General pattern**: 5+ interviews emphasize wanting transparency + understanding, not outsourcing

### What We Learned
- Owners want **transparency + optional expert input**, not full outsourcing
- DIY + guidance model (what Ledger offers) resonates better than done-for-you
- Hybrid model works: owner sees data; can ask accountant for guidance (not entire tax prep)

### Confidence Level
**MEDIUM-HIGH** — Evidence contradicts initial hypothesis

### Implication
- **Don't build done-for-you tax prep; focus on transparency + guidance**
- Accountants remain valuable advisors (not competitors)
- This aligns with distribution bet (accountants recommend Ledger for transparency)

---

## Bet 9 (Backlog): Deduction Optimization Increases Tax Efficiency by 10-15%

**Strategic Hypothesis**: Small business owners leave 15-25% of potential deductions on the table. Ledger can suggest deductions, increasing tax efficiency.

### Status: 🔄 HYPOTHESIS (Not Yet Tested)

### Evidence Supporting
- **Interview 016 (Nathan)**: "I have no methodology for allocation; probably conservative on deductions"
- **Interview 019 (Fiona)**: "Want to optimize deductions but don't know how"
- **Secondary research**: Studies suggest 15-25% deduction gap for small businesses

### Evidence Needed
- Actual deduction capture before/after using Ledger
- Accountant feedback: Do they see clients claiming more when Ledger suggests?
- Tax return impact: Do owners save more money?

### Confidence Level
**LOW** — Hypothesis, not yet validated

### Questions
- How accurate can we be suggesting deductions by industry?
- Will owners trust Ledger's suggestions, or prefer accountant validation?
- Is this $X/month value proposition, or just nice-to-have?

### Action Items
- **Q3-Q4**: Research deduction patterns by industry
- **Q4**: Build MVP deduction tracker + suggestions
- **Post-launch**: Measure adoption + impact on tax savings

---

## Summary: Bets & Confidence Levels

| Bet | Status | Confidence | Action |
|-----|--------|-----------|--------|
| 1. Consolidation beats best-of-breed | ✅ Validated | HIGH | Ship integration APIs; measure tool consolidation NPS |
| 2. Emotion > features | ✅ Validated | HIGH | Tone/psychology testing; measure anxiety reduction |
| 3. Accountants are distribution | 🟡 Medium | MEDIUM | Launch accountant view MVP; track referral impact |
| 4. Decision-making is differentiator | 🟡 Concept validated | MEDIUM-HIGH | Ship decision features; collect case studies |
| 5. Year-round tax visibility | ✅ Validated | HIGH | Measure actual savings behavior; validate estimate accuracy |
| 6. Recurring invoicing saves time | 🟡 Concept validated | MEDIUM-HIGH | Launch; measure time savings post-launch |
| 7. Solopreneurs ≠ agencies | ✅ Validated | VERY HIGH | Build segment-specific UX; measure by segment |
| 8. Done-for-you tax appeal | ⚠️ Rejected | MEDIUM-HIGH | Pivot to transparency + guidance model |
| 9. Deduction optimization | 🔄 Hypothesis | LOW | Research Q3-Q4; build MVP |

---

## How to Use This Document

**For product decisions**: "Does this feature align with a validated bet, or are we pursuing untested hypotheses?"

**For prioritization**: Validated bets should be resourced first.

**For roadmap planning**: Backlog hypotheses (9) are Q3-Q4; core bets (1-7) drive Q1-Q2.

**For team alignment**: All three teams (leadership, invoicing PM, tax PM) reference this to ensure strategic alignment.

---

## Quarterly Review Process

Each quarter (Jan, Apr, Jul, Oct):

1. **Assess each bet**: Are we still on track? Any new evidence?
2. **Update status**: Validated → Ship. Challenged → Pivot. Hypothesis → Testing?
3. **Adjust roadmap**: Shift resources based on new evidence
4. **New interviews**: Always gathering evidence (quarterly customer research)

---

**Related Documents**:
- `/leadership-brain/company-okrs.md` — Strategic intent driving these bets
- `/pm-brain/*/hypothesis-evidence.md` — Team-specific hypothesis tracking
- `/research/primary-research/customer-interviews/` — Raw evidence
J