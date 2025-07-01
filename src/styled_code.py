from manim import Code

class StyledCode(Code):
    """
    A class for displaying styled code snippets in the Dracula color theme. The
    only required argument is a path to a file (str). The default language is
    Python and can be overridden.
    """
    def __init__(self, *args, language="python", **kwargs):
        super().__init__(
            *args,
            language=language,
            insert_line_no=False,
            background_stroke_width=0,
            style=Code.styles_list[10],
            **kwargs
        )