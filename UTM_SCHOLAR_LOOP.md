# UTM Scholar Loop

A non-guarantee academic progress engine: it cannot guarantee a career outcome, but it makes scholarly progress auditable.

## State machine

READ -> NOTE -> QUESTION -> ARGUE -> WRITE -> FEEDBACK -> REVISE -> ARCHIVE

A state advances only when an artifact exists.

## Daily invariant

At least one small artifact:
- source note
- quotation + citation locator
- philosophical question
- premise/conclusion argument
- objection/reply
- paragraph draft
- revision

## Research gate

A metaphysical or philosophical claim may be promoted from IDEA to RESEARCH_CLAIM only when it is linked to at least one external source and has survived at least one objection check.

## Chakra interpretation

Reading = intake; argument = transformation; writing = expression; feedback = correction; archive = continuity.

## API

GET /health
GET /state
POST /advance with JSON {"stage":"READ","artifact":"..."}

This staged branch is intended for a separate Railway service and does not modify the existing UTM-Universe services.
