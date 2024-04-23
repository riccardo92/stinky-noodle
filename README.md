# Stinky noodle

Stiny noodle is a Python OpenAPI spec linter that can read `spectral` (https://github.com/stoplightio/spectral) rule sets. This project is very early stage and not stable at all. The main reason for creating this project is to make it much easier to use with Python projects.

## Getting started

Run `pip install stinky-noodle` and then run `noodle <path-to-spec-file>` to start linting.

## Rule sets

Stinky noodle fully relies on rule sets as defined in the `spectral` docs and does not have its own syntax:
https://meta.stoplight.io/docs/spectral/e5b9616d6d50c-rulesets

You can use a rule set by adding the following argument:

```bash
noodle -s <path-to-ruleset>[ -d <dir-containing-custom-module>][ -m <cusom-module-name>] <path-to-spec-file>
```

## Caveats

Spectral linting rules can make use of custom functions written in js. There is currently no way of automatically converting those functions in python built into Stink noodle. Functions always have to be manually converted. See the `Functions` section on how to do that.
