from manim import Code

class StyledCode(Code):
    def __init__(self, *args, language="python", **kwargs):
        super().__init__(
            *args,
            language=language,
            insert_line_no=False,
            background_stroke_width=0,
            style=Code.styles_list[10],
            **kwargs
        )