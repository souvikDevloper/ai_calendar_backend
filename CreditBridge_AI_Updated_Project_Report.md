# CreditBridge AI

## Technical Progress and Implementation Report

**Version:** 0.5.0  
**Report date:** 22 June 2026  
**Prototype status:** Runnable full-stack demonstration  
**Data classification:** Synthetic demonstration data only

---

## Executive Summary

CreditBridge AI is a consent-controlled alternate credit assessment platform for individuals and micro, small, and medium enterprises that do not have sufficient traditional credit history. The prototype demonstrates how a lender can combine verified alternative-data signals, psychometric responses, explainable machine learning, human underwriting controls, and post-sanction monitoring without treating the model as an autonomous sanctioning authority.

The current implementation is materially different from the initial concept deck. It contains a React progressive web application for borrowers, a separate lender portal, a FastAPI service, encrypted SQLite storage, role-based two-step authentication, a trained XGBoost and neural ensemble, real Tree SHAP explanations, model-governance evidence, revocable consent, maker-checker authorization, downloadable credit appraisal documents, and early-warning monitoring for active loans.

This is a hackathon and evaluation prototype, not a production banking platform. All customer records, source identifiers, transactions, model-training observations, decisions, and monitoring events are synthetic. Aadhaar, Account Aggregator, GSTN, UPI, bureau, telecom, messaging, and bank-core connections are simulated. The fairness report demonstrates the governance method on synthetic validation data and is not a regulatory certification.

### Current Progress Snapshot

| Capability | Current status | Evidence in prototype |
|---|---|---|
| Borrower digital journey | Implemented | OTP, eKYC simulation, profile, consent, source linking, assessment, fetch, score and consent centre |
| Alternative-data scoring | Implemented with synthetic signals | 26 approved features from eight consent-controlled source categories |
| Machine-learning model | Implemented | XGBoost classifier plus scikit-learn MLP probability component |
| Explainability | Implemented | Tree SHAP contributions on log-odds scale plus neural adjustment |
| Human decisioning | Implemented | Credit Officer maker and Branch Manager checker workflow |
| Consent governance | Implemented | Purpose, version, expiry, freshness, receipt, renewal, revocation and partial erasure |
| Security controls | Implemented for demo | OTP limits, JWT sessions, RBAC, password hashing and AES-256-GCM at-rest encryption |
| Post-loan monitoring | Implemented | Active loans, repayment signals, deterministic alerts and audited interventions |
| Model governance | Implemented | Validation metrics, confusion matrix, feature manifest and synthetic fairness comparison |
| Deployment package | Implemented | Local PowerShell launcher and multi-stage Docker image for port 7860 |
| Public cloud deployment | Not completed | Hugging Face Docker Space remains a deployment option |
| Live regulated integrations | Not implemented | Requires institutional approvals, contracts, security review and production adapters |

---

## 1. Problem Definition

Traditional lending processes depend heavily on bureau history, formal bank statements, documented income and collateral. A borrower may therefore be excluded even when their recent economic behaviour is stable and their need for credit is legitimate. The target problem is to create an alternate credit system that considers phone-bill consistency, e-commerce behaviour, geolocation stability, questionnaire-based risk, merchant ratings, bank cash-flow patterns when available, and other responsible indicators of creditworthiness.

CreditBridge AI addresses this gap through four design principles:

1. **Consent before access.** Selecting a source only grants permission. The borrower must also link and verify the relevant identifier before the prototype can fetch signals.
2. **Evidence over questionnaire-only scoring.** Psychometric answers are supporting evidence. Consented financial, payment, business and stability signals supply most of the underwriting context.
3. **Explanation before action.** The lender receives a score, estimated default probability, SHAP evidence, reason codes, missing-data warnings and source provenance.
4. **Human authorization.** The model recommends; a Credit Officer makes a recommendation; a distinct Branch Manager performs final review.

### 1.1 Target Users

- Thin-file individuals with limited or no bureau history.
- Informal and micro-business operators with digital payment or bill-payment footprints.
- Bank credit officers who need a structured appraisal workspace.
- Branch managers who must authorize or return recommendations.
- Portfolio and collections teams monitoring early signs of repayment stress.

### 1.2 Prototype Objective

The objective is to prove an end-to-end decision-support lifecycle:

```text
Authenticate -> identify borrower -> capture purpose-specific consent
-> verify source identifiers -> fetch synthetic source signals
-> complete psychometric assessment -> calculate score and explanations
-> officer recommendation -> independent manager authorization
-> active loan -> early-warning monitoring and intervention
```

---

## 2. Scope and Boundaries

### 2.1 Implemented Scope

