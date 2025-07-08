from manim import Code

class StyledCode(Code):
    """
    A class for displaying styled code snippets in the Dracula color theme. The
    only required argument is a path to a file (str).
    
    ### Default parameters (can be overriden):
    language="python"\n
    background_stroke_width=0
    """
    def __init__(
        self, *args, 
        language="python",
        background_stroke_width=0,
        **kwargs
    ):
        super().__init__(
            *args,
            language=language,
            insert_line_no=False,
            background_stroke_width=background_stroke_width,
            style=Code.styles_list[10],
            **kwargs
        )