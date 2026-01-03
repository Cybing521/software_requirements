# Software Requirements Course Review

## 1. Requirement Elicitation (Getting Information)
**Definition:** Proactive process of identifying needs/constraints, not just "collecting". It is collaborative and analytical.

### Core Techniques
*   **Interviews:** Most common. Build rapport, stay in scope, active listening.
*   **Workshops:** Collaborative, uses ground rules, timeboxing, agenda.
*   **Focus Groups:** Representative users for attitudes/opinions (subjective).
*   **Observations:** Validating info, seeing actual workflow/problems.
*   **Questionnaires:** Large groups. Design is critical (mutually exclusive options, no leading questions).
*   **Document/Interface Analysis:** Studying legacy systems.

### Classification of Requirements
1.  **Business Requirements:** High-level business goals (e.g., Increase market share).
2.  **User Requirements:** User goals/tasks (User Stories/Use Cases).
3.  **Functional Requirements:** What the system must *do* (Observable behaviors).
4.  **Quality Attributes (Non-Functional):** How *well* the system does it.
5.  **Constraints:** Restrictions (Design, Implementation).
6.  **Business Rules:** Policies/Laws (Facts, Constraints, Action Enablers, Computations).
7.  **External Interfaces:** Hardware, Software, User connections.

---

## 2. Requirement Analysis (Modelling & Prioritising)
**Goal:** Refining elicitation results into structured models.

### Modelling Tools
*   **User Stories:** Agile format. "As a \<role>, I want \<goal> so that \<reason>".
*   **Use Cases:** Scenario-based. Includes Actor, Pre/Post-conditions, Normal Flow, Alternative Flows.
*   **Activity Diagrams:** Visualizing workflows.
*   **ER Diagrams & CRUD Matrix:** Data modelling and lifecycle (Create, Read, Update, Delete).

### Prioritisation Methods (Exam Key Point)
*   **In/Out:** Binary decision for a release.
*   **Pairwise Comparison:** Ranking by comparing two at a time.
*   **Three-level Scale:** High/Medium/Low based on **Importance** and **Urgency**.
*   **MoSCoW:** Must (Mental), Should, Could, Won't.
*   **Value/Cost/Risk:** Optimization formula: `Priority = Value / (Cost + Risk)`.

---

## 3. Requirement Specification (Documenting)
**Output:** Software Requirements Specification (SRS).

### SRS Components
*   **Introduction:** Purpose, Scope, Definitions.
*   **Overall Description:** User classes, Operating environment, Assumptions/Dependencies.
*   **System Features:** Functional requirements.
*   **Data Requirements:** Data dictionary, Reports.
*   **External Interfaces & Non-functional Reqs.**

### Quality Attributes (NFRs)
**External (User View):**
*   **Availability:** Uptime, MTBF.
*   **Performance:** Response time, Throughput.
*   **Usability:** Ease of learning/use.
*   **Security:** Authorization, Privacy, Integrity.
*   **Reliability & Safety.**

**Internal (Developer View):**
*   **Maintainability/Modifiability:** Ease of changing code.
*   **Portability:** Different environments.
*   **Reusability & Scalability.**

---

## 4. Requirement Validation (Checking Quality)
**Verification vs. Validation:**
*   **Verification:** "Are we building the product *right*?" (Conforms to specs).
*   **Validation:** "Are we building the *right* product?" (Meets user needs).

### Validation Techniques
*   **Peer Reviews:**
    *   **Informal:** Desk-check, Pass-around, Walkthrough.
    *   **Formal (Inspection):** Roles (Author, Moderator, Reader, Recorder), Entry/Exit criteria, strict process.
*   **Prototyping:**
    *   **Mock-up:** UI focused, throwaway.
    *   **Proof-of-concept:** Tech feasibility focused.
    *   **Throwaway:** For exploration/clarification.
    *   **Evolutionary:** Becomes the final product (high quality code needed).

### The V-Model (Testing Levels)
*   User Requirements $\leftrightarrow$ **Acceptance Testing**
*   Functional Requirements $\leftrightarrow$ **System Testing**
*   System Architecture $\leftrightarrow$ **Integration Testing**
*   Detailed Design $\leftrightarrow$ **Unit Testing**

---

## 5. Potential Exam Topics Checklist
- [ ] **Difference between Verification and Validation?**
- [ ] **Identify Requirement Types:** Given a statement, classify it (e.g., "Must respond in 2s" is Performance/NFR; "Must calculate tax" is Functional).
- [ ] **Prioritisation:** Explain MoSCoW or calculate priority using the Value/Cost/Risk formula.
- [ ] **Prototyping:** When to use Mock-up vs Proof-of-Concept? Throwaway vs Evolutionary?
- [ ] **Review Process:** Roles in a formal inspection.
- [ ] **V-Model:** Which test stage corresponds to which requirement stage?
- [ ] **Writing User Stories:** Correct format ("As a...").