- Borrower authentication using mobile OTP challenges.
- Staff password plus OTP authentication.
- English, Devanagari Hindi and Bengali borrower interfaces.
- Browser speech-synthesis read-aloud controls.
- eKYC demonstration and borrower profile capture.
- Independent consent for eight source categories.
- Source-specific identifier verification before data retrieval.
- Consent metadata, renewal, revocation, PDF receipt and access history.
- Five-question psychometric and behavioural assessment.
- Synthetic data fetching with source provenance and freshness.
- Trained XGBoost and MLP ensemble inference.
- Real Tree SHAP applicant-level explanations.
- Score, risk band, confidence, recommended limit, pricing guidance and review flags.
- Searchable lender case workspace and downloadable credit memo.
- Maker-checker sanction workflow with role separation.
- Active-loan creation only after checker-approved sanction.
- Early-warning portfolio monitoring and audited intervention actions.
- Installable PWA shell with offline fallback and reconnect status.
- Same-origin Docker deployment configuration.

### 2.2 Explicit Non-Scope

- No live Aadhaar or KYC verification.
- No live Account Aggregator consent manager or Financial Information Provider connection.
- No real UPI, GSTN, telecom, utility, e-commerce, merchant or bureau API.
- No SMS or email OTP delivery; the code is displayed in demo mode.
- No real customer data or production repayment outcomes.
- No production-grade fraud engine, loan origination system or core-banking posting.
- No regulatory certification, legal opinion or independent model validation.
- No PostgreSQL support in the current local build; SQLite URLs are supported.
- No guaranteed high-availability hosting on the free deployment option.

---

## 3. System Architecture

### 3.1 Logical Architecture

```text
Borrower PWA                 UCO Lender Portal
 - Authentication            - Case queue and risk review
 - Consent centre            - Credit Officer recommendations
 - Source linking            - Branch Manager approvals
 - Assessment                - Model governance
 - Score explanation         - Portfolio monitoring
          \                       /
           \---- React/Vite -----/
                    |
              Same-origin REST
                    |
               FastAPI service
        /-----------|------------\
 Authentication  Scoring      Workflow
 OTP/JWT/RBAC    XGB/MLP/SHAP  Consent/Maker-checker
        \-----------|------------/
                    |
      SQLite + AES-256-GCM encrypted JSON
                    |
        Synthetic model artifacts and seed data
```

### 3.2 Technology Stack

**Frontend**

- React with Vite.
- Tailwind CSS and application-specific responsive styles.
- i18next and react-i18next.
- Recharts for governance and risk visualizations.
- Lucide React for interface icons.
- Vitest, Testing Library and jsdom for UI tests.

**Backend and model**

- Python 3.11+ and FastAPI 0.124.2.
- Uvicorn 0.38.0.
- SQLite for local and ephemeral demonstration storage.
- XGBoost 3.0.2, scikit-learn 1.6.1 and NumPy 1.26.4.
- SHAP 0.48.0 and joblib 1.4.2.
- ReportLab 4.4.2 for credit memos and consent receipts.
- cryptography 45.0.3 for AES-GCM.
- PyJWT 2.10.1 for authenticated sessions.

### 3.3 Application Surfaces

| Surface | Route | Primary user |
|---|---|---|
| Borrower application and demo console | `/` | Borrower and presenter |
| Lender case workspace | `/uco-dashboard` | Credit Officer and Branch Manager |
| Model governance | `/model-governance` | Risk, governance and audit users |
| Portfolio monitoring | `/portfolio-monitoring` | Credit and portfolio staff |
| Interactive API documentation | `/docs` on backend | Technical evaluator |

---

## 4. Borrower Journey and Data Flow

### 4.1 Authentication

The borrower enters a ten-digit mobile number. The backend creates an OTP challenge that expires after five minutes. A maximum of five failed attempts is allowed. In demo mode, the OTP is returned visibly as `123456`; in production this response field would be disabled and delivery would use an approved messaging provider. Successful verification creates a revocable JWT session that expires after 30 minutes.

### 4.2 Identity and Profile

The eKYC interaction is a simulation. It demonstrates where an approved KYC provider would be integrated and how identity match and address stability could enter the evidence layer. It must not be represented as a live Aadhaar verification.

### 4.3 Consent Is Permission, Not a Data Link

The application separates two actions:

1. The borrower grants permission for a named purpose and source.
2. The borrower links the source-specific identifier and completes verification.

Examples include an Account Aggregator or masked bank handle, UPI ID, GSTIN, utility customer ID, phone account, merchant profile and e-commerce account. The fetch endpoint rejects a request when no source has been consented or when a consented source has no verified identifier. This prevents the unrealistic behaviour of obtaining data from a checkbox alone.

### 4.4 Alternative Data Sources

