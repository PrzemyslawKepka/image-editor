import os
import textwrap

import streamlit as st
from PIL import ImageDraw, ImageFont

from image_editor import fonts


class TextParams:

    FONT_DICT = fonts.FONT_DICT
    FONT_BOLD_DICT = fonts.FONT_BOLD_DICT
    FONT_ITALIC_DICT = fonts.FONT_ITALIC_DICT
    FONT_BOLD_ITALIC_DICT = fonts.FONT_BOLD_ITALIC_DICT
    FONTS_DIR = fonts.FONTS_DIR

    def __init__(self, key) -> None:
        self.key = key

        self.alignment = self.alignment_radio()
        self.font = self.font_selectbox()
        self.font_size = self.font_size_text_input()
        self.color = self.color_picker()
        self.bold = self.bold_checkbox()
        self.italic = self.italic_checkbox()
        self.upper_case = self.upper_case_checkbox()
        self.font_true_type = self.get_font_true_type(
            self.font, self.FONTS_DIR
        )

        # self.checkboxes()

    def alignment_radio(self):

        align_options = ["Left", "Center", "Right"]

        align_selection = st.radio(
            "Text Alignment",
            align_options,
            index=0,
            key=self.key,
            horizontal=True,
        )

        return align_selection

    def font_selectbox(self):

        font_selection = st.selectbox(
            "Font", fonts.FONT_DICT.keys(), index=0, key=self.key
        )

        return font_selection

    def font_size_text_input(self):

        font_size_selection = st.text_input(
            "Font size", value="20", key=self.key
        )

        if not font_size_selection.isnumeric():
            return st.error(
                "Please insert a number for a valid font size in pixels"
            )

        return int(font_size_selection)

    def bold_checkbox(self):

        bold_selection = st.checkbox("Bold", key=self.key)

        return bold_selection

    def italic_checkbox(self):

        italic_selection = st.checkbox("Italic", key=self.key)

        return italic_selection

    def upper_case_checkbox(self):

        upper_case_selection = st.checkbox("Upper Case", key=self.key)

        return upper_case_selection

    def color_picker(self):

        color_selection = st.color_picker(
            "Text color", "#FFFFFF", key=self.key
        )

        return color_selection

    def get_font_true_type(
        self, selected_font: str, font_dir: str = FONTS_DIR
    ):

        if self.bold and self.italic:
            font_name = self.FONT_BOLD_ITALIC_DICT[selected_font]
        elif self.bold:
            font_name = self.FONT_BOLD_DICT[selected_font]
        elif self.italic:
            font_name = self.FONT_ITALIC_DICT[selected_font]
        else:
            font_name = self.FONT_DICT[selected_font]

        font_full_path = os.path.join(font_dir, font_name)
        true_type = ImageFont.truetype(font_full_path, self.font_size)

        return true_type

    def place_text_on_image(self, image, text: str, position: str):

        if position not in ["top", "bottom"]:
            raise ValueError(
                "Text can be placed on top or at the bottom of the image only"
            )

        if self.upper_case:
            text = text.upper()

        WIDTH, HEIGHT = image.size

        left_anchor = {"top": "la", "bottom": "ld"}
        middle_anchor = {"top": "ma", "bottom": "md"}
        right_anchor = {"top": "ra", "bottom": "rd"}

        # text location
        if self.alignment == "Left":
            x_width = 15
            text_anchor = left_anchor[position]
        elif self.alignment == "Center":
            x_width = WIDTH / 2
            text_anchor = middle_anchor[position]
        elif self.alignment == "Right":
            x_width = WIDTH - 15
            text_anchor = right_anchor[position]

        # initalize drawing on inserted image
        draw = ImageDraw.Draw(image)
        # wrapping text
        line_length = (WIDTH / self.font_size) * 2.2
        text_wrap = textwrap.wrap(text, width=line_length)

        # assigning text position for botttom
        if len(text_wrap) == 1:
            bot_text_height_start = HEIGHT - 10
        else:
            bot_text_height_start = HEIGHT - len(text_wrap) * (0.07 * HEIGHT)

        starting_height = {"top": 10, "bottom": bot_text_height_start}

        current_h, pad = starting_height[position], 10
        for line in text_wrap:
            w, h = draw.textsize(line, font=self.font_true_type)
            draw.text(
                (x_width, current_h),
                line,
                fill=self.color,
                font=self.font_true_type,
                anchor=text_anchor,
            )
            current_h += h + pad

        return line_length
