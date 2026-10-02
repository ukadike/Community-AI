# Community AI

**A locally governed accessibility intelligence prototype from Small Systems Lab.**

Community AI begins with a simple proposition:

> **Access is a condition of correctness.**

Instead of beginning with a large AI model and searching for a community in which to deploy it, Community AI begins with people, place, access needs, and local governance.

```text
person → street → community → need → system → infrastructure
```

## Community AI Node 0.1

The first prototype is software.

It is designed to test whether an AI system can use **community-declared access requirements** and **environmental conditions** to choose actions that increase meaningful participation without sacrificing privacy or agency.

The system does **not** infer disability or diagnosis from a person's body, face, gait, voice, or identity.

## Access state

```text
A(t) = [m, p, r, s, c, l, e, g]
```

- `m` — mobility and path access
- `p` — pace and timing access
- `r` — reach and physical interaction
- `s` — sensory and perceptual access
- `c` — cognitive-load access
- `l` — language and communication access
- `e` — environmental access
- `g` — agency, consent, and control

The current access state is modeled from deliberately shared community requirements and environmental conditions:

```text
P(A(t) | D(t), E(t))
```

where:

- `D(t)` = declared or community-governed access requirements
- `E(t)` = environmental conditions

## Participation objective

```text
x*(t) = arg max_x E[ Participation(x | A(t), E(t)) ]
```

Subject to:

```text
Access(x)  >= τA
Privacy(x) >= τP
Agency(x)  >= τG
```

The optimization target is **participation, not classification**.

## Repository structure

```text
Community-AI/
├── README.md
├── index.html
├── ARCHITECTURE.md
├── schemas/
│   └── access-state.schema.json
├── src/
│   ├── governance.py
│   └── participation.py
└── examples/
    └── neighborhood-scenario.json
```

## Development sequence

1. Formalize the access-state schema.
2. Implement deterministic participation scoring.
3. Enforce access, privacy, and agency gates.
4. Test against neighborhood scenarios.
5. Add a local open-weight language model only after the deterministic layer works.
6. Move the same engine onto edge hardware.
7. Measure actual compute requirements before considering custom silicon.

## Governance defaults

Community AI should prefer:

- community-declared needs over inferred personal characteristics;
- minimum necessary data;
- local processing where appropriate;
- anonymous or aggregated information;
- visible system rules;
- explicit uncertainty;
- human challenge and override;
- accessible explanations;
- community control over retention and use.

## Small Systems Lab

Community AI is being developed through **ECHO**, Small Systems Lab's AI-governance research branch, and may later connect to African Sovereign Compute for edge hardware and compute infrastructure research.

**Build from the street outward.**
