#!/usr/bin/python
import sys
import yaml

def main():
    gold_standard = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    print(gold_standard, input_file, output_file)
    with open(gold_standard, 'r') as g_s:
        g_s_config = yaml.load(g_s)
    with open(input_file, 'r') as i_f:
        i_f_config = yaml.load(i_f)
    ''' LEVEL 1 '''
    for key in g_s_config["ora_asm"][0]:
        print("- Level 1 list - key " + str(key) + " - Type - " + str(type(g_s_config["ora_asm"][0][key])))
        key_l1 = g_s_config["ora_asm"][0][key]
        ''' LEVEL 1 list '''
        if type(key_l1) is list:
            ''' LEVEL 2 '''
            for element in range(len(g_s_config["ora_asm"][0][key])):
                print("    - Level 2 - key " + str(element) + " - Type - " + str(type(g_s_config["ora_asm"][0][key][element])))
                key_l2 = g_s_config["ora_asm"][0][key][element]
                if type(key_l2) is dict:
                    ''' LEVEL 3 '''
                    for item in g_s_config["ora_asm"][0][key][element]:
                        print("        - Level 3 - key " + str(item) + " - Type - " + str(type(g_s_config["ora_asm"][0][key][element][item])))
                        ''' try will add entries only into existing blocks '''
                        try:
                            if item not in i_f_config["ora_asm"][0][key][element]:
                                i_f_config["ora_asm"][0][key][element][item] = ''
                        except:
                            pass
        ''' LEVEL 1 string '''
        if type(key_l1) is str:
            print("    - Level 1 string - key " + str(key) + " - Type - " + str(type(g_s_config["ora_asm"][0][key][element])))
            if key not in i_f_config["ora_asm"][0]:
                i_f_config["ora_asm"][0][key] = ''
    with open(output_file, 'w') as o_f:
        o_f.write(yaml.dump(i_f_config, default_flow_style=False))


if __name__ == '__main__':
    main()
