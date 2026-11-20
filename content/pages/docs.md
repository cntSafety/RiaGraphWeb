Title: Documentation
Slug: docs
Save_as: docs.html
Url: docs.html
Eyebrow: RIAGRAPH DOCUMENTATION
Heading: Build with
Heading_em: connected data.
Intro: A practical introduction to the engine, its Cypher dialect, and the features that make RiaGraph distinct.

<section id="getting-started" markdown="1">

<p class="eyebrow">01 / START HERE</p>

## Getting started

RiaGraph is an embedded property graph database with a Cypher query interface. It is a fork of Ladybug, itself a fork of Kùzu, and prioritizes quality and reliability.

RiaGraph packages are not yet published to public package registries. Build from source or check the [release artifacts](https://github.com/cntSafety/RiaGraph/releases). The core library and shell can be built with:

```
git clone https://github.com/cntSafety/RiaGraph.git
cd RiaGraph
make release
```

For prerequisites and build options, see the [source build guide](https://github.com/cntSafety/RiaGraph/blob/main/CONTRIBUTING.md).

<div class="note" markdown="1">

**Database compatibility**

RiaGraph can read Ladybug and Kùzu databases, but after RiaGraph writes one, Ladybug can no longer open it. Keep a copy if you need to use the original engine.

</div>

</section>

<section id="model" markdown="1">

<p class="eyebrow">THE BASICS</p>

## The graph model

Nodes represent entities; relationships connect them. Both can carry properties. Tables define the types and properties used by the graph.

```
CREATE NODE TABLE Person(id INT64, name STRING, PRIMARY KEY(id));
CREATE REL TABLE Knows(FROM Person TO Person);
CREATE (:Person {id: 1, name: 'Ada'});
MATCH (p:Person) RETURN p.name;
```

For a compact reference to common queries, see the [Cypher cheat sheet](cheatsheet.html).

</section>

<section id="namespaces" markdown="1">

<p class="eyebrow">RIAGRAPH FEATURE</p>

## Namespaces

A namespace assigns each node and relationship to one logical group. Tables retain a shared schema; namespaces do not create separate databases or physical tables, and they are not an authorization boundary.

```
CREATE NAMESPACE team_a;
CREATE NODE TABLE Person IN ALL NAMESPACES (
  id INT64 LOCAL PRIMARY KEY, name STRING
);
CREATE (:Person {id: 1, name: 'Ada'}) IN team_a;
USE NAMESPACE team_a;
MATCH (p:Person) RETURN p.name;
```

### Selection and writes

Without a session selection, reads see all namespaces and writes default to the implicit global namespace. A singleton session selection scopes reads and supplies a default write target. Restore unrestricted reads with `USE NAMESPACE ALL NAMESPACES`. Inline selectors can narrow the scope of individual pattern elements; they cannot broaden a surrounding restriction.

### Keys and relationships

Primary keys are global to a table by default; a `LOCAL PRIMARY KEY` permits the same key in different namespaces. Relationships have their own namespace and can connect nodes in different namespaces. Each path element must be visible in the effective query scope.

### Lifecycle

`ALTER NAMESPACE team_a RENAME TO team_b` preserves identity and membership. Dropping a namespace is restrictive: remove its data and finite table memberships first. `namespace(element)` returns its name, or NULL for global membership.

Consult the [namespace specification](https://github.com/cntSafety/RiaGraph/blob/main/namespace.md) for selectors, moves, imports, transaction behavior, and supported integrations.

</section>

<section id="assert" markdown="1">

<p class="eyebrow">RIAGRAPH FEATURE</p>

## ASSERT

`ASSERT condition [AS 'message']` checks an expectation when a statement runs. It passes rows through unchanged; it does not filter rows or create a persistent schema constraint. Only TRUE succeeds: FALSE and NULL both fail.

```
ASSERT $amount > 0 AS 'Amount must be positive';
MATCH (p:Person)
ASSERT p.age IS NULL OR p.age >= 0 AS 'Invalid age'
RETURN p.name;
```

### Rows and aggregates

A non-aggregate condition is checked for each incoming row; zero rows means no per-row checks. A condition containing an aggregate is checked once over all incoming rows and then passes those rows through. On empty input, `count(*)` is zero. Aggregate conditions cannot mix row-dependent terms outside the aggregate.

```
MATCH (p:Person)
ASSERT count(*) > 0 AS 'Expected people'
RETURN p.name;
```

### Failure and transactions

A failed assertion raises an error prefixed `Assertion failed:`. The statement fails without returning rows. In auto-commit mode its transaction rolls back; in an explicit transaction, the whole transaction rolls back. After a write, use `WITH` before a following assertion.

See the [ASSERT specification](https://github.com/cntSafety/RiaGraph/blob/main/docs/assert.md) for full semantics and examples.

</section>

<section id="resources" markdown="1">

<p class="eyebrow">KEEP EXPLORING</p>

## Further reading

[Cypher cheat sheet](cheatsheet.html) · [RiaGraph source](https://github.com/cntSafety/RiaGraph) · [Ladybug documentation](https://docs.ladybugdb.com/)

Ladybug documentation describes the upstream project; check RiaGraph sources for differences and availability.

</section>
