import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from utils import *
from tqdm import tqdm


def part1(data):
    lines = [line.rstrip() for line in data]

    towel_line, _, *patterns = lines
    towels = towel_line.split(', ')

    # t = re.compile(r'^(r|wr|b|g|bwu|rb|gb|br)+$')
    t = re.compile(r'^(bubgb|buburr|rrrbrr|wubgbb|gggbw|wrr|rrbu|wbw|gubr|bruu|bub|rww|gguubguu|wwb|ugbrrw|burur|rgwwb|ugu|bbu|rug|uwwb|ggw|bgb|wbru|uuwrrrg|uuug|gur|urguw|ugru|urbwggg|bru|rgug|guu|g|grwr|rbuwb|bbr|wgbr|gubrw|rwrgb|rbw|buw|gbg|wrw|wrbrwg|gbrg|urgubgb|uwg|wggubgr|rgrub|bwuugrwr|gurgu|bur|wwgwwbu|bbbrgu|wbggru|wbuur|rgubg|rwww|br|wbr|wgrrggb|wwuubgg|gbu|uuu|rwbwb|uwugrgu|bugrgwwu|wgwbb|bgwwggr|wgbb|rubbr|ugbrbgub|urg|uruuwu|ggb|rgwwg|guw|uruur|wbgbr|wrbrbw|rrrggr|rgw|rgbgwbu|uru|bwgbgr|wwgg|ggbrgwr|rwgurruu|uwbr|rwur|uu|uugr|wg|wbuwuwr|bwbu|bgw|gbr|uugb|bubw|wrg|ugw|rwb|ww|rrggrb|ugww|bbw|wbb|ubbrwr|wrwr|uwbb|uwr|ugrg|ruu|gbw|gwurr|wwu|bbg|wbbw|rgww|wwbb|wuu|wwbwr|uugbwb|bbrw|wguwr|rugr|rgb|ubb|wrgr|grrrw|rrb|burwr|www|uub|wgbbwbb|rw|rbww|uwu|ugb|ugrw|ruuuubb|uwbbw|rgg|wuw|grbbw|gbru|rb|gwrwr|bgg|gwuug|rgu|bugrbb|rrrr|rubwu|bgbbu|wbgubbg|wwwuw|wwrb|uwgbg|rur|rbbu|rbr|rrrbwb|rgggugu|bgwuu|rbwgrbg|gbwwuuru|gg|wgru|grrub|ruurb|urgw|wuurgw|bbbgwww|gwb|gwwb|rbuw|ruuwwg|uuw|brggrw|wubgwu|ubw|ubgb|wbu|bubrrgww|wbg|brw|bggrrr|uwubw|wbbugu|bgu|rrbbww|ru|wbgbw|ggrwrugg|bwbwg|gbb|urwrrb|uuwuggr|gugw|urb|wbwbwrrb|grbwb|wwwgg|gwu|buwg|ug|gruwgub|gbgr|bgbbuwwr|rbb|ubuw|gww|b|wggg|wuwgub|gbbbbu|wgr|gwwbw|wurrb|gurw|rbur|brbrbrb|rgbu|ggbrb|rgggr|wwbrr|rrw|wur|urwwbgu|wubuwu|wwbu|bg|bbru|bgrguuuu|uwbru|bruburb|ugwrb|rbrwbgg|ugwru|ubu|ggwb|buu|burrbw|wr|rrrw|uuru|uurbbbb|wubrgb|gb|wbwwrug|rbu|bwrrww|uuwggrbb|gw|brg|uwrr|rbwb|rub|gggwr|gbbg|gwgb|rubggu|gbgu|wgb|brwurg|rrru|burg|rrbb|ubugub|uuwg|uwgu|grr|guwwww|gwg|grggg|ggwggbgb|wru|uurwwu|gbbbr|bbbb|brgu|buwgrr|grwgwu|buwbw|rru|gubwg|gub|wwr|gubgwg|buub|wrbbuw|urr|wu|bbgb|bw|uubb|ggrwrguw|wbgrrb|rrbuurb|ubwug|ggwww|bgrr|rgrgb|ur|brwuwbg|bubb|grruwwub|wurr|buuwbw|r|bu|brb|bgrurwb|bggrwg|rwu|wrwwbb|wbbugr|gggb|brbb|bwbuw|rwgurb|bgbuurg|buwb|uugu|ubwbggb|rruw|bggg|ubbrbw|grrr|bbruug|wgg|rwubgrgb|uubrruwr|wgbrb|bwb|gubrb|gwuurg|ggbr|wwg|ruww|bb|ggg|rgr|bww|gwburgwr|urw|gbbgb|rwg|bgr|ub|gwwug|bug|rr|rg|wrb|rrg|gggw|wwbbg|uwb|wwrw|bgbwrbg|ggrr|wug|wwuwww|bgrubw|gru|bubbgw|gwuww|gbggbb|gwbu|bgbugrb|wwrbr|ubbgr|brub|ugbwubug|uww|rugrb|rgbuu|w|wrrbw|rbg|rururwb|grbrwbwu|brurwb|ubgwrrr|ruw|bbrrrwu|ruwgw|rbrwu|rrgurg|ururbww|bbb|ugbb|bwu|wugb|uwrurwg|bwg|bggw|gug|bbgubw|uug|uur|grwwu|rrug|brgbbru|ggu|brwbu|grw|rwr|ubwbu|wbbb|wubrwg|gbgg|ugg|bbggub|gwr|ggub|wwgur|bwrw|rwbuw|wb|rbbr|urbb|gbggg|grg|ggwu|uwurgg|wbugug|ugr|rrbwr|gwuur|uwbgr|brrb|ubg|uuugwu|gr|bgbb|wggr|ggr|bwguw|ugubwbu|wgw|grb|wub|wbuww)+$')

    # for pattern in patterns:
    #     if re.match(t, pattern):
    #         print(f'{pattern}')

    return sum(1 for pattern in tqdm(patterns) if re.match(t, pattern))

    print(len(towels))
    print(len(patterns))



def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
