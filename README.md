# Sphinx APA References

## Introduction

This Sphinx extension allows you to have APA formatting of references in your book.

> [!NOTE]
> This extension only modifies the formatting of references to comply with APA style. It does not handle citation management or reference generation; you will need to manage your references separately.

## What does it do?

This extension modifies the way references are formatted in Sphinx-generated documentation to comply with APA (American Psychological Association) style guidelines _for references_. It ensures that citations and bibliographies are presented in a manner consistent with APA standards.

This entails **forcing** the following APA-specific formatting rules:

- Author names are formatted as "Last, F. M." (e.g., "Smith, J. D.").
- Author-year formatting for in-text citations (e.g., "(Smith, 2020)").
- Proper indentation and spacing for reference entries.
- Alphabetical ordering of references by the last name of the first author.

## Installation

To use this extension, follow these steps:

**Step 1: Install the Package**

Install the module `sphinx-apa-references` package using `pip`:
```
pip install sphinx-apa-references
```
    
**Step 2: Add to `requirements.txt`**

Make sure that the package is included in your project's `requirements.txt` to track the dependency:
```
sphinx-apa-references
```

**Step 3: Enable in `_config.yml` or `conf.py`**

In your `_config.yml` file, add the extension to the list of Sphinx extra extensions (**important**: underscore, not dash this time):
```
sphinx: 
    extra_extensions:
        .
        .
        .
        - sphinx_apa_references
        .
        .
        .
```

or in your `conf.py` file, add the extension to the `extensions` list:
```python
extensions = [
    .
    .
    .
    "sphinx_apa_references",
    .
    .
    .
]
```

## Configuration

No additional configuration is possible. The extension automatically applies APA formatting to all references in your Sphinx documentation.

This extensions enforces the following settings, overriding any user-defined settings in `_config.yml`/`conf.py`:

- `bibtex_default_style = "myapastyle"`
- `bibtex_reference_style = "author_year_round"`

Furthermore, the `bibliography` directive is adapted to always use the value `apa` for the `style` option if the user does not provide a value for the `style` option.

## Examples and details

To see examples of usage visit [this page in the TeachBooks manual](https://teachbooks.io/manual/features/apa.html).