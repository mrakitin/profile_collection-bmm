from IPython.core.magic import register_line_magic  #, register_cell_magic, register_line_cell_magic)

run_report(__file__, text='ipython magics for BMM')


@register_line_magic
def h(line):
    '''BMM help text'''
    BMM_help()
    return None

@register_line_magic
def k(line):
    '''help on ipython keyboard shortcuts'''
    BMM_keys()
    return None

@register_line_magic
def ut(line):
    '''show BMM utilities status'''
    su()
    return None

@register_line_magic
def v(line):
    '''show BMM vacuum status'''
    show_vacuum()
    return None

@register_line_magic
def se(line):
    '''show foils and ROIs cnfiguration'''
    show_edges()
    return None

@register_line_magic
def h2o(line):
    '''show BMM DI and PCW water status'''
    sw()
    return None

@register_line_magic
def m(line):
    '''show BMM motor status'''
    ms()
    return None

@register_line_magic
def xm(line):
    '''show XRD motor status'''
    xrdm()
    return None

@register_line_magic
def w(arg):
    '''show a motor position'''
    motor = eval(arg)
    return motor.wh()

@register_line_magic
def ca(arg):
    '''close all plots'''
    close_all_plots()
    return None
