# Interview 004: Tom Rodriguez

**Date**: February 5, 2024  
**Duration**: 62 minutes  
**Role**: CEO/Founder  
**Business**: Consulting Firm (Digital Strategy)  
**Business Model**: Project-based consulting (3-6 month engagements, $10K-$100K per project)  
**Company Size**: 15 people  
**Annual Revenue**: ~$2.2M  
**Years in Business**: 10  
**Current Tools**: Quickbooks, Salesforce, Harvest (time tracking)  
**Ledger Status**: Non-user (not interested in switching from QB)

---

## Background & Context

Tom's consulting firm is established and growing. He works with enterprise and mid-market clients on digital transformation projects. The business is complex: engagements often have fixed fees with time-and-materials components, retainers with variable usage, and complex contract terms.

Tom has invested heavily in systems. He's not looking to rip-and-replace; he's looking for point solutions that integrate with what he has.

---

## The Problem: Invoicing Complexity

### The Real Problem (Not Just Tooling)

**Tom's own words**: "Our invoicing is complicated because our contracts are complicated. A tool can't fix that."

Tom's invoicing process involves ambiguous scope, variable rates, and contract interpretation. The bottleneck is not the tool—it's the process.

### A Specific Example

**Engagement details**:
- **Fixed component**: $40K fixed fee for 4 months of strategic consulting
- **T&M component**: Additional work at $250/hr (if out of scope)
- **Reality**: After 3 months, client requested extra work. Out-of-scope work accumulated to $15K.
- **The problem**: Now Tom needs to invoice for $40K + $15K, but needs to justify the T&M hours.

**Process that follows**:
1. Harvest tracks time (says 60 hours of T&M)
2. Consultant prepares invoice with hours breakdown and rate justification
3. Finance team reviews: "Is this aligned with contract? Did we agree to $250/hr?"
4. Legal team reviews: "Can we legally charge this? Is it consistent with terms?"
5. Client finance team reviews: "Wait, we didn't approve this scope."
6. Back-and-forth negotiation for 1-2 weeks

**Total time to invoice**: 4-6 hours of coordination across teams  
**Bottleneck**: Finance/legal approval, not invoice generation

---

## Current Workaround

**Current system**:
1. **Harvest** tracks time logged to projects
2. **Spreadsheet** consolidates scope, agreed rates, hours, and calculations
3. **Quickbooks** generates invoice based on spreadsheet data
4. **Finance review** - Finance manager checks contract against invoice (1-2 hours)
5. **Legal review** - Legal department checks contractual alignment (2-4 hours, sometimes days)
6. **Client communication** - Often need to clarify "what was in scope" before sending invoice

**Timeline**: 1-2 weeks from project completion to invoice sent

**Pain points**:
- Finance/legal review is the real bottleneck (not invoice generation)
- Back-and-forth with client about scope interpretation
- No automated way to track "scope creep"
- Difficult to forecast revenue when invoices are delayed 1-2 weeks post-project

---

## Tom's Current Needs (What He's Actually Looking For)

Tom's needs are *not* about invoicing. They're about contract management and scope tracking:

1. **Scope change workflows** - When a client requests out-of-scope work, can we automatically flag it for approval and rate confirmation?
2. **Contract-to-invoice reconciliation** - Does the invoice align with the signed contract? (This is what finance/legal are checking manually)
3. **Approval workflows** - Finance and legal sign off before invoice is sent (not a Ledger feature)
4. **Revenue recognition accuracy** - Make sure invoices match the engagement agreement

---

## Hypothesis: Does Ledger Solve Tom's Problem?

**Ledger Hypothesis**: "If we could auto-generate invoices from project data + time tracking, reducing manual admin, Tom would be interested."

⚠️ **Hypothesis challenged**:
- Tom's bottleneck isn't invoice *generation*; it's post-generation *review* and client communication
- He needs finance + legal approval workflows (Ledger doesn't offer this)
- Quickbooks is not the problem; contract complexity is the problem
- Tom is happy with QB; he doesn't want to rip-and-replace

---

## Segment-Specific Insight: High-ACV Professional Services

**Key finding**: As engagement complexity increases, invoicing complexity increases. Generic invoicing tools are insufficient.

**Tom's segment characteristics**:
- High ACV ($10K-$100K per engagement)
- Complex contracts (fixed + variable, retainers, usage-based)
- Multiple approval chains (finance, legal, sometimes client)
- Longer sales cycles (3-6 month engagement duration)
- Scope creep is a constant (requires approval workflows)

**Implication for Ledger**: Tom's segment is **not a good fit** for Ledger's initial GTM. Focus on solopreneurs + SMB agencies with simpler invoicing. Come back to Tom's segment later with more complex features.

---

## What Tom Actually Uses & Likes

**Quickbooks**: "It's complex, but it does what we need. I've invested time learning it. I'm not switching."

**Harvest**: "Accurate time tracking. We couldn't operate without it."

**Salesforce**: "Tracks all our deals. I know the pipeline."

**Finance spreadsheet**: "Where we build custom invoice logic before it goes to QB."

**Tom's philosophy**: "I don't need a new invoicing tool. I need better workflows around scope management and approval."

---

## Why Tom Wouldn't Use Ledger

1. **High switching cost** - He's invested in Quickbooks; not worth migrating
2. **Missing features** - Needs approval workflows, contract reconciliation, legal sign-off (Ledger doesn't have these)
3. **Complexity of invoicing** - Generic invoicing won't work; needs custom logic
4. **Trust in QB** - Quickbooks is his system of record; he trusts it for revenue recognition

---

## Follow-Up & Future Opportunity

**Possible future opportunity** (not now):
- Build a "scope management" layer on top of invoicing (for high-ACV services)
- Allow approval workflows before invoices are sent
- Integrate deeply with contract data to validate invoices against terms
- But this is a specialized product, not general invoicing

**For now**: Tom is a good learning interview (what *not* to target), but not a customer.

---

## Quotes for Learning (What Not to Do)

> "Our invoicing is complicated because our contracts are complicated. A tool can't fix that."

> "The bottleneck isn't invoice generation. It's approval and client communication after we generate it."

> "I've invested too much in Quickbooks to switch. I'd rather integrate with what I have."

---

## Key Takeaway

**Tom's interview reveals an important product boundary**: Ledger is great for **straightforward invoicing** (solopreneurs, SMB agencies). It's not great for **complex, high-ACV engagements** where scope ambiguity requires approval workflows and contract reconciliation.

This is healthy learning—knowing who *not* to target helps focus product development.

---

**Interview conducted by**: Marcus (Ledger founder)  
**Notes quality**: High (reveals product boundaries, shows different segment needs)  
**Confidence in insights**: HIGH  
**Key takeaway**: Complex invoicing needs are *not* about tooling; they're about process. Ledger should focus on simpler invoicing use cases.
