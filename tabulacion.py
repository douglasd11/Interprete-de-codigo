def tab(lista):
    ls_tab = []
    con_fun = 0  #contador

    sym_tab = '\t'
    for x in range(len(lista)):

        ls_ax = lista[x].split()
        n_tab = (sym_tab * con_fun)
        cad_aux = n_tab + lista[x]
        if len(ls_ax) > 0:
            if ls_ax[0] == "FINF":
                con_fun -= 1

            else:
                ls_tab.append(cad_aux)
            if ls_ax[0] == "FUNCION":
                con_fun += 1



    return ls_tab