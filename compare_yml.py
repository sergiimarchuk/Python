#!/usr/bin/python
import yaml

print "******** Pars struncture asm_soft ******************************"; print " "*5

def rebuild_dict(_get_dict,orig_key_dic_value):
        var_list = list(_get_dict)
        list_values = []
        d = {}
        for _get_dict_list_key in var_list:
                _get_dict_value = _get_dict.get(_get_dict_list_key)
                if type(_get_dict_value) is dict:
                        ##print _get_dict_list_key#,"-------------",_get_dict_value
                        list_values.append(_get_dict_list_key)
                else:
                        ##print  value + "  OOOO", _get_dict_list_key#,"+++++++++++++",_get_dict_value
                        list_values.append(_get_dict_list_key)
        d[orig_key_dic_value]=list_values
        ##print value,list_values
        ##print " hm ...",d
        #return "hm ..." + str(d)
        return d

def read(path):
        with open(path, 'r') as fp:
           my_config = yaml.load(fp)

        asm_soft_dict = my_config["ora_asm"][0]["asm_soft"]
        return asm_soft_dict


'''def collect_into_list(func):
    collect_list = []
    def wrapper2(a):
        collect_list.append(func(a))
        print "aaaaaaaaaaaaaaaaaaaaaa", collect_list
    return wrapper2'''


#@collect_into_list
def compare_structure(path):
        list_finish = []
        asm_soft_list = list(read(path).keys())
        for asm_soft_list_key in asm_soft_list:
                asm_soft_value = read(path).get(asm_soft_list_key)
                d = {}
                if type(asm_soft_value) is dict:
                        ##print asm_soft_list_key,"-------dict--------------podstructure  ::: ",asm_soft_value
                        ##print rebuild_dict(asm_soft_value,asm_soft_list_key)
                        list_finish.append(rebuild_dict(asm_soft_value,asm_soft_list_key))
                else:
                        ##print asm_soft_list_key,"_______NOT_dict__________podstructure  ::: ",asm_soft_value
                        d = dict.fromkeys([asm_soft_list_key])
                        ##print d
                        ##print "wow ...",d
                        list_finish.append(d)
        #print "lllllllllllllllll", list_finish
        return list_finish
c1 = compare_structure("/home/user/link-nfs/Yakiv/ansible_1/host_vars/xadago/test/wora_asm.yml")
print c1

c2 = compare_structure("/home/user/link-nfs/Yakiv/ansible_1/host_vars/dlt-star-hob-st22/ora_asm.yml")
print c2
'''
#for i in (c1):
#       print type(i),i,len(c1)

comp = c1, c2
#rint comp
#rint type(comp)
for ij in comp:
        for m in ij:
                anchor_key = (str(m)).split(":")[0].replace("{","").replace("'",""); #print anchor_key;
                anchor_value = (str(m)).split(":")[1].replace("}","") ;
                if "None" in anchor_value:
                        print anchor_key
                else:
                        print anchor_key, anchor_value

                #k = m.keys();# v = m.values()
                #print k#, v
                #for l in v:
                #       print k,l
'''
