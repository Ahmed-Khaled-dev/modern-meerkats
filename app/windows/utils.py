from blessed import Terminal
from pydantic import BaseModel

from app import constants as const


class BorderConfig(BaseModel):
    """Border configuration contianer used for rendering borders"""

    top_left = "┌"
    top_right = "┐"
    bottom_left = "└"
    bottom_right = "┘"
    top = "─"
    left = "│"
    bottom = "─"
    right = "│"


def render_border(
    start_x: int,
    start_y: int,
    height: int,
    width: int,
    title: str,
    term: Terminal,
    cfg: BorderConfig = BorderConfig(),
) -> str:
    """Render border around a box"""
    _top = term.center(title, width=width, fillchar=cfg.top)
    top = term.move_xy(start_x, start_y) + f"{cfg.top_left}{_top}{cfg.top_right}"
    bot = (
        term.move_xy(start_x, start_y + height + 1)
        + f"{cfg.bottom_left}{cfg.bottom * width}{cfg.bottom_right}"
    )
    left = ""
    right = ""
    for i in range(0, height):
        left += term.move_xy(start_x, start_y + i + 1) + cfg.left
        right += term.move_xy(start_x + width + 1, start_y + i + 1) + cfg.right
    border = top + bot + left + right
    return term.tomato(term.bold(border))


def render_cmdhelp_border(term: Terminal) -> str:
    """Render border around cmdhelp box"""
    return render_border(
        start_x=const.CMDHELP_X,
        start_y=const.CMDHELP_Y,
        height=const.CMDHELP_HEIGHT,
        width=const.CMDHELP_WIDTH,
        title=" Help ",
        term=term,
    )


def render_cmdlist_border(term: Terminal) -> str:
    """Render border around cmdlist box"""
    return render_border(
        start_x=const.CMDLIST_X,
        start_y=const.CMDLIST_Y,
        height=const.CMDLIST_HEIGHT,
        width=const.CMDLIST_WIDTH,
        title=" Plan ",
        term=term,
    )


def render_user_input_border(term: Terminal) -> str:
    """Render border around userinput box"""
    return render_border(
        start_x=const.INPUT_X,
        start_y=const.INPUT_Y,
        height=const.INPUT_HEIGHT,
        width=const.INPUT_WIDTH,
        title=" Input ",
        term=term,
    )


def render_map_border(term: Terminal, title: str) -> str:
    """Render border around map"""
    cfg = BorderConfig(left="├", right="┤", top="┬", bottom="┴")
    return render_border(
        start_x=const.MAP_X,
        start_y=const.MAP_Y,
        height=const.MAP_HEIGHT,
        width=const.MAP_WIDTH,
        title=f" {title} ",
        term=term,
        cfg=cfg,
    )


def render_positioned_content(
    pos_x: int, pos_y: int, lines: list[str], term: Terminal
) -> str:
    """Render content at position"""
    res = ""
    for i, l in enumerate(lines):
        res += term.move_xy(pos_x, pos_y + i) + l
    return res


def clear_window(
    pos_x: int, pos_y: int, width: int, height: int, term: Terminal
) -> str:
    """Clear content area"""
    res = ""
    for i in range(0, height):
        res += term.move_xy(pos_x, pos_y + i) + " " * width
    return res


def clear_user_input_window(term: Terminal) -> str:
    """Clear user input area"""
    return clear_window(
        pos_x=const.INPUT_X + 1,
        pos_y=const.INPUT_Y + 1,
        width=const.INPUT_WIDTH,
        height=const.INPUT_HEIGHT,
        term=term,
    )


def clear_cmdhelp_window(term: Terminal) -> str:
    """Clear cmdhelp area"""
    return clear_window(
        pos_x=const.CMDHELP_X + 1,
        pos_y=const.CMDHELP_Y + 1,
        width=const.CMDHELP_WIDTH,
        height=const.CMDHELP_HEIGHT,
        term=term,
    )


def clear_cmdlist_window(term: Terminal) -> str:
    """Clear cmdlist area"""
    return clear_window(
        pos_x=const.CMDLIST_X + 1,
        pos_y=const.CMDLIST_Y + 1,
        width=const.CMDLIST_WIDTH,
        height=const.CMDLIST_HEIGHT,
        term=term,
    )


def clear_map_window(term: Terminal) -> str:
    """Clear map area"""
    return clear_window(
        pos_x=const.MAP_X + 1,
        pos_y=const.MAP_Y + 1,
        width=const.MAP_WIDTH,
        height=const.MAP_HEIGHT,
        term=term,
    )
