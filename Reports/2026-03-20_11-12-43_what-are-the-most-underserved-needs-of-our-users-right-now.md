# What are the most underserved needs of our users right now

*Generated March 20, 2026 at 11:12*

---

# Most Underserved User Needs — Ledger

Based on cross-referencing interview evidence, validated bets, competitive gaps, and market shifts, here are the most underserved needs ranked by urgency and evidence strength.

---

## 1. 🔴 Cross-Platform Cashflow Visibility (Multi-Stream Income)

**The gap**: Users have income flowing through Stripe, PayPal, bank transfers, and other platforms — but no single view of their real cash position.

**Evidence**:
- 7/20 users use 3+ tools for finance (Strategic Bets doc)
- Interview 008 (Michael): "FreshBooks is good, but syncing with Asana + Quickbooks is constant friction"
- Interview 020 (Leo): "Wouldn't want to go back to Stripe + spreadsheet"
- Market Shifts doc: Average solopreneur now has **2.3 income streams** (up from 1.8 in 2020)

**Why it's underserved**: No competitor provides cross-platform cashflow that works *above* payment rails. Stripe, Square, and PayPal only show data from their own rails. Pulseflow is agency-only. QuickBooks is too complex.

**OKR linkage**: O2/KR1 — 80% of MAU using cashflow/decision-making features

---

## 2. 🔴 Automated Payment Follow-Up (Without Emotional Cost)

**The gap**: Users know they need to chase late payments but won't do it manually because it feels awkward or aggressive.

**Evidence**:
- **8/10** invoicing interviewees mentioned anxiety about payment follow-up
- Interview 001 (Maya): *"I don't want to be the person who nags people for money; if it's automated, it's okay"*
- Interview 003 (Sarah): *"If the system handled it automatically, I'd invoice weekly instead of quarterly"*
- Late payment rates on freelance invoices are **up 14% YoY** (Freshbooks Industry Report, 2023)
- Average days-to-payment grew from 32 days (2021) to **41 days (2023)**

**Why it's underserved**: Competitors have reminders, but none have addressed the *emotional* design layer — tone, framing, and psychological safety of automated follow-up. This is Bet 2 (Emotion > Features), validated at HIGH confidence.

**OKR linkage**: O1/KR1 — reduce time on invoicing by 50%

---

## 3. 🟠 Year-Round Tax Clarity With Dynamic Estimates

**The gap**: Users currently get one surprise in April. They want to see their tax liability building in real time, by month, so they can save and plan proactively.

**Evidence**:
- Interview 013 (Rachel): *"Owed $35K in April; couldn't believe it; would have saved differently if I saw it coming"*
- Interview 012 (Vikram): *"Last year surprised with $40K tax bill; this year planning ahead because I see profit monthly"*
- **8/10** tax interviews mention the "April surprise" as a core pain
- TaxWise Pro (8,000 users) offers only static annual estimates — a major product gap

**Why it's underserved**: TaxWise Pro's estimate is static. Cleo Finance's is basic. No competitor offers *dynamic, rolling* quarterly estimates that adapt to variable income — which is exactly what solopreneurs need (Bet 5, validated HIGH confidence).

**OKR linkage**: O1/KR2 — 70% of users report confidence in tax position (7+/10)

---

## 4. 🟠 Decision-Making Support (Hiring, Pricing, Investments)

**The gap**: Users make major business decisions (hire someone? buy a tool? raise rates?) with no financial modeling — they default to conservatism out of uncertainty.

**Evidence**:
- **7/20** users make conservative decisions due to financial uncertainty (Strategic Bets doc)
- Interview 011 (Emma): *"With quarterly estimates, I could decide whether to invest in tools"*
- Interview 020 (Leo): *"Profit by project helps me set pricing for future work"*
- Interview 015 (Sophie): *"Ledger helped me model S-Corp decision"*

**Why it's underserved**: **Zero competitors** own this space. Meridian does scenario planning but for teams of 2–50, at $149/mo. No tool serves the solopreneur or small agency owner who needs a simple "what if I hire?" calculator.

**Caveat**: This is validated at concept level, but the *product* is untested — it's Bet 4 (MEDIUM-HIGH confidence). It's high opportunity but higher build risk.

**OKR linkage**: O2/KR1 and KR3 — decision-making feature adoption + proof points

---

## 5. 🟡 Deduction Awareness & Capture

**The gap**: Users are leaving money on the table — not because they're dishonest, but because they don't know what's deductible or how to allocate mixed-use expenses.

**Evidence**:
- Interview 016 (Nathan): *"I have no methodology for allocation; probably conservative on deductions"*
- Interview 019 (Fiona): *"Want to optimize deductions but don't know how"*
- Secondary research: Studies suggest **15–25% deduction gap** for small businesses (Bet 9)

**Why it's underserved**: This is Bet 9 — currently a **LOW confidence hypothesis** with no product validation yet. It's real pain, but Ledger hasn't built toward it. Scheduled for Q3–Q4 research.

**OKR linkage**: O1/KR2 (tax clarity and confidence)

---

## Priority Matrix

| Need | Evidence Strength | Competitive Gap | Build Complexity | Priority |
|---|---|---|---|---|
| Cross-platform cashflow visibility | HIGH | HIGH | Medium | 🔴 Ship now |
| Automated reminders (emotional design) | HIGH | HIGH | Low | 🔴 Ship now |
| Dynamic tax estimates (rolling) | HIGH | HIGH | Medium | 🔴 Ship now |
| Decision-making tools (hiring/pricing) | MEDIUM-HIGH | Very High | High | 🟠 Q3 build |
| Deduction capture & suggestions | LOW | Medium | Medium | 🟡 Q4 hypothesis test |

---

## Bottom Line

The **three highest-urgency gaps** are all in the compliance + cashflow foundation:
1. Users can't see their full cash picture across platforms
2. Users won't chase payments manually — automation with the right *tone* is the unlock
3. Users are blindsided by taxes every April — rolling estimates fix this

Decision-making tools (Bet 4) are the **strategic differentiator** but require the foundation to exist first. They're the right Q3 bet, not Q1–Q2.
