import os
import sys

FONTS_DIR = "" if sys.platform == 'darwin' else r"C:\\WINDOWS\FONTS"

FONT_DICT = {
    "Arial": "ARIAL.TTF",
    "Times New Roman": "TIMES.TTF",
    "Comic Sans": "COMIC.TTF",
    "Calibri": "CALIBRIL.TTF",
    "Garamond": "GARA.TTF",
    "Cambria": "CAMBRIA.TTC",
    "Verdana": "VERDANA.TTF",
    "Franklin Gothic": "FRAMD.TTF",
}

FONT_BOLD_DICT = {
    "Arial": "ARIALBD.TTF",
    "Times New Roman": "TIMESBD.TTF",
    "Comic Sans": "COMICBD.TTF",
    "Calibri": "CALIBRIB.TTF",
    "Garamond": "GARABD.TTF",
    "Cambria": "CAMBRIAB.TTF",
    "Verdana": "VERDANAB.TTF",
    "Franklin Gothic": "FRAHV.TTF",
}

FONT_ITALIC_DICT = {
    "Arial": "ARIALI.TTF",
    "Times New Roman": "TIMESI.TTF",
    "Comic Sans": "COMICI.TTF",
    "Calibri": "CALIBRII.TTF",
    "Garamond": "GARAIT.TTF",
    "Cambria": "CAMBRIAI.TTF",
    "Verdana": "VERDANAI.TTF",
    "Franklin Gothic": "FRAMDIT.TTF",
}

FONT_BOLD_ITALIC_DICT = {
    "Arial": "ARIALBI.TTF",
    "Times New Roman": "TIMESBI.TTF",
    "Comic Sans": "COMICZ.TTF",
    "Calibri": "CALIBRIZ.TTF",
    "Garamond": "GARA.TTF",
    "Cambria": "CAMBRIAZ.TTF",
    "Verdana": "VERDANAZ.TTF",
    "Franklin Gothic": "FRAHVIT.TTF",
}



def get_font_full_name(
    selected_font: str, font_dict: dict = FONT_DICT, font_dir: str = FONTS_DIR
) -> str:
    """ """
    font_name = font_dict[selected_font]
    font_full_path = os.path.join(font_dir, font_name)

    return font_full_path
