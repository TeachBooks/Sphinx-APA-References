import sphinxcontrib.bibtex.plugin

from dataclasses import dataclass, field
from .pybtexapastyle.formatting.apa import APAStyle
from .pybtexapastyle.labels.apa import LabelStyle as APALabelStyle
from pybtex.plugin import register_plugin
from sphinxcontrib.bibtex.style.referencing import BracketStyle
from sphinxcontrib.bibtex.style.referencing.author_year import AuthorYearReferenceStyle

class MyAPALabelStyle(APALabelStyle):
    def format_label(self, entry):
        return APALabelStyle.format_label(self, entry)

class MyAPAStyle(APAStyle):
    default_label_style = 'apa'

def bracket_style() -> BracketStyle:
    return BracketStyle(
        left='(',
        right=')',
    )

@dataclass
class MyReferenceStyle(AuthorYearReferenceStyle):
    bracket_parenthetical: BracketStyle = field(default_factory=bracket_style)
    bracket_textual: BracketStyle = field(default_factory=bracket_style)
    bracket_author: BracketStyle = field(default_factory=bracket_style)
    bracket_label: BracketStyle = field(default_factory=bracket_style)
    bracket_year: BracketStyle = field(default_factory=bracket_style)

def setup(app):
    register_plugin('pybtex.style.labels', 'myapa', MyAPALabelStyle)
    register_plugin('pybtex.style.formatting', 'myapastyle', MyAPAStyle)
    sphinxcontrib.bibtex.plugin.register_plugin('sphinxcontrib.bibtex.style.referencing','author_year_round', MyReferenceStyle)