| Consent source | Example signals used by prototype | Intended underwriting question |
|---|---|---|
| Bank account / Account Aggregator | Inflow regularity, balance stability, average inflow, EMI burden | Is cash generation stable and affordable? |
| Phone bills | On-time ratio and recharge consistency | Does the borrower meet recurring commitments? |
| E-commerce | Order regularity, dispute rate, essential-purchase share | Is digital purchase behaviour stable and low-dispute? |
| UPI transactions | UPI consistency and merchant inflow share | Is there recurring digital business activity? |
| GSTN / business data | Sales stability, GST availability and vintage | Is the enterprise established and economically active? |
| Utility bills | On-time ratio and recurring-payment ratio | Are household or business obligations paid consistently? |
| Merchant ratings | Rating, review volume and complaint ratio | Is there independent reputation evidence? |
| Bureau-lite | Optional bureau fields when available | Is any traditional history available without making it mandatory? |

### 4.5 Behavioural Assessment

The five-question assessment covers response to irregular income, EMI priority, record keeping, intended use of funds and emergency buffer. Answers are converted to values between 0 and 1 and averaged. This produces the `intent_to_repay` explanatory subscore and the `behavior_score` model feature.

The questionnaire cannot independently establish creditworthiness. It is easy to manipulate and may be affected by literacy or cultural context. The prototype therefore treats it as a support signal and exposes its contribution rather than hiding it.

### 4.6 Fetch, Score and Result

After verified links exist, the demonstration fetch creates deterministic synthetic source signals. The score endpoint requires fetched signals, runs inference, stores the model version and explanations, and presents:

- Credit score from 300 to 900.
- Model-estimated default probability.
- Risk band and manual-review status.
- Confidence based on available evidence.
- Six interpretable underwriting subscores.
- Real SHAP contributions and neural adjustment.
- Evidence metrics with source, consent ID, fetch time and freshness.
- Reason codes and actionable review flags.
- Recommended limit and indicative pricing range.

---

## 5. Machine-Learning Methodology

### 5.1 Reproducible Synthetic Training Data

The committed model is trained on 8,000 synthetic observations using fixed seed `20260621`. A stratified 22% holdout creates 1,760 validation observations. The generated target represents a synthetic default event and has an overall default rate of 22.63%.

Synthetic training was selected because the team does not have permission to use sensitive banking data. This makes the pipeline reproducible and safe for demonstration, but it also means the validation results cannot be interpreted as evidence of performance on real Indian borrowers.

### 5.2 Approved Feature Contract

The model version `creditbridge-xgb-mlp-v1.0` accepts 26 numerical features:

| Domain | Model features |
|---|---|
| Cash flow and affordability | `inflow_regularity`, `balance_stability`, `monthly_inflow_norm`, `emi_to_inflow` |
| Phone discipline | `phone_bill_on_time_ratio`, `mobile_recharge_consistency` |
| E-commerce | `ecommerce_order_regularity`, `ecommerce_dispute_ratio`, `ecommerce_essential_purchase_ratio` |
| UPI and merchant inflows | `upi_consistency`, `merchant_inflow_ratio` |
| Business | `sales_stability`, `gst_available`, `business_vintage_norm` |
| Utility and recurring payments | `utility_on_time_ratio`, `recurring_payment_ratio` |
| Merchant reputation | `merchant_rating_norm`, `merchant_complaint_ratio` |
| Stability and identity | `geo_stability_norm`, `device_consistency`, `identity_match`, `address_stability` |
| Trust controls | `fraud_flags_norm`, `anomaly_count_norm` |
| Supporting and governance | `behavior_score`, `consent_coverage` |

`gender` and `location` are deliberately excluded from the model feature matrix. They are generated only for post-model fairness comparison. Location-related stability is represented by behavioural stability signals, not the name of a protected or socially sensitive geography.

### 5.3 Primary XGBoost Model

The XGBoost classifier uses 180 trees, maximum depth 3, learning rate 0.045, subsample 0.86, column sample 0.86, minimum child weight 4 and L2 regularization 2.2. These conservative settings constrain individual tree depth while retaining non-linear interactions among alternative-data signals.

### 5.4 Neural Probability Component

The secondary model is a scikit-learn multilayer perceptron. Inputs are standardized and passed through hidden layers of 18 and 8 ReLU units. The model uses regularization, early stopping and a fixed random seed. It provides a second non-linear probability estimate; the interface calls its ensemble effect a neural calibration adjustment.

### 5.5 Ensemble Probability

Let `p_xgb` be the XGBoost default probability and `p_mlp` be the MLP probability:

```text
p_ensemble = clamp(0.82 * p_xgb + 0.18 * p_mlp, 0.01, 0.35)
```

The 82/18 blend keeps the tree model primary because it supplies stable Tree SHAP explanations. The neural component has enough influence to demonstrate ensemble calibration without making the explanation inconsistent with the dominant model. The 1%-35% clamp is a prototype policy boundary used to keep seeded demonstrations interpretable; it would require independent validation before production use.

### 5.6 Credit Score Mapping

The final score is derived from the ensemble probability, not from a hand-weighted addition of the six displayed factor scores:

```text
credit_score = round(300 + 600 * exp(-5.5 * p_ensemble))
credit_score = clamp(credit_score, 300, 900)
```

