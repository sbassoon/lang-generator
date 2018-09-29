import random as r
import math as m

# NEXT STEPS
#
# Consonant orthography styles
# Vowel orthography styles
#
# hard clusters based on sonority sequencing principle: https://en.wikipedia.org/wiki/Sonority_Sequencing_Principle
#   instead of indexing

vowel_five_standard = ["a", "e", "i", "o", "u"]
vowel_three_aiu = ["a", "i", "u"]
vowel_three_eou = ["e", "o", "u"]
vowel_five_aiuai = vowel_three_aiu + ["A", "I"]
vowel_extra_aou = vowel_five_standard + ["A", "O", "U"]
vowel_extra_aei = vowel_five_standard + ["A", "E", "I"]
vowel_extra_u = vowel_five_standard + ["U"]
vowel_extra_five = vowel_five_standard + ["A", "E", "I", "O", "U"]

consonant_unvstops = ["p", "t", "k", "q", "ʔ"]
consonant_vstops = ["g", "d", "b"]
consonant_stops_full = consonant_unvstops + consonant_vstops

consonant_unvsibilants = ["s", "ʃ"]
consonant_vsibilants = ["z", "ʒ"]
consonant_sibilants_full = consonant_unvsibilants + consonant_vsibilants

consonant_unvfricatives = ["f", "θ", "x"]
consonant_vfricatives = ["v", "ð", ]
consonant_fricatives_full = consonant_unvfricatives + consonant_vfricatives

consonant_unvaffricatives = ["ʦ", "ʧ"]
consonant_vaffricatives = ["ʣ", "ʤ"]
consonant_affricatives_full = consonant_unvaffricatives + consonant_vaffricatives

consonant_nasals_full = ["m", "n", "ŋ"]
consonant_liquids_full = ["r", "l", "w", "j"]

consonant_fricatives_and_sibilants_full = consonant_sibilants_full + consonant_fricatives_full
consonant_full = consonant_stops_full + consonant_fricatives_and_sibilants_full + consonant_affricatives_full + consonant_nasals_full + consonant_liquids_full

vowlist = vowel_three_eou
conlist = consonant_stops_full
siblist = consonant_fricatives_and_sibilants_full
liqlist = consonant_liquids_full
finlist = consonant_nasals_full + consonant_fricatives_and_sibilants_full + consonant_stops_full

restricted_pairs = ["tq", "ʔx", "rl", "lr", "tn", "ʔn", "pb", "pn",
                    "px", "ʔt", "pd", "gq", "pb", "qv", "gt", "gb",
                    "tk", "pv", "pm", "dŋ", "pj", "ʔw", "dn", "dʒ",
                    "qg", "ʔð", "dʃ", "pz", "pʔ", "tx", "qŋ", "dm",
                    "ʔʃ", "pl", "ʔb", "qt", "pw", "qð", "gf", "pr",
                    "pg", "pŋ", "pʒ", "ʔf", "qz", "kr", "pg", "bp",
                    "zp"]

phonot = "TCVL"
check_doubles = True
check_hard_clusters = True


def main():
    sylList = generateSyllables(conlist, vowlist, siblist, liqlist, finlist, phonot, 20, 4, 0.5)
    print(sylList)


