from manim import Code

class StyledCode(Code):
    """
    A class for displaying styled code snippets in the Dracula color theme.
    Inherits from manim's Code class.
    The only required argument is a path to a file (str).
    """
    def __init__(
        self, *args, 
        language="python",
        has_line_numbers=False,
        background_config={"stroke_width": 0},
        **kwargs
    ):
        super().__init__(
            *args,
            language=language,
            add_line_numbers=has_line_numbers,
            paragraph_config={"font": "Source Code Pro"}, # cannot be a font with ligatures
            formatter_style="dracula",
            background_config=background_config,
            **kwargs
        )