A lower model-estimated default probability therefore produces a higher credit score. The exponential mapping provides stronger separation at the low-risk end while preserving the familiar 300-900 range.

### 5.7 Risk Bands

| Score | Band | Prototype policy treatment |
|---|---|---|
| 750-900 | Low Risk | May be recommended within cap after normal checks |
| 650-749 | Medium Risk | Conditional or reduced-limit review |
| 580-649 | Manual Review | Mandatory human verification |
| Below 580 | High Risk | No model-recommended limit; decline or documented escalation |

The band alone is not the decision. A nominally low-risk score can still be routed to manual review when evidence is missing, confidence is low, consent has become invalid or a high-severity anomaly exists.

### 5.8 SHAP Explainability

The XGBoost component is explained using `shap.TreeExplainer`. For each borrower, the backend returns:

- The XGBoost base value on the log-odds scale.
- A contribution for each approved model feature.
- Whether each contribution raises or reduces model risk.
- The normalized feature value and consent source.
- A separate neural ensemble adjustment.

For the tree component, the base value plus Tree SHAP contributions reconstructs the tree-model log odds within numerical tolerance. The neural adjustment is reported separately because Tree SHAP does not explain the MLP model.

### 5.9 Six Underwriting Subscores

The interface groups detailed evidence into six understandable views. These fixed weights support explanation, reason-code ranking and confidence calculation. They are **not direct coefficients of the final machine-learning score**.

| Subscore | Governance weight | Reason for emphasis |
|---|---:|---|
| Cash-flow strength | 25% | Repayment capacity depends primarily on recurring inflow and affordability |
| Payment discipline | 20% | Timely small recurring obligations are useful for thin-file applicants |
| Business health | 18% | Stability, vintage and independent merchant evidence indicate continuity |
| Stability | 14% | Identity, address, device and location continuity reduce verification uncertainty |
| Intent to repay | 13% | Psychometric evidence adds context but must not dominate observed behaviour |
| Trust flags | 10% | Fraud, anomalies, disputes and consent coverage can override otherwise strong indicators |

The subscore formulas are:

```text
Cash Flow = 35% inflow regularity
          + 25% inflow-to-stated-income score
          + 20% balance stability
          + 20% affordability score

Payment Discipline = 24% phone bill on-time ratio
                   + 26% utility on-time ratio
                   + 27% UPI consistency
                   + 23% recurring payment ratio

Business Health = 26% sales stability
                + 20% business vintage
                + 22% merchant inflow ratio
                + 20% merchant rating quality
                + 12% GST availability indicator

Stability = 30% geolocation stability
          + 25% device consistency
          + 25% identity match
          + 20% address stability

Intent to Repay = mean of five normalized assessment answers * 100

Trust = 78% anomaly/fraud/consent component
      + 22% e-commerce regularity/dispute/essential-purchase component
```

The detailed helper logic caps extreme values. For example, affordability declines as existing EMI rises relative to income; merchant quality combines rating, review volume and complaint ratio; fraud and anomaly counts reduce trust.

### 5.10 Evidence Confidence

Confidence measures evidence completeness and consistency; it is not a statistical confidence interval:

```text
weighted_subscore = sum(subscore_i * governance_weight_i)
consent_coverage  = active_consented_sources / 8

confidence = round(clamp(
    54 + 26 * consent_coverage + 0.35 * (weighted_subscore - 60),
    35,
    96
))
```

This design ensures that the display does not show a fixed percentage for every case. Missing consent and weak evidence reduce confidence even where the machine-learning score remains strong.

### 5.11 Recommended Limit and Pricing

The recommended limit is capped by both stated request and a risk-band multiple of monthly income:

```text
Low Risk       = min(requested amount, 2.40 * monthly income)
Medium Risk    = min(requested amount, 1.80 * monthly income)
Manual Review  = min(requested amount, 1.15 * monthly income)
High Risk      = 0
```

The amount is rounded upward to the nearest INR 10,000 for demonstration. Indicative pricing bands are 11%-13% p.a. for Low Risk, 13%-16% for Medium Risk and 16%-19% for Manual Review. Pricing is illustrative and is not a live UCO Bank product or approved rate card.

### 5.12 Review Flags

Human review is triggered or guided by:

- Confidence below 70%.
- Any subscore below 55 as high severity, or 55-62 as medium severity.
- Transaction anomaly signals.
- Missing consented evidence.
- Existing EMI affordability pressure.
- Stale score after consent change.
- Expired consent or purpose-version mismatch.
- Requested sanction above model limit without policy-exception reason.

---

## 6. Model Validation and Fairness Governance

### 6.1 Validation Results

The committed validation artifact reports:

| Metric | Result | Interpretation for this prototype |
|---|---:|---|
| Validation observations | 1,760 | Stratified holdout from 8,000 synthetic rows |
| ROC AUC | 0.7479 | Moderate synthetic rank separation |
| Accuracy | 0.6545 | Threshold-dependent overall correctness |
| Precision | 0.3694 | Many positive alerts are conservative false positives |
| Recall | 0.7462 | Most synthetic defaults are identified at the chosen threshold |
| F1 score | 0.4942 | Balance of precision and recall at threshold 0.18 |
| Brier score | 0.1544 | Synthetic probability error measure; lower is better |

