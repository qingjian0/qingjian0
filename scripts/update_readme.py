#!/usr/bin/env python
"""每日一言更新脚本 - 从国学经典中选取名言更新到 README"""
import json, random, datetime, re, os

QUOTES = [
    {"text": "道生一，一生二，二生三，三生万物", "source": "《道德经》"},
    {"text": "学而不思则罔，思而不学则殆", "source": "《论语·为政》"},
    {"text": "知之为知之，不知为不知，是知也", "source": "《论语·为政》"},
    {"text": "温故而知新，可以为师矣", "source": "《论语·为政》"},
    {"text": "三人行，必有我师焉", "source": "《论语·述而》"},
    {"text": "天行健，君子以自强不息", "source": "《周易·乾卦》"},
    {"text": "地势坤，君子以厚德载物", "source": "《周易·坤卦》"},
    {"text": "穷则变，变则通，通则久", "source": "《周易·系辞下》"},
    {"text": "知止而后有定，定而后能静，静而后能安", "source": "《大学》"},
    {"text": "物有本末，事有终始，知所先后，则近道矣", "source": "《大学》"},
    {"text": "博学之，审问之，慎思之，明辨之，笃行之", "source": "《中庸》"},
    {"text": "上善若水，水善利万物而不争", "source": "《道德经》"},
    {"text": "祸兮福之所倚，福兮祸之所伏", "source": "《道德经》"},
    {"text": "合抱之木，生于毫末；九层之台，起于累土", "source": "《道德经》"},
    {"text": "知己知彼，百战不殆", "source": "《孙子兵法》"},
    {"text": "工欲善其事，必先利其器", "source": "《论语·卫灵公》"},
    {"text": "不积跬步，无以至千里；不积小流，无以成江海", "source": "《荀子·劝学》"},
    {"text": "千里之行，始于足下", "source": "《道德经》"},
    {"text": "人法地，地法天，天法道，道法自然", "source": "《道德经》"},
    {"text": "大道至简", "source": "中国哲学经典"},
]

def main():
    today = datetime.date.today()
    idx = today.toordinal() % len(QUOTES)
    quote = QUOTES[idx]
    
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print(f"README.md not found in {os.getcwd()}")
        return
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    quote_block = f"> **「{quote['text']}」**\n> *—— {quote['source']}*"
    
    pattern = r"> \*\*「.*?」\*\*
> \*—— .*\*"
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, quote_block, content)
    else:
        content += f"

---

{quote_block}
"
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Updated quote: {quote['text']} — {quote['source']}")

if __name__ == "__main__":
    main()
