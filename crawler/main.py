from collect_issue_infos import fetch_issue_infos
from collect_articles_links import fetch_articles_links
from download_article import download, download_by
from read_article import read_by
from read_article_pdf import pdf_read_by
from read_article_ocr import ocr_read_by
import json

articles = [
  {
    "year": "2025",
    "volume": "48",
    "number_and_link": []
  },
  {
    "year": "2024",
    "volume": "47",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=332"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=333"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=334"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=335"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=337"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=338"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=339"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=340"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=341"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=342"
      }
    ]
  },
  {
    "year": "2023",
    "volume": "46",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=321"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=323"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=324"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=325"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=326"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=327"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=328"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=329"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=330"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=331"
      }
    ]
  },
  {
    "year": "2022",
    "volume": "45",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=311"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=312"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=313"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=314"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=315"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=316"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=317"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=318"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=319"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=320"
      }
    ]
  },
  {
    "year": "2021",
    "volume": "44",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=301"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=302"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=303"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=304"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=305"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=306"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=307"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=308"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=309"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=310"
      }
    ]
  },
  {
    "year": "2020",
    "volume": "43",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=286"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=287"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=288"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=293"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=294"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=295"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=296"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=297"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=298"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=300"
      }
    ]
  },
  {
    "year": "2019",
    "volume": "42",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=276"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=277"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=278"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=279"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=280"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=281"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=282"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=283"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=284"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=285"
      }
    ]
  },
  {
    "year": "2018",
    "volume": "41",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=265"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=266"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=267"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=268"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=269"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=270"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=271"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=273"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=274"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=275"
      }
    ]
  },
  {
    "year": "2017",
    "volume": "40",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=254"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=255"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=256"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=258"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=259"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=260"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=261"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=262"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=263"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=264"
      }
    ]
  },
  {
    "year": "2016",
    "volume": "39",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=244"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=245"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=246"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=247"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=248"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=249"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=250"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=251"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=252"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=253"
      }
    ]
  },
  {
    "year": "2015",
    "volume": "38",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=234"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=235"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=236"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=237"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=238"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=239"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=240"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=241"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=242"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=243"
      }
    ]
  },
  {
    "year": "2014",
    "volume": "37",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=9"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=1"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=2"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=3"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=5"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=8"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=227"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=231"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=232"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=233"
      }
    ]
  },
  {
    "year": "2013",
    "volume": "36",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=103"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=108"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=102"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=105"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=101"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=106"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=104"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=107"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=109"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=110"
      }
    ]
  },
  {
    "year": "2012",
    "volume": "35",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=133"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=137"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=135"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=139"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=134"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=138"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=136"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=140"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=141"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=143"
      },
      {
        "number": "11",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=142"
      }
    ]
  },
  {
    "year": "2011",
    "volume": "34",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=164"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=170"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=165"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=168"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=167"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=169"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=166"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=171"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=172"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=173"
      }
    ]
  },
  {
    "year": "2010",
    "volume": "33",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=196"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=201"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=194"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=200"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=195"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=199"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=197"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=198"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=202"
      },
      {
        "number": "10",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=203"
      }
    ]
  },
  {
    "year": "2009",
    "volume": "32",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=13"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=16"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=12"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=14"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=11"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=15"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=10"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=17"
      },
      {
        "number": "9",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=18"
      }
    ]
  },
  {
    "year": "2008",
    "volume": "31",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=36"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=40"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=39"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=41"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=38"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=42"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=37"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=43"
      }
    ]
  },
  {
    "year": "2007",
    "volume": "30",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=58"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=63"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=61"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=62"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=60"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=64"
      },
      {
        "number": "7",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=59"
      },
      {
        "number": "8",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=65"
      }
    ]
  },
  {
    "year": "2006",
    "volume": "29",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=84"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=82"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=81"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=83"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=85"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=86"
      }
    ]
  },
  {
    "year": "2005",
    "volume": "28",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=111"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=112"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=113"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=114"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=115"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=117"
      }
    ]
  },
  {
    "year": "2004",
    "volume": "27",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=144"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=146"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=145"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=147"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=148"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=149"
      }
    ]
  },
  {
    "year": "2003",
    "volume": "26",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=177"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=176"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=175"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=174"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=178"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=179"
      }
    ]
  },
  {
    "year": "2002",
    "volume": "25",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=205"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=209"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=204"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=210"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=208"
      }
    ]
  },
  {
    "year": "2001",
    "volume": "24",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=20"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=22"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=21"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=19"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=23"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=24"
      }
    ]
  },
  {
    "year": "2000",
    "volume": "23",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=44"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=45"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=47"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=46"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=48"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=49"
      }
    ]
  },
  {
    "year": "1999",
    "volume": "22",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=69"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=66"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=68"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=67"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=70"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=71"
      }
    ]
  },
  {
    "year": "1998",
    "volume": "21",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=89"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=87"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=90"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=88"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=91"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=92"
      }
    ]
  },
  {
    "year": "1997",
    "volume": "20",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=121"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=118"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=119"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=120"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=122"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=123"
      }
    ]
  },
  {
    "year": "1996",
    "volume": "19",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=151"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=152"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=150"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=153"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=154"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=155"
      }
    ]
  },
  {
    "year": "1995",
    "volume": "18",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=181"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=183"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=182"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=180"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=184"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=185"
      }
    ]
  },
  {
    "year": "1994",
    "volume": "17",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=212"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=213"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=214"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=215"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=216"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=217"
      }
    ]
  },
  {
    "year": "1993",
    "volume": "16",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=25"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=28"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=26"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=27"
      },
      {
        "number": "5",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=29"
      },
      {
        "number": "6",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=30"
      }
    ]
  },
  {
    "year": "1992",
    "volume": "15",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=50"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=53"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=52"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=51"
      }
    ]
  },
  {
    "year": "1991",
    "volume": "14",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=75"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=73"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=72"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=74"
      }
    ]
  },
  {
    "year": "1990",
    "volume": "13",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=93"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=96"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=94"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=95"
      }
    ]
  },
  {
    "year": "1989",
    "volume": "12",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=126"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=128"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=127"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=125"
      }
    ]
  },
  {
    "year": "1988",
    "volume": "11",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=156"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=158"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=159"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=157"
      }
    ]
  },
  {
    "year": "1987",
    "volume": "10",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=186"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=187"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=188"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=189"
      }
    ]
  },
  {
    "year": "1986",
    "volume": "9",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=219"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=218"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=220"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=221"
      }
    ]
  },
  {
    "year": "1985",
    "volume": "8",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=32"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=34"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=33"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=35"
      }
    ]
  },
  {
    "year": "1984",
    "volume": "7",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=55"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=57"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=56"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=54"
      }
    ]
  },
  {
    "year": "1983",
    "volume": "6",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=80"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=79"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=78"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=77"
      }
    ]
  },
  {
    "year": "1982",
    "volume": "5",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=97"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=100"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=99"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=98"
      }
    ]
  },
  {
    "year": "1981",
    "volume": "4",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=129"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=130"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=131"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=132"
      }
    ]
  },
  {
    "year": "1980",
    "volume": "3",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=160"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=163"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=161"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=162"
      }
    ]
  },
  {
    "year": "1979",
    "volume": "2",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=191"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=190"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=193"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=192"
      }
    ]
  },
  {
    "year": "1978",
    "volume": "1",
    "number_and_link": [
      {
        "number": "1",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=225"
      },
      {
        "number": "2",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=222"
      },
      {
        "number": "3",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=223"
      },
      {
        "number": "4",
        "link": "https://quimicanova.sbq.org.br/default.asp?ed=224"
      }
    ]
  }
]


def main():
    #issue_infos = fetch_issue_infos()
    #articles_links = fetch_articles_links(issue_infos)
    #download(articles_links)
    ##download_by(2024,4,"https://quimicanova.sbq.org.br/audiencia_pdf.asp?aid2=9655&nomeArquivo=v47n4a11.pdf")
    ##download_by(1978,1,"https://quimicanova.sbq.org.br/audiencia_pdf.asp?aid2=5640&nomeArquivo=Vol1No4_45_v01_n4_(13)-indice_assuntos.pdf")
    #read_by(articles)
    ##pdf_read_by("./articles/2024/4/v47n4a11.pdf")
    ##ocr_read_by("./articles/1978/1/Vol1No4_45_v01_n4_(13)-indice_assuntos.pdf")

    #print(json.dumps(articles_links, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