The confusion matrix at probability threshold 0.18 is:

| Actual / predicted | No default | Default |
|---|---:|---:|
| No default | 855 | 507 |
| Default | 101 | 297 |

The selected threshold favours recall over precision. This is consistent with decision support that routes uncertain cases to human review, but it would increase operational review volume. A bank would select thresholds using real default costs, approval strategy, collections capacity and fairness constraints.

### 6.2 Synthetic Fairness Results

Protected fields are excluded from training and inference. They are retained only in the synthetic validation frame to compare outcomes.

| Comparison | Demographic parity difference | Equal opportunity difference | Demo threshold |
|---|---:|---:|---:|
| Gender groups | 0.0652 | 0.0787 | 0.10 |
| Geography groups | 0.0274 | 0.0008 | 0.10 |

The committed report marks both comparisons within the prototype threshold. Excluding protected attributes does not by itself guarantee fairness because other variables may act as proxies. Production governance would require representative data, subgroup sample-size controls, intersectional testing, drift analysis, adverse-action review and periodic independent validation.

---

## 7. Consent and Data Governance

### 7.1 Consent Metadata

Each source stores a consent identifier, purpose, purpose version, grant time, 30-day expiry, retention date, status, last access, last fetch, freshness, revocation time and deletion status. The borrower can download a consent receipt and inspect source access history.

### 7.2 Expiry and Purpose Changes

An expired consent or changed purpose version requires renewal. Dependent evidence becomes stale and an existing recommendation cannot be treated as current. The scoring and decision APIs enforce this state rather than relying only on interface warnings.

### 7.3 Revocation Behaviour

Revocation performs four linked actions:

1. Marks the source consent as revoked.
2. Removes the verified source link.
3. Invalidates dependent fetched evidence and marks the previous score stale.
4. Records an audit event.

The borrower must grant or renew consent, verify the source again, refetch signals and rescore before a current recommendation is available.

### 7.4 Partial Erasure

The demonstration supports compliant partial erasure. It pseudonymizes direct borrower identifiers and removes source links, behavioural answers, fetched alternative data and derived score data. It retains the minimum case reference, final banking decisions, timestamps and a non-sensitive deletion audit event. This illustrates the distinction between erasing optional analytical data and retaining records required for a lending decision; the actual retention policy would require legal and regulatory review.

### 7.5 Provenance

Officer evidence includes the source, consent ID, fetch timestamp and freshness. Provenance allows the reviewer to distinguish observed consented evidence from model-generated interpretation and missing data.

---

## 8. Authentication, Security and Privacy

### 8.1 Authentication Controls

- Borrower: mobile number plus OTP.
- Staff: password plus OTP.
- OTP lifetime: five minutes.
- Maximum failed OTP attempts: five.
- JWT session lifetime: 30 minutes.
- Logout: revokes the server-side session identifier.
- Password storage: scrypt with per-password salt.
- Seeded roles: `credit_officer` and `branch_manager`.
- Borrower ownership: borrower sessions can access only the matching phone-owned case.

### 8.2 Encryption at Rest

Sensitive borrower JSON columns are encrypted with AES-256-GCM using a unique 12-byte nonce for every write. Encrypted values have an `enc:v1:` envelope. The encrypted columns are profile, source links, behavioural answers, fetched signals and score results. Legacy plaintext rows are migrated to encrypted storage when the store initializes.

The local fallback key exists only for frictionless demonstration. A deployment must provide `DATA_ENCRYPTION_KEY` as a secret and must use managed key rotation, least-privilege access, backup protection and operational monitoring.

### 8.3 Transport Security Indicator

The application reports `TLS protected` only when the request is HTTPS or carries an HTTPS forwarding header. Local development accurately shows `Local HTTP demo`. The prototype does not claim end-to-end encryption because the server must decrypt data to perform scoring.

### 8.4 Audit Characterization

Authentication, consent, fetching, scoring, recommendations, checker reviews, alerts and interventions are written to an append-oriented audit table. The current SQLite audit is not cryptographically immutable or tamper-evident. A production design should use restricted write permissions, signed events or a write-once audit service, retention controls and independent security monitoring.

---

## 9. Lender Decision Workflow

### 9.1 Credit Officer as Maker

The Credit Officer can search cases and inspect applicant identity, score, probability, confidence, factor summaries, SHAP contributions, evidence, flags, consent ledger, access provenance and audit history. Available operational actions include requesting documents, initiating field verification, escalating a case and submitting approve, conditional-approve or decline recommendations.

Submitting a terminal recommendation does not sanction the loan. The case enters `pending_checker` state.

### 9.2 Branch Manager as Checker

