from env import *
import command.exit
import command.login

while True:
    cmd = input(">>> ")

    module: Any = None
    if cmd == "exit":
        module = command.exit
    elif cmd == 'login':
        module = command.login


    if module == None and module.run == None:
        show_error("Run function not found")
        continue
    else:
        module.run()



    
