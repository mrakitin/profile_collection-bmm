run_report(__file__, text='Monochromator definitions')

from BMM.dcm import DCM

dcm = DCM('XF:06BMA-OP{Mono:DCM1-Ax:', name='dcm', crystal='111')
if dcm_x.user_readback.get() > 10: dcm.set_crystal('311')