def generateSyllables(consonants: list, vowels: list, sibilants: list, liquids: list, finals: list, phonotype: str,
                      number_to_make: int,
                      simple_consonant_factor: int,
                      optional_factor: float) -> list:
    syllableList = []
    i = 0
    while i < number_to_make:
        syllable = ""
        j = 0
        for p in phonotype:
            if j != len(phonotype):
                if p == "C":
                    # consonants
                    weighted_choice_factor = int(m.floor(m.pow(r.random(), simple_consonant_factor) * len(consonants)))
                    consonant = consonants[weighted_choice_factor]
                    if (len(syllable) > 0):
                        if ((syllable[-1] + consonant) in restricted_pairs) and (check_hard_clusters is True):
                            while (syllable[-1] + consonant in restricted_pairs):
                                consonant = consonants[weighted_choice_factor]
                            syllable = syllable + consonant
                            j += 1
                        elif (consonant == syllable[-1]) and (check_doubles is True):
                            while (consonant == syllable[-1]):
                                consonant = consonants[weighted_choice_factor]
                            syllable = syllable + consonant
                            j += 1
                        else:
                            syllable = syllable + consonant
                            j += 1
                    else:
                        syllable = syllable + consonant
                        j += 1
                    if j == len(phonotype):
                        syllableList.append(syllable)
                elif p == "D":
                    # consonants at probability
                    if r.random() < optional_factor:
                        weighted_choice_factor = int(
                            m.floor(m.pow(r.random(), simple_consonant_factor) * len(consonants)))
                        consonant = consonants[weighted_choice_factor]
                        if (len(syllable) > 0):
                            if ((syllable[-1] + consonant) in restricted_pairs) and (check_hard_clusters is True):
                                while (syllable[-1] + consonant in restricted_pairs):
                                    consonant = consonants[weighted_choice_factor]
                                syllable = syllable + consonant
                                j += 1
                            elif (consonant == syllable[-1]) and (check_doubles is True):
                                while (consonant == syllable[-1]):
                                    consonant = consonants[weighted_choice_factor]
                                syllable = syllable + consonant
                                j += 1
                            else:
                                syllable = syllable + consonant
                                j += 1
                        else:
                            syllable = syllable + consonant
                            j += 1
                    else:
                        j += 1
                    if j == len(phonotype):
                        syllableList.append(syllable)
                elif p == "V":
                    # vowels
                    vowel = vowels[r.randint(0, len(vowels) - 1)]
                    if (len(syllable) > 0):
                        if ((syllable[-1] + vowel) in restricted_pairs) and (check_hard_clusters is True):
                            while (syllable[-1] + vowel in restricted_pairs):
                                vowel = vowels[r.randint(0, len(vowels) - 1)]
                            syllable = syllable + vowel
                            j += 1
                        elif (vowel == syllable[-1]) and (check_doubles is True):
                            while (vowel == syllable[-1]):
                                vowel = vowels[r.randint(0, len(vowels) - 1)]
                            syllable = syllable + vowel
                            j += 1
                        else:
                            syllable = syllable + vowel
                            j += 1
                    else:
                        syllable = syllable + vowel
                        j += 1
                    if j == len(phonotype):
                        syllableList.append(syllable)
                elif p == "W":
                    # vowels at probability
                    if r.random() < optional_factor:
                        vowel = vowels[r.randint(0, len(vowels) - 1)]
                        if (len(syllable) > 0):
                            if ((syllable[-1] + vowel) in restricted_pairs) and (check_hard_clusters is True):
                                while (syllable[-1] + vowel in restricted_pairs):
                                    vowel = vowels[r.randint(0, len(vowels) - 1)]
                                syllable = syllable + vowel
                                j += 1
                            elif (vowel == syllable[-1]) and (check_doubles is True):
                                while (vowel == syllable[-1]):
                                    vowel = vowels[r.randint(0, len(vowels) - 1)]
                                syllable = syllable + vowel
                                j += 1
                            else:
                                syllable = syllable + vowel
                                j += 1
                        else:
                            syllable = syllable + vowel
                            j += 1
                    else:
                        j += 1
                    if j == len(phonotype):
                        syllableList.append(syllable)
                elif p == "S":
                    # sibilants
                    sibilant = sibilants[r.randint(0, len(sibilants) - 1)]
                    if (len(syllable) > 0):
                        if ((syllable[-1] + sibilant) in restricted_pairs) and (check_hard_clusters is True):
                            while (syllable[-1] + sibilant in restricted_pairs):
                                sibilant = sibilants[r.randint(0, len(sibilants) - 1)]
                            syllable = syllable + sibilant
                            j += 1
                        elif (sibilant == syllable[-1]) and (check_doubles is True):
                            while (sibilant == syllable[-1]):
                                sibilant = sibilants[r.randint(0, len(sibilants) - 1)]
                            syllable = syllable + sibilant
                            j += 1
                        else:
                            syllable = syllable + sibilant
                            j += 1
                    else:
                        syllable = syllable + sibilant
                        j += 1
                    if j == len(phonotype):
                        syllableList.append(syllable)
                elif p == "T":
                    # sibilants at probability
                    if r.random() < optional_factor:
                        sibilant = sibilants[r.randint(0, len(sibilants) - 1)]
                        if (len(syllable) > 0):
                            if ((syllable[-1] + sibilant) in restricted_pairs) and (check_hard_clusters is True):
                                while (syllable[-1] + sibilant in restricted_pairs):
                                    sibilant = sibilants[r.randint(0, len(sibilants) - 1)]
                                syllable = syllable + sibilant
                                j += 1
                            elif (sibilant == syllable[-1]) and (check_doubles is True):
                                while (sibilant == syllable[-1]):
                                    sibilant = sibilants[r.randint(0, len(sibilants) - 1)]
                                syllable = syllable + sibilant
                                j += 1
                            else:
                                syllable = syllable + sibilant
                                j += 1
                        else:
                            syllable = syllable + sibilant
                            j += 1
                    else:
                        j += 1
                    if j == len(phonotype):
                        syllableList.append(syllable)
                elif p == "L":
                    # liquids
                    liquid = liquids[r.randint(0, len(liquids) - 1)]
                    if (len(syllable) > 0):
                        if ((syllable[-1] + liquid) in restricted_pairs) and (check_hard_clusters is True):
                            while (syllable[-1] + liquid in restricted_pairs):
                                liquid = liquids[r.randint(0, len(liquids) - 1)]
                            syllable = syllable + liquid
                            j += 1
                        elif (liquid == syllable[-1]) and (check_doubles is True):
                            while (liquid == syllable[-1]):
                                liquid = liquids[r.randint(0, len(liquids) - 1)]
                            syllable = syllable + liquid
                            j += 1
                        else:
                            syllable = syllable + liquid
                            j += 1
                    else:
                        syllable = syllable + liquid
                        j += 1
                    if j == len(phonotype):
                        syllableList.append(syllable)
                elif p == "M":
                    # liquids at probability
                    if r.random() < optional_factor:
                        liquid = liquids[r.randint(0, len(liquids) - 1)]
                        if (len(syllable) > 0):
                            if ((syllable[-1] + liquid) in restricted_pairs) and (check_hard_clusters is True):
                                while (syllable[-1] + liquid in restricted_pairs):
                                    liquid = liquids[r.randint(0, len(liquids) - 1)]
                                syllable = syllable + liquid
                                j += 1
                            elif (liquid == syllable[-1]) and (check_doubles is True):
                                while (liquid == syllable[-1]):
                                    liquid = liquids[r.randint(0, len(liquids) - 1)]
                                syllable = syllable + liquid
                                j += 1
                            else:
                                syllable = syllable + liquid
                                j += 1
                        else:
                            syllable = syllable + liquid
                            j += 1
                    else:
                        j += 1
                    if j == len(phonotype):
                        syllableList.append(syllable)
                elif p == "F":
                    # finals
                    final = finals[r.randint(0, len(finals) - 1)]
                    if (len(syllable) > 0):
                        if ((syllable[-1] + final) in restricted_pairs) and (check_hard_clusters is True):
                            while (syllable[-1] + final in restricted_pairs):
                                final = finals[r.randint(0, len(finals) - 1)]
                            syllable = syllable + final
                            j += 1
                        elif (final == syllable[-1]) and (check_doubles is True):
                            while (final == syllable[-1]):
                                final = finals[r.randint(0, len(finals) - 1)]
                            syllable = syllable + final
                            j += 1
                        else:
                            syllable = syllable + final
                            j += 1
                    else:
                        syllable = syllable + final
                        j += 1
                    if j == len(phonotype):
                        syllableList.append(syllable)
                elif p == "G":
                    # finals at probability
                    if r.random() < optional_factor:
                        final = finals[r.randint(0, len(finals) - 1)]
                        if (len(syllable) > 0):
                            if ((syllable[-1] + final) in restricted_pairs) and (check_hard_clusters is True):
                                while (syllable[-1] + final in restricted_pairs):
                                    final = finals[r.randint(0, len(finals) - 1)]
                                syllable = syllable + final
                                j += 1
                            elif (final == syllable[-1]) and (check_doubles is True):
                                while (final == syllable[-1]):
                                    final = finals[r.randint(0, len(finals) - 1)]
                                syllable = syllable + final
                                j += 1
                            else:
                                syllable = syllable + final
                                j += 1
                        else:
                            syllable = syllable + final
                            j += 1
                    else:
                        j += 1
                    if j == len(phonotype):
                        syllableList.append(syllable)
        i += 1
    return syllableList


if __name__ == '__main__':
    main()
