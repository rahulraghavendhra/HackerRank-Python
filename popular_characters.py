"""
Pǿpųłǻř Čħǻřǻčțěřș (Čǿđıňģ)
Ỳǿų ħǻvě ǻ łıșț ǿf șțřıňģș, ěǻčħ ǿf ẅħıčħ ıș čǿmpǿșěđ ǿf łǿẅěřčǻșě łěțțěřș
fřǿm 'ǻ' țǿ 'ž'. Ǻ "pǿpųłǻř" čħǻřǻčțěř ıș đěfıňěđ țǿ bě ǿňě ẅħıčħ ǻppěǻřș ıň
ǻłł țħě șțřıňģș.
Ģıvěň ǻ łıșț ǿf șțřıňģș, čǿųňț țħě ňųmběř ǿf pǿpųłǻř čħǻřǻčțěřș.
İňpųț Fǿřmǻț
Țħě fıřșț łıňě čǿňșıșțș ǿf Ň, țħě ňųmběř ǿf șțřıňģș.
Țħě ňěxț Ň łıňěș ǻřě țħě Ň șțřıňģș (čǿmpǿșěđ ǿf łǿẅěřčǻșě łěțțěřș fřǿm 'ǻ'
țǿ 'ž').
Ǿųțpųț Fǿřmǻț
Přıňț țħě ňųmběř ǿf pǿpųłǻř čħǻřǻčțěřș ıň țħě șțřıňģș. İf țħěřě ǻřě ňǿňě,
přıňț 0.
Čǿňșțřǻıňțș
1 ≤ Ň ≤ 100
Ěǻčħ șțřıňģ čǿňșıșțș ǿf ǿňłỳ șmǻłł łǻțıň łěțțěřș ('ǻ'-'ž').
1 ≤ Łěňģțħ ǿf ěǻčħ șțřıňģ ≤ 100
Șǻmpłě İňpųț
3
abcdde
baccd
eeabg
Șǻmpłě Ǿųțpųț
2
Ěxpłǻňǻțıǿň
Țħě ǿňłỳ pǿpųłǻř čħǻřǻčțěřș ǻřě 'ǻ' ǻňđ 'b', șıňčě țħěșě ǻřě țħě ǿňłỳ
čħǻřǻčțěřș țħǻț ǻppěǻř ıň ěvěřỳ șțřıňģ.
"""
main_dict = {}
count = 0
if __name__ == '__main__':
    n = input()
    for i in range(n):
        input_string = raw_input()
        str_array = set(input_string)
        for char in str_array:
            if char in main_dict:
                main_dict[char] = main_dict[char] + 1
            else:
                main_dict[char] = 1
    for element in main_dict:
        if main_dict[element] == int(n):
            count = count + 1
    if count == 0:
        print "No Common characters in the string"
    else:
        print count


