Title: Cypher cheat sheet
Slug: cheatsheet
Save_as: cheatsheet.html
Url: cheatsheet.html
Eyebrow: A PRACTICAL REFERENCE
Heading: Cypher,
Heading_em: at a glance.
Intro: Common patterns for creating, querying, and updating a property graph in RiaGraph.

<section id="schema" markdown="1">

## Define a schema

Create node and relationship tables before adding data.

```
CREATE NODE TABLE Person(id INT64, name STRING, PRIMARY KEY(id));
CREATE REL TABLE Knows(FROM Person TO Person);
```

</section>

<section id="create" markdown="1">

## Create data

```
CREATE (:Person {id: 1, name: 'Ada'});
CREATE (:Person {id: 2, name: 'Lin'});
MATCH (a:Person {id: 1}), (b:Person {id: 2})
CREATE (a)-[:Knows]->(b);
```

</section>

<section id="match" markdown="1">

## Match patterns

```
MATCH (p:Person)
WHERE p.name = 'Ada'
RETURN p.id, p.name;

MATCH (a:Person)-[:Knows]->(b:Person)
RETURN a.name, b.name;
```

Use parameters such as `$name` for values supplied by your application.

</section>

<section id="shape" markdown="1">

## Shape results

```
MATCH (p:Person)
RETURN p.name ORDER BY p.name LIMIT 10;

MATCH (p:Person) RETURN count(*) AS people;

UNWIND [1, 2, 3] AS value RETURN value;
```

</section>

<section id="update" markdown="1">

## Update and delete

```
MATCH (p:Person {id: 1}) SET p.name = 'Ada Lovelace';
MATCH (p:Person {id: 2}) DETACH DELETE p;
```

`DETACH DELETE` removes incident relationships as well as the matched node.

</section>

<section id="scope" markdown="1">

## Namespaces & assertions

```
CREATE NAMESPACE team_a;
USE NAMESPACE team_a;
MATCH (p:Person) ASSERT count(*) > 0 AS 'Expected people'
RETURN p.name;
USE NAMESPACE ALL NAMESPACES;
```

See the [namespace](docs.html#namespaces) and [ASSERT](docs.html#assert) guides for scope and transaction semantics.

</section>
