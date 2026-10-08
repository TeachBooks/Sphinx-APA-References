import os
from dataclasses import dataclass, field

import sphinxcontrib.bibtex.plugin
from pybtex.richtext import HRef
from pybtex.style.formatting.apa import Style as APAStyle
from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset_file
from sphinxcontrib.bibtex.directives import BibliographyDirective
from sphinxcontrib.bibtex.style.referencing import BracketStyle
from sphinxcontrib.bibtex.style.referencing.author_year import (
    AuthorYearReferenceStyle,
)


class APABibliographyDirective(BibliographyDirective):
    """Same as BibliographyDirective, but forces style='myapa'."""

    def run(self):
        self.options.setdefault("style", "myapa")
        return super().run()


def bracket_style() -> BracketStyle:
    return BracketStyle(
        left="(",
        right=")",
    )


@dataclass
class MyReferenceStyle(AuthorYearReferenceStyle):
    bracket_parenthetical: BracketStyle = field(default_factory=bracket_style)
    bracket_textual: BracketStyle = field(default_factory=bracket_style)
    bracket_author: BracketStyle = field(default_factory=bracket_style)
    bracket_label: BracketStyle = field(default_factory=bracket_style)
    bracket_year: BracketStyle = field(default_factory=bracket_style)


class MyAPAStyle(APAStyle):
    """
    APA style with custom URL text.

    Use in BibTeX:

        url = {https://example.com}
        urldescription = {Project page}

    If urldescription is omitted, the title is used.
    """

    def format_url(self, e):
        url = e.fields.get("url")

        if not url:
            return None

        text = (
            e.fields.get("urldescription")
            or e.fields.get("title")
            or "Link"
        )

        return HRef(url, text)


def copy_stylesheet(app: Sphinx, exc: None) -> None:
    base_dir = os.path.dirname(__file__)
    style = os.path.join(base_dir, "assets", "apastyle.css")

    if app.builder.format == "html" and not exc:
        static_dir = os.path.join(app.builder.outdir, "_static")
        copy_asset_file(style, static_dir)


def override_config(app, config):
    config.bibtex_reference_style = "author_year_round"


def setup(app):
    app.setup_extension("sphinxcontrib.bibtex")

    sphinxcontrib.bibtex.plugin.register_plugin(
        "sphinxcontrib.bibtex.style.referencing",
        "author_year_round",
        MyReferenceStyle,
    )

    sphinxcontrib.bibtex.plugin.register_plugin(
        "pybtex.style.formatting",
        "myapa",
        MyAPAStyle,
    )

    app.add_directive("bibliography", APABibliographyDirective, override=True)

    app.connect("build-finished", copy_stylesheet)
    app.add_css_file("apastyle.css")
    app.connect("config-inited", override_config)
