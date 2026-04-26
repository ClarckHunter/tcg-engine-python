# TCG Engine — Modular Card Game Rules Engine

A modular and extensible **Trading Card Game rules engine** designed to execute complex card interactions through composable systems instead of hardcoded logic.

This project focuses on **architecture, scalability, and maintainability**, allowing new cards and mechanics to be implemented without modifying core engine logic.

---

## 🚀 Project Status

**Active Development**

Current focus:

* Core gameplay architecture
* Effect execution pipeline
* Query system design

This repository represents the **engine foundation**, not a finished game.

---

## 🎯 Goal

Traditional card games often implement mechanics using conditional logic scattered across the codebase.

This engine explores a different approach:

> Cards are *data*
> Mechanics are *composable behaviors*
> The engine is a *rule executor*

The objective is to make complex interactions possible without rewriting existing systems.

---

## 🧠 Core Concepts

### Ability

Represents a playable action or triggered behavior.

An ability is composed of:

* **Conditions** → determine if execution is valid
* **Selects** → resolve targets dynamically
* **Effects** → modify game state

```
Ability
 ├── Conditions
 ├── Selects
 └── Effects
```

---

### Effect System

Effects are isolated executable objects.

Instead of:

```
if card == fireball:
    damage(target)
```

The engine executes:

```
DamageEffect(target, amount)
```

This allows:

* reusable mechanics
* predictable execution order
* easier balancing and testing

---

### Query System

The Query system dynamically retrieves entities from the game state.

Examples:

* all enemy units
* lowest health target
* random card from deck

Queries separate **selection logic** from **effect execution**, preventing tightly coupled gameplay code.

---

### Execution Flow

1. Ability requested
2. Conditions validated
3. Targets resolved via queries
4. Effects executed sequentially
5. Game state updated

---

## 🏗 Architecture Principles

* Composition over inheritance
* Data-driven design
* Decoupled gameplay logic
* Deterministic execution
* Extensible rule system

The engine is intentionally designed so that **new mechanics require extension, not modification**.

---

## ⚡ Quick Start

Clone the repository:

```
git clone https://github.com/ClarckHunter/tcg-engine-python
cd tcg-engine-python
```

Run example:

```
python example.py
```

*(Example script demonstrates ability execution flow.)*

---

## 📦 Current Features

* Modular Ability system
* Effect execution pipeline
* Query abstraction layer
* Condition validation system
* Early combat rule modeling

---

## 🗺 Roadmap

* [x] Ability architecture
* [x] Effect system
* [x] Query system
* [ ] Turn manager
* [ ] Event system
* [ ] Serialization layer
* [ ] Card definition format
* [ ] Editor tooling
* [ ] Playable prototype

---

## 🤔 Design Decisions

### Why object-based effects?

To allow stacking, ordering, logging, and replayability without procedural coupling.

### Why separate Select from Effect?

Target resolution should not modify state.
This guarantees predictable execution and easier debugging.

### Why build an engine instead of a game first?

The goal of this project is exploring scalable game architecture before content production.

---

## 👨‍💻 About the Project

This engine is being developed as part of my ongoing study of:

* software architecture
* system design
* game engine patterns
* scalable rule execution

It serves both as an experimental framework and a learning platform for advanced programming concepts.

---

## 📄 License

MIT License
