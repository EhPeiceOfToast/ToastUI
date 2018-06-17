print "ToastUI v0.01"
print "ToastUI is still in development! Reporting bugs or errors is appreciated!"
input = "placeholder"
sto1 = 0
while sto1 == 0:
  input = raw_input("Enter a command. If you're new to ToastUI, use the 'help' command.")
  if input == "help":
    print "Avalible commands are 'help', 'load', and 'shutdown'."
  elif input == "shutdown":
    sto1 = 1
  elif input == "load":
    sto1 = 1
    input = raw_input("Specify a module to load. Default modules are 'calculator'.")
    sto2 = 0
    while sto2 == 0:
      if input == "calculator":
        open(calculator)
        sto2 == 1
      else:
        print "That's not a valid module."
  else:
    print "That's not a command."
