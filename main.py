from parser import parse_it
from export_suzuchan import export_suzuchan


def main():
    # url = 'file:///' + os.path.abspath('.') + '/wikipage.html'
    url_o = 'https://w.atwiki.jp/jubeat/pages/2224.html'
    parse_it(url_o)
    url_n = 'https://w.atwiki.jp/jubeat/pages/2223.html'
    parse_it(url_n, append=True)
    export_suzuchan().to_csv("jubeat_list_per_chart.csv")


if __name__ == "__main__":
    main()
