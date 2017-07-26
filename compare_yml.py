#!/usr/bin/python
import sys
import yaml
def main():
        gold_standard = sys.argv[1]
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        print(gold_standard,input_file,output_file)

        with open(gold_standard, 'r') as g_s:
                g_s_config = yaml.load(g_s)

        with open(input_file, 'r') as i_f:
                i_f_config = yaml.load(i_f)
        for key in g_s_config["ora_asm"][0]:
                #print("aaa")
                #print(key)
                #print(type(g_s_config["ora_asm"][0][key]))
                temp_type = type(g_s_config["ora_asm"][0][key])
                if (temp_type is list) or (temp_type is str):
                        #print("bbb")
                        #print("step A: " + key)
                        print(type(g_s_config["ora_asm"][0][key]))
                        ### Level 2 ###
                        if type(key) is list:
                                for element in range(len(g_s_config["ora_asm"][0][key])):
                                        print("step B: " + str(element))
                                        ### Level 3 ###
                                        #print(type(g_s_config["ora_asm"][0][key]))
                                        if type(element) is list:
                                                print("Step E: " + element)
                                                for item in g_s_config["ora_asm"][0][key][element]:
                                                        print("Step D: " + item)
                                                        if item not in i_f_config["ora_asm"][0][key][element]:
                                                                #print(type(g_s_config["ora_asm"][0][key][element]))
                                                                print("aaa")
                                                                i_f_config["ora_asm"][0][key][element][item] = ''
                        if type(key) is str:
                                #print("Step C: " + key)
                                if key not in i_f_config["ora_asm"][0]:
                                        i_f_config["ora_asm"][0][key] = ''
        with open(output_file, 'w') as o_f:
                o_f.write(yaml.dump(i_f_config, default_flow_style=False))




if __name__ == '__main__':
    main()

