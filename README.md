# National Informatics Olympiad Problem OOP Solution (Duck Race)

### Layered Architecture Solution for an Algorithmic Optimization Problem

---

## Problem Overview

This application solves the **“Duck race”** problem from the National Informatics Olympiad (Romania).

A prince organizes a swimming race using a selection of ducks, each characterized by:

* **Speed** (meters/second)
* **Resistance**

There are multiple swimming lanes, each with a **beacon placed at increasing distances** from the start.

### 🎯 Goal

Select and assign ducks to lanes such that:

1. Each duck swims to its assigned beacon and returns.
2. Ducks must respect a **non-decreasing resistance constraint**:

   * A duck on a farther lane must have **equal or higher resistance** than the previous.
3. The race finishes when the **slowest duck returns**.

The objective is to **minimize the total race duration**.

---

## 💡 Key Insight

The total race time is determined by the **maximum individual completion time**:

$$
T = \max\left(\frac{2 \cdot d_i}{v_i}\right)
$$

*(where (d_i) = distance and (v_i) = speed of duck (i))*

This transforms the problem into:

* Selecting **M ducks from N**
* Assigning them optimally to lanes
* Respecting resistance ordering
* Minimizing the **maximum time**

---

## Solution Strategy

### 1. Sorting & Preprocessing

* Ducks are sorted or filtered based on **resistance constraints**
* Lanes are naturally sorted by distance

### 2. Optimization Approach

* Use **binary search on time**:

  * Guess a maximum allowed time (T)
  * Check if it's possible to assign ducks under this constraint

### 3. Feasibility Check

For a fixed (T), verify:

$$
\frac{2 \cdot d}{v} \le T
$$

* Ensure there are enough valid ducks
* Maintain **monotonic resistance ordering**

### 4. Greedy Assignment

* Assign ducks to lanes in order
* Always pick the **fastest valid duck** that satisfies resistance rules

---

## Application Architecture

The project follows a **Layered OOP Architecture**, ensuring separation of concerns and maintainability.

### 🔹 Layers

#### 1. **Presentation Layer**

* Handles input/output
* Reads from file (`natatie.in`)
* Writes result (`natatie.out`)

#### 2. **Application Layer**

* Coordinates the solving process
* Calls services and manages flow

#### 3. **Domain Layer**

* Core business logic:

  * Duck entity
  * Lane constraints
  * Time calculation

* Implements:

  * Feasibility checking
  * Optimization logic

#### 4. **Infrastructure Layer**

* File handling
* Data parsing
* Utility helpers

---

## 🧩 Core Classes

### 🦆 `Duck`

* Properties: `speed`, `resistance`
* Represents a participant

### 🛣️ `Lane`

* Property: `distance`
* Represents a swimming track

### ⚙️ `RaceSolver`

* Main algorithm logic
* Implements:

  * Binary search
  * Feasibility checks

### 📂 `FileManager`

* Handles input/output operations

---

## 🔄 Execution Flow

1. Read input data
2. Initialize domain objects
3. Run optimization algorithm
4. Compute minimal race time
5. Output result

---

## 📈 Complexity

* **Time Complexity:**
  $$O(N \log N + N \log )$$

* **Space Complexity:**
  $$O(N)$$

Efficient enough for constraints up to **3000 ducks**

---

## Example

**Input:**

```
3 2
4 5 3
5 2 2
3 7
```

**Output:**

```
2.8
```

---

## ✨ Highlights

* ✅ Clean separation using layered architecture
* ✅ Efficient optimization with binary search
* ✅ Greedy + constraint-based assignment
* ✅ Scalable and maintainable design

---

## 🚀 Possible Improvements

* Add **unit tests** for feasibility checks
* Extend to **GUI visualization** of race simulation
* Improve performance with advanced data structures

---

## Conclusion

This project demonstrates how a **complex combinatorial optimization problem** can be elegantly solved using:

* Algorithmic techniques (binary search + greedy)
* Clean software design (OOP + layered architecture)

It balances **performance, clarity, and extensibility** — making it both competitive-programming ready and production-structured.

---

💬 *“Fast ducks win races, but smart architecture wins projects.”*

