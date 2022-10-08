#Factorio Modpack Helper - Helps in making modpacks for Factorio.


#Functions
def get_mods():
    global IS_DEBUG
    global KEYWORD
    global PREFIXES

    global main_mods
    global optional_mods
    global incompatible_mods

    try:
        mod_links_txt=open("mod_links_input.txt","r")
        mod_links=mod_links_txt.read().splitlines()
    except:
        mod_links_txt=open("mod_links_input.txt","x")
        mod_links=[]
    mod_links_txt.close()

    for pos in range(0,len(mod_links)):
        current_mod=mod_links[pos][(mod_links[pos].find(KEYWORD)+len(KEYWORD)):]

        if mod_links[pos][0] == PREFIXES[0]:
            optional_mods.append(current_mod)
        elif mod_links[pos][0] == PREFIXES[1]:
            incompatible_mods.append(current_mod)
        else:
            main_mods.append(current_mod)

    if IS_DEBUG:
        print("\n\nmod_links: "+str(mod_links)+"\nmain_mods: "+str(main_mods)+"\noptional_mods: "+str(optional_mods)+"\nincompatible_mods: "+str(incompatible_mods))

def construct_mod_list():
    global IS_DEBUG

    global main_mods
    global optional_mods
    global incompatible_mods
    mod_list='"dependencies": ['

    main_mods.sort()
    optional_mods.sort()
    incompatible_mods.sort()

    for current_mod in main_mods:
        mod_list+='"'+current_mod+'", '
    for current_mod in optional_mods:
        mod_list+='"? '+current_mod+'", '
    for current_mod in incompatible_mods:
        mod_list+='"! '+current_mod+'", '

    mod_list=mod_list[:len(mod_list)-2]+"]"

    mod_list_txt=open("mod_list_output.txt","w")
    mod_list_txt.write(mod_list)
    mod_list_txt.close()

    if IS_DEBUG:
        print("mod_list: "+mod_list+"\n\n")

#Constants
KEYWORD="mod/"
PREFIXES=["?","!"]
IS_DEBUG=False

#Global Variables
main_mods=[]
optional_mods=[]
incompatible_mods=[]

#Main Program
get_mods()
construct_mod_list()