The Branch Manager reviews the pending recommendation and can approve, return for clarification, reject or escalate it. A user cannot check their own recommendation. Final authorization is blocked when the score is stale or consent is no longer valid.

### 9.3 Policy Exceptions

An amount above the model-recommended limit requires a written policy-exception reason at maker stage and cannot be manager-approved as a normal sanction. It must be escalated to the credit committee path.

### 9.4 Loan Creation

Only a Branch Manager approval of an approve or conditional-approve recommendation creates an active loan. Both maker and checker identities, notes, timestamps and actions appear in the audit trail and credit memo.

### 9.5 Credit Appraisal PDF

The case-level memo includes applicant details, score, model-estimated default probability, evidence, SHAP reasons, review flags, consent state, policy checks, model version, officer recommendation, checker authorization and audit history.

---

## 10. Post-Loan Early-Warning Monitoring

The portfolio-monitoring page separates active-loan supervision from origination. It shows exposure, open alert count, days past due, EMI status, UPI inflow trend, bill punctuality, merchant rating, source freshness and warning band.

### 10.1 Deterministic Warning Rules

| Signal | Amber condition | Red or high condition |
|---|---|---|
| Days past due | Greater than 0 | At least 15 days |
| UPI inflow change | At or below -20% | At or below -40% |
| Bill delay | At least 5 days | Combined with other high deterioration |
| Merchant rating | Decline of at least 0.5 point | Escalated with other deterioration |
| Device or geolocation | Material anomaly | High-severity alert |

### 10.2 Intervention Actions

Staff can acknowledge an alert, contact the borrower, place the loan under enhanced monitoring, initiate field verification or recommend restructuring assessment. Every monitoring refresh, generated alert and intervention is audited.

The seeded Lata scenario demonstrates an amber warning: UPI inflows decline by 26%, a bill is delayed seven days and the EMI is two days past due. The purpose is to show explainable, early engagement rather than automatic punitive action.

---

## 11. Inclusion and PWA Behaviour

- Borrower UI is available in English, complete Devanagari Hindi and Bengali.
- Authentication, consent, errors and score explanations are translated.
- Browser speech synthesis uses `en-IN`, `hi-IN` and `bn-IN` where supported.
- Unsupported speech synthesis fails gracefully.
- The web manifest supports installation as a standalone PWA.
- The service worker caches only the application shell and static assets.
- `/api/` responses and sensitive borrower data are not cached.
- Only language and non-sensitive questionnaire progress may be persisted locally.
- Phone, Aadhaar, source identifiers, signals and scores are not intended for browser storage.
- Connection status and reconnect recovery are visible to the user.

---

## 12. Current Demonstration Personas

The following results were regenerated on 22 June 2026 using the committed model artifact and current API journey.

| Persona | Current result | Confidence | Ensemble risk | Limit | Decision interpretation |
|---|---|---:|---:|---:|---|
| Ramesh Kumar | 788, Low Risk | 90% | 3.77% | INR 120,000 | Strong consented cash-flow and payment evidence |
| Lata Devi | 798, Low Risk | 89% | 3.39% | INR 80,000 | Thin-file case supported by UPI and bill discipline |
| Aman Ali | 581, Manual Review | 81% | 13.78% | INR 40,000 | Cash-flow instability and weaker business evidence require review |
| Missing-data persona | 761, Low Risk score | 82% | 4.79% | INR 60,000 | Manual review remains true because important evidence is unavailable |

These outcomes are deterministic demonstration fixtures, not approval promises. The missing-data example is intentionally important: a high numerical score does not suppress the human-review requirement created by incomplete evidence.

---

## 13. API Surface

### 13.1 Authentication and Security

- `POST /api/auth/borrower/request-otp`
- `POST /api/auth/borrower/verify-otp`
- `POST /api/auth/staff/login`
- `POST /api/auth/staff/verify-otp`
- `GET /api/auth/me`
- `POST /api/auth/logout`
- `GET /api/security/status`

### 13.2 Borrower and Consent

- `POST /api/borrowers`
- `POST /api/borrowers/{id}/consents`
- `GET /api/borrowers/{id}/consents`
- `POST /api/borrowers/{id}/consents/{source}/revoke`
- `POST /api/borrowers/{id}/consents/{source}/renew`
- `POST /api/borrowers/{id}/data-deletion`
- `GET /api/borrowers/{id}/consent-receipt.pdf`
- `POST /api/borrowers/{id}/source-links`
- `POST /api/borrowers/{id}/behavioral`
- `POST /api/borrowers/{id}/fetch-signals`
- `POST /api/borrowers/{id}/score`

### 13.3 Officer, Governance and Workflow

