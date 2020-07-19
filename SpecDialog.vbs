Dim Arg, msg
Set Arg = WScript.Arguments

'Parameter1, begin with index0
msg = Arg(0)

msgbox "Your Support ID Is: " _
       & msg

'Clear the objects at the end of your script.
set Arg = Nothing