
from BMM.metadata import TC, Ring

run_report(__file__, text='miscellaneous metadata and the baseline')

first_crystal  = TC('XF:06BMA-OP{Mono:DCM-Crys:1}',      name='first_crystal')
compton_shield = TC('XF:06BMA-OP{Mono:DCM-Crys:1-Ax:R}', name='compton_shield')

ring = Ring('SR', name='ring')

sd.baseline = (xafs_linx, xafs_liny, xafs_pitch, xafs_wheel, xafs_ref, #xafs_roll, xafs_linxs, xafs_roth, xafs_rots,
               dm3_bct, dm3_foils, dm2_fs,
               dcm_x, dcm_pitch, dcm_roll,
               slits3.top, slits3.bottom, slits3.outboard, slits3.inboard, slits3.vsize, slits3.vcenter, slits3.hsize, slits3.hcenter, 
               slits2.top, slits2.bottom, slits2.outboard, slits2.inboard, slits2.vsize, slits2.vcenter, slits2.hsize, slits2.hcenter,
               #m1.yu, m1.ydo, m1.ydi, m1.xu, m1.xd, m1.vertical, m1.lateral, m1.pitch, m1.roll, m1.yaw,
               m2.yu, m2.ydo, m2.ydi, m2.xu, m2.xd, m2.vertical, m2.lateral, m2.pitch, m2.roll, m2.yaw, m2_bender,
               m3.yu, m3.ydo, m3.ydi, m3.xu, m3.xd, m3.vertical, m3.lateral, m3.pitch, m3.roll, m3.yaw,
               xafs_table.yu, xafs_table.ydo, xafs_table.ydi, xafs_xu , xafs_xd,
               xafs_table.vertical, xafs_table.pitch, xafs_table.roll, 
)

#sd.baseline = ()