- `GET /api/model/metrics`
- `GET /api/model/fairness`
- `GET /api/officer/cases`
- `GET /api/officer/cases/{id}`
- `GET /api/officer/cases/{id}/credit-memo.pdf`
- `POST /api/officer/cases/{id}/decision` as compatibility adapter
- `POST /api/officer/cases/{id}/recommendations`
- `GET /api/officer/approvals`
- `POST /api/officer/recommendations/{id}/review`
- `GET /api/audit/{borrower_id}`

### 13.4 Loans and Monitoring

- `GET /api/officer/loans`
- `GET /api/officer/loans/{id}`
- `POST /api/officer/loans/{id}/alerts/{alert_id}/action`
- `POST /api/demo/monitoring/{loan_id}/advance`
- `POST /api/demo/monitoring/seed-case/{borrower_id}`

Demo reset, monitoring advancement and case seeding are protected staff operations and are intended only for evaluation.

---

## 14. Data Storage

SQLite contains the following logical records:

- `borrowers`: encrypted profile, links, answers, signals and scores plus consent state.
- `decisions`: final or operational decision records.
- `audit`: append-oriented event history.
- `auth_users`: staff identity, role and password hash.
- `auth_challenges`: OTP hashes, expiry, attempt count and usage.
- `auth_sessions`: JWT session identifiers, expiry and revocation.
- `recommendations`: maker action, amount, conditions, exception, checker state and identities.
- `loans`: active exposure, rate, term, due date, delinquency and warning state.
- `monitoring_snapshots`: period-level monitoring metrics.
- `monitoring_alerts`: warning reason, severity, status and intervention.

The schema supports backward-compatible addition of consent metadata and migrates legacy sensitive plaintext JSON on initialization. The local build accepts SQLite `DATABASE_URL` values; PostgreSQL remains a planned production change rather than a current capability.

---

## 15. Verification Results

Fresh verification on 22 June 2026 produced:

- Backend: **20 tests passed** in 48.29 seconds using Python 3.11.
- Frontend: **11 tests passed** across two Vitest files.
- Frontend production build: **passed**, transforming 2,327 modules.
- Build output: 752.22 kB JavaScript, 216.77 kB gzip.
- Residual build warning: the main JavaScript chunk exceeds Vite's 500 kB advisory threshold and should be split before production.

The tests cover score outcomes, SHAP consistency, consent and link prerequisites, model governance, consent revocation, stale rescoring, credit memo generation, OTP and session behaviour, encrypted storage, maker-checker restrictions, monitoring alerts, consent renewal, expiry, partial erasure, ownership authorization, UI governance, multilingual content and consent confirmation.

### 15.1 Important Remaining Test Gaps

- No external penetration test or dependency-security assessment.
- No real-browser end-to-end suite against every supported viewport.
- No load, concurrency, recovery or long-running session testing.
- Docker configuration exists, but the Docker runtime was not available in the current verification environment.
- No integration tests against live AA, KYC, GSTN, UPI, bureau or core-banking systems.

---

## 16. Running and Deployment

### 16.1 Local Windows Start

Prerequisites are Python 3.11 or 3.12, Node.js 20+, npm and PowerShell.

```powershell
.\start-dev.ps1
```

If script execution is blocked:

```powershell
powershell -ExecutionPolicy Bypass -File .\start-dev.ps1
```

Default development URLs:

- Borrower app: `http://127.0.0.1:5173`
- UCO portal: `http://127.0.0.1:5173/uco-dashboard`
- Model governance: `http://127.0.0.1:5173/model-governance`
- Portfolio monitoring: `http://127.0.0.1:5173/portfolio-monitoring`
- FastAPI documentation: `http://127.0.0.1:8000/docs`

Demo staff accounts:

- Credit Officer: `officer@creditbridge.demo` / `Demo@123`
- Branch Manager: `manager@creditbridge.demo` / `Demo@123`
- Demo OTP: `123456`

### 16.2 Docker and Hugging Face Space

The multi-stage image builds React and serves the compiled SPA through FastAPI on port 7860 with deep-link fallback.

```powershell
docker build -t creditbridge-ai .
docker run --rm -p 7860:7860 `
  -e JWT_SECRET="replace-me" `
  -e DATA_ENCRYPTION_KEY="replace-me" `
  creditbridge-ai
