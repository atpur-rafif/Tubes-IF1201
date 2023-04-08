from env import *
import command.exit

while True:
    cmd = input(">>> ")

    module: Any = None
    if cmd == "exit":
        module = command.exit

    if module == None and module.run == None:
        show_error("Run function not found")
        continue
    else:
        module.run()



    
