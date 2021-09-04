import nuke
import nukeScriptShare

rk_menu = nuke.toolbar("Nuke")
RK_menu = rk_menu.addMenu('RK_Menu')
RK_menu.addCommand('Nukesharescript', 'nukeScriptShare.main()')
