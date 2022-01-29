from pathlib import Path

from nonebot import get_driver
from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    wordcloud_width: int = 1920
    wordcloud_height: int = 1200
    wordcloud_background_color: str = "black"
    wordcloud_font_path: str = str(Path(__file__).parent / "SimHei.ttf")
    wordcloud_stopwords_path: Path = Path(__file__).parent / "stopwords.txt"


global_config = get_driver().config
plugin_config = Config.parse_obj(global_config)