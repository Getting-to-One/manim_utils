import os
from manim import VGroup, Text, LIGHT_GRAY, UP, DOWN
from styled_code import StyledCode

class StyledCodeWindow(VGroup):
    """
    A mobject that combines a StyledCode block with a window and text title,
    replicating the appearance of a titled window in an OS.
    
    Inherits from manim's VGroup class.

    Args:
        file_path (str): The path to the code file to be displayed.
        window_title_text (str | None, optional): A custom title for the
                                                  window. If None, the basename
                                                  of the file_path is used.
                                                  Defaults to None.
        **kwargs: Additional keyword arguments to be passed to the VGroup.
    """
    def __init__(
        self,
        file_path: str,
        window_title_text: str | None = None,
        **kwargs
    ):
        super().__init__(**kwargs)

        code = StyledCode(
            file_path,
            background="window"
        )
        
        if window_title_text is None:
            window_title_text = os.path.basename(file_path)

        window_title = Text(
            window_title_text,
            font="Inter Variable",
            font_size=22,
            color=LIGHT_GRAY
        )

        window_title.align_to(code, UP).shift(DOWN * 0.15)
        self.add(code, window_title)