```

A free Hugging Face Docker Space can host the same image. Free CPU Spaces sleep when unused and do not guarantee 24/7 availability. Waking starts the already-built image and loads the bundled artifacts; dependencies rebuild only when the image is rebuilt after source or configuration changes. SQLite is intentionally ephemeral and seeded data may reset after container restart.

`JWT_SECRET` and `DATA_ENCRYPTION_KEY` must be configured as Space secrets and must never be committed to a public repository.

---

## 17. Production Readiness Assessment

### 17.1 What the Prototype Proves

- A realistic consent and source-linking journey can be demonstrated end to end.
- Alternative-data evidence can be converted into a reproducible model feature contract.
- A trained model, probability mapping and real SHAP explanations can be exposed to officers.
- Missing or revoked evidence can invalidate an earlier score.
- Human recommendations and independent authorization can be enforced by API roles.
- Monitoring can continue after sanction with explainable warning rules and intervention history.

### 17.2 What Must Happen Before Real Lending

1. Obtain lawful access to representative, permissioned historical data and define outcome labels.
2. Conduct data-quality, leakage, stability, bias and proxy-variable assessment.
3. Retrain and independently validate the model on real out-of-time samples.
4. Calibrate probability and score mapping against actual observed defaults.
5. Define product-specific eligibility, affordability, pricing, limit and exception policies.
6. Complete legal, RBI, privacy, KYC/AML, cybersecurity and fair-lending reviews.
7. Integrate approved consent manager, Financial Information Providers, KYC, fraud, LOS and core systems.
8. Move to managed PostgreSQL or an institutional data platform with migrations, backups and recovery.
9. Introduce a key-management service, rotation, secrets management, tamper-evident audit and SIEM monitoring.
10. Add accessibility certification, penetration testing, SAST/DAST, dependency scanning and incident response.
11. Deploy high-availability infrastructure with queues, observability, rate limits and disaster recovery.
12. Establish model monitoring for drift, calibration, fairness, overrides, stability and portfolio outcomes.

### 17.3 Claims That Should Not Be Made

The current prototype should not be described as RBI certified, production compliant, connected to live Aadhaar or Account Aggregator data, trained on real customers, guaranteed fair, continuously available or capable of making autonomous banking sanctions.

---

## 18. Recommended Judging Demonstration

1. Start with the problem and state clearly that all data is synthetic.
2. Authenticate as Ramesh and show the `2-step verified`, at-rest protection and local-HTTP indicators.
3. Grant purpose-specific consent and explain that permission alone does not fetch data.
4. Link each selected source and show verification before fetch.
5. Complete the psychometric assessment and stress that it is only supporting evidence.
6. Generate the score and explain the 82/18 ensemble, exponential score mapping and real SHAP waterfall.
7. Open the officer portal, inspect evidence provenance and submit a maker recommendation.
8. Sign in as Branch Manager and demonstrate independent checker authorization.
9. Open the active-loan page and show Lata's explainable amber warning and an intervention.
10. Open model governance and discuss AUC, recall/precision trade-off, protected-field exclusion and limitations.
11. Revoke one consent source and demonstrate that evidence and the prior score become stale.
12. Download the consent receipt and credit memo to close the auditability story.

---

## 19. Conclusion

CreditBridge AI now demonstrates more than a score screen. It presents a full alternate-credit lifecycle: authenticated onboarding, source-specific consent, verified links, alternative evidence, psychometric support, trained machine-learning inference, SHAP explanation, role-separated authorization, revocable data rights and post-loan monitoring.

The strongest aspect of the prototype is not a claim that synthetic model performance is production-ready. Its value is the coherent control framework around the model: consent validity, evidence provenance, missing-data safety, human authorization, audit records and ongoing risk monitoring. The next stage is institutional validation using lawful representative data and production-grade integrations, security and governance.

---

## Appendix A: Model Reproduction

The trained artifact is committed. Retraining is optional and deterministic:

```powershell
cd backend
py -3.11 -m app.train_model
```

This regenerates the joblib bundle, validation metrics, fairness report and model manifest using fixed seed `20260621`.

## Appendix B: Test Commands

```powershell
cd backend
$env:PYTHONPATH = (Get-Location).Path
py -3.11 -m pytest -q
```

```powershell
cd frontend
npm test
npm run build
```

## Appendix C: Principal Source Files

| File | Responsibility |
|---|---|
| `backend/app/main.py` | API routes, authorization and workflow enforcement |
| `backend/app/auth.py` | OTP, JWT sessions, revocation and role authentication |
| `backend/app/security.py` | AES-256-GCM JSON encryption and scrypt password hashing |
| `backend/app/modeling.py` | Feature contract, inference, score mapping and SHAP |
| `backend/app/train_model.py` | Synthetic data generation, training, validation and fairness artifacts |
| `backend/app/scoring.py` | Subscores, evidence, confidence, limits, reason codes and flags |
| `backend/app/store.py` | SQLite schema, encryption migration and persistence |
| `backend/app/monitoring.py` | Early-warning bands, alert rules and seeded time series |
| `backend/app/memo.py` | Credit memo and consent receipt PDF generation |
| `backend/tests/test_api.py` | Backend journey, security, model and workflow tests |
| `frontend/src/App.jsx` | Borrower, officer, governance and monitoring interfaces |
| `frontend/src/i18n.js` | English, Devanagari Hindi and Bengali translations |
| `frontend/src/App.ui.test.jsx` | UI governance, explanation and consent tests |
| `frontend/public/sw.js` | PWA shell caching and offline fallback |
| `Dockerfile` | Multi-stage production image for port 7860 |

---

*CreditBridge AI v0.5.0 - Technical Progress and Implementation Report*  
*Prepared from the verified repository state on 22 June 2026.*
