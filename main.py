from script.parser import parse_it
from script.export_suzuchan import export_suzuchan
from script.Extract_10 import extract_level_10
from script.Extract_9 import extract_level_9


def main():
    # url = 'file:///' + os.path.abspath('.') + '/wikipage.html'
    url_o = 'https://w.atwiki.jp/jubeat/pages/2334.html'
    parse_it(url_o)
    url_n = 'https://w.atwiki.jp/jubeat/pages/2333.html'
    parse_it(url_n, append=True)
    export_suzuchan()
    extract_level_10()
    extract_level_9()


if __name__ == "__main__":
    main()
