
def _check_first_position(area, district, sector, unit):
    """
    The letters Q, V and X are not used in the first position.
    """
    return area[0] not in ('Q', 'V', 'X')

def _check_second_position(area, district, sector, unit):
    """
    The letters I, J and Z are not used in the second position.
    """
    if len(area) == 1:
        return True

    return area[1] not in ('I', 'J', 'Z')

def _check_third_position(area, district, sector, unit):
    """
    The only letters to appear in the third position are A, B, C, D, E, F, G, H, J, K, P, S, T, U and W when the structure starts with A9A.
    """
    if len(area) == 2:
        return True

    if len(district) == 1:
        return True

    if district[1].isdigit():
        return True

    return district[1] in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'P', 'S', 'T', 'U', 'W')


def _check_fourth_position(area, district, sector, unit):
    """
    The only letters to appear in the fourth position are A, B, E, H, M, N, P, R, V, W, X and Y when the structure starts with AA9A.
    """
    if len(area) == 1:
        return True

    if len(district) == 1:
        return True

    if district[1].isdigit():
        return True

    return district[1] in ('A', 'B', 'E', 'H', 'M', 'N', 'P', 'R', 'V', 'W', 'X', 'Y')


def _check_final_two_letters(area, district, sector, unit):
    """
    The final two letters do not use C, I, K, M, O or V, so as not to resemble digits or each other when hand-written.
    """
    check_tuple = ('C', 'I', 'K', 'M', 'O', 'V')
    return unit[0] not in check_tuple and unit[1] not in check_tuple


def _check_only_one_double_position(area, district, sector, unit):
    """
    Areas with only double-digit districts: AB, LL, SO
    """
    if area not in ('AB', 'LL', 'SO'):
        return True

    if len(district) == 1:
        return False

    return district[1].isdigit()

def _check_zero_district(area, district, sector, unit):
    """
    Areas with a district '0' (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS (BS is the only area to have both a district 0 and a district 10)
    """
    if district == '0':
        return area in ('BL', 'BS', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS')

    if district == '10':
        return area not in ('BL', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS')

    return True


def _check_single_digit_district(area, district, sector, unit):
    """
    Areas with only single-digit districts: BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE
    (although WC is always subdivided by a further letter, e.g. WC1A) - check in London
    """
    if area not in ('BR', 'FY', 'HA', 'HD', 'HG', 'HR', 'HS', 'HX', 'JE', 'LD', 'SM', 'SR', 'WN', 'ZE'):
        return True

    return len(district) == 1


def _check_central_london(area, district, sector, unit):
    """
    The following central London single-digit districts have been further divided by inserting a letter after the digit and before the space:
    EC1–EC4 (but not EC50), SW1, W1, WC1, WC2 and parts of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P).
    """
    is_last_alpha = (len(district) == 2 and district[1].isalpha())
    is_full_central_london = ((area == 'EC' and '1' <= district[0] <= '4') or
                              (area == 'WC'))
    if is_full_central_london:
        return is_last_alpha

    if area == 'W' and district[0] == '1':
        return len(district) == 2

    if area == 'SW' and district[0] == '1':
        return len(district) == 2

    if area == 'E' and district[0] == '1':
        return len(district) == 1 or district[1].isdigit() or district[1] == 'W'

    if area == 'N' and district[0] == '1':
        return len(district) == 1 or (district[1].isdigit() or district[1] in ('C', 'P'))

    if area == 'NW' and district[0] == '1':
        return len(district) == 1 or (district[1].isdigit() or district[1] == 'W')

    if area == 'SE' and district[0] == '1':
        return len(district) == 1 or district[1].isdigit() or district[1] == 'P'

    return not is_last_alpha
#Postcode sectors are one of ten digits: 0 to 9, with 0 only used once 9 has been used in a post town, save for Croydon and Newport (see above).


def _check_single_character(area, district, sector, unit):
    """
    A9 9AA
    A99 9AA    B, E, G, L, M, N, S, W
    """
    if len(area) == 2:
        return True

    if len(district) == 2 and district[1].isdigit():
        return True

    # stay only case 'A9', 'A99'
    return area in ('B', 'E', 'G', 'L', 'M', 'N', 'S', 'W')
