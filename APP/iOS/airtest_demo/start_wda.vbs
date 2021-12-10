dim args
Set args = WScript.Arguments

Set ws = CreateObject("Wscript.Shell")
ws.run "cmd /c " &args(0) &args(1) &args(2) &args(3),0
