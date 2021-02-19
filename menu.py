import nuke
import sys
from nukescripts import panels

rk_menu = nuke.toolbar("Nuke")
RK_menu = rk_menu.addMenu('RK_Menu')
RK_menu.addCommand('Nukesharescript', 'share_script()')


def share_script():
    try:
        del sys.modules['NukeShareScript']
    except:
        import NukeShareScript
        NukeShareScript.main()
