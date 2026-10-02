# Community AI Node 0.1 — Architecture

## Purpose

Community AI Node 0.1 is the smallest testable form of Community AI.

It is not a general chatbot and it is not yet a physical device. It is a governed decision layer that asks:

> Given the access requirements the community has declared and the current environmental conditions, which available action best increases meaningful participation?

## Layer 1 — Declared needs

Inputs come from deliberate, governable sources such as:

- accessibility preferences;
- service requests;
- route feedback;
- public accessibility reports;
- neighborhood surveys;
- community-maintained datasets.

The prototype does not require passive classification of people.

## Layer 2 — Environment

Environmental state can include:

- slope;
- curb condition;
- crossing duration;
- elevator availability;
- route closure;
- seating;
- lighting;
- noise;
- weather;
- transit status.

## Layer 3 — Access state

```text
A(t) = [m, p, r, s, c, l, e, g]
```

Each dimension is normalized to `0..1` and describes the degree of access support currently required.

## Layer 4 — Participation objective

```text
x*(t) = arg max_x E[Participation(x | A(t), E(t))]
```

Candidate actions are evaluated for how well they improve participation under the current state.

## Layer 5 — Governance gates

Every candidate action must satisfy:

```text
Access(x)  >= τA
Privacy(x) >= τP
Agency(x)  >= τG
```

An action that fails a required gate cannot win merely because its utility score is high.

## Layer 6 — Explanation

The system should return:

- selected action;
- participation score;
- access/privacy/agency gate results;
- source provenance;
- uncertainty;
- a human-readable explanation.

## Later layers

Only after this deterministic core works should the project add:

1. local open-weight model for language interaction;
2. local database / map layer;
3. multimodal accessible interface;
4. edge hardware;
5. field testing;
6. measured compute profiling;
7. optional custom accelerator research.

The hardware should be derived from the workload, not imagined before the workload exists.
