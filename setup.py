from cx_Freeze import setup, Executable

buildOptions = dict(includes=["qtconsole.rich_jupyter_widget","qtconsole.inprocess","matplotlib.pyplot","tkinter.filedialog", "matplotlib.figure","matplotlib.backends.backend_qt4agg","matplotlib.backends.backend_tkagg"],include_files = ["design/","modules/","graph.png","file1.png","column.png","machine learning.png","new.png","rows.jpg","typesSave.png","script4.jpg","ico.png","report4.png","table2.jpg"])

setup(
    name="GUI PROGRAM",
    version="0.1",
    description="MyEXE",
    options = dict(build_exe = buildOptions),
    executables=[Executable("aina_navigator.py", base="Win32GUI")]
